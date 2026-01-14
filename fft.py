import numpy as np
from pandas import read_csv

def zero_padding(cpx, N):
    # zero-padding
    if (N & (N - 1) != 0) or N == 0:
        print(
            f"Aviso: O tamanho do sinal (N={N}) não é uma potência de 2. Realizando zero-padding..."
        )
        # arredonda N para a próxima potência de 2
        N_otimo = 2 ** np.ceil(np.log2(N))
        # parametros:(dados,(antes,     depois),  constante)
        cpx = np.pad(cpx, (0, int(N_otimo - N)), "constant")
        # atualiza N
        N = len(cpx)
    return cpx, N


def n_padding(cpx, L):

    print(f"Aviso: O tamanho do sinal ({cpx=} = {len(cpx)}) não é uma potência de 2. Realizando zero-padding...")
    # parametros:(dados,(antes,     depois),  constante)
    cpx = np.pad(cpx, (0, int(L - len(cpx))), "constant")
    print(f"tamanho depois: {len(cpx)}")
    return cpx


def ifft(X):
    """
    IFFT usando a relação:
    ifft(X) = conj( fft( conj(X) ) ) / N
    """
    X = np.asarray(X, dtype=complex)
    N = len(X)
    return np.conjugate(t_fft(np.conjugate(X))) / N


def bit_reverse(x):
    """
    Reordena o array x permutando os índices com seus reversos binários.
    Ex: Para N=8 (000...111), o índice 1 (001) troca com 4 (100).
    """
    N = len(x)
    j = 0
    for i in range(1, N):
        # Lógica de "soma binária invertida" para encontrar o próximo índice reverso
        bit = N >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        # Troca os elementos se i < j (para evitar trocar duas vezes)
        if i < j:
            x[i], x[j] = x[j], x[i]
    return x


# FFT por Decimação no Tempo (T_FFT)
def t_fft(cpx, sign=-1):
    # Garante tipo complexo e cópia para não alterar o original externamente
    a = np.asarray(cpx, dtype=np.complex128)
    N = len(a)
    a, N = zero_padding(a, N)

    # propriedade das exponenciais na FFT: exp(sign * 2j * pi * k / N) = W_N^k
    k_indices = np.arange(N // 2)
    # tabela de lookup
    tab = np.exp(sign * 2j * np.pi * k_indices / N)
    # Revertendo os bits na entrada
    a = bit_reverse(a)

    # Butterfly
    # iterações da FFT (log2 N iterações)
    it = int(np.log2(N))

    for s in range(1, it + 1):
        m = 1 << s  # Tamanho do bloco atual (2, 4, 8...)
        m2 = m >> 1  # Metade do bloco

        #passo na tabela de lookup
        passo = N // m

        # nesse loop, k varia de 0 a N-1, pulando de m em m
        for k in range(0, N, m):
            # nesse loop, j varia de 0 a m/2-1
            for j in range(m2):
                w = tab[j * passo]
                # butterflies
                t = w * a[k + j + m2]
                u = a[k + j]
                # atualiza os valores
                a[k + j] = u + t
                a[k + j + m2] = u - t

    return a


# FFT por Decimação na Frequência (F_FFT)
def f_fft(cpx, sign=-1):
    #Paramêtros: (cpx: Array de dados complexos de entrada, sign: Direção da transformação (-1 para Forward, 1 para Inverse))
    a = np.asarray(cpx, dtype=np.complex128)
    # Encontra o N a partir do array original de entrada
    N = len(a)
    
    a, N = zero_padding(a, N)
    
    # Total de estágios = log2(N)
    # m é o tamanho do bloco atual, começa em N e vai dividindo por 2
    m = N
    
    while m >= 2:
        m2 = m // 2  # Metade do bloco (// divide e arredonda para baixo, caso não seja inteiro)
        
        # O ângulo é sempre 2*pi * j / m
        # Usando a lógica de tabela similar ao t_fft para consistência, mas adaptada
        
        # k varrendo de 0 a N-1, pulando de m em m
        for k in range(0, N, m):
            # Itera sobre a primeira metade do bloco
            for h in range(m2):
                # butterflies
                # w = exp(sign * 2j * pi * j / m)
                w = np.exp(sign * 2j * np.pi * h / m)
                
                u = a[k + h]
                t = a[k + h + m2]
                
                # butterflies
                # Parte superior: u + t
                # Parte inferior: (u - t) * w
                a[k + h] = u + t
                a[k + h + m2] = (u - t) * w
        
        m = m2  # Próximo estágio (metade do tamanho)
        
    # Bit-reverse ocorre no FINAL para a DIF
    a = bit_reverse(a)
    
    return a


def seccionada(x, h):
    """
    Overlap-Add algorithm for linear convolution

    x : sinal de entrada (1D array)
    h : FIR filter (1D array)

    retorna: y = x * h (convolução linear)
    """
    # Garante que x e h sejam arrays numpy
    x = np.asarray(x).ravel()
    h = np.asarray(h).ravel()

    N1= len(x)
    N2 = len(h)
    # L = 2^ceiling(log2(N2))
    L = 2 ** (int(np.ceil(np.log2(N2))) + 1)

    # N3 = L/2
    N3 = int(L/2)

    # FFT do filtro, zero-padded até L
    h = n_padding(h, L)
    H = t_fft(h)

    # saída (convolução linear tem tamanho N1 + N2 - 1)
    y = np.zeros(N1 + N2 - 1)

    position = 0

    while position + N3 <= N1:
        # bloco de entrada
        x_block = x[position : position + N3]

        # FFT do bloco (zero-padding automático até L)
        x_padded = n_padding(x_block, L)
        X = t_fft(x_padded)

        # convolução no domínio da frequência
        y_block = ifft(X * H)
        y_re = np.real(y_block)
        # overlap-add
        y[position : position + L] += y_re

        position += N3

    return y


def read_input():
    input_file = input("Digite o nome do arquivo de entrada: ")
    try:
        df = read_csv(input_file, sep=" ", header=None)
    # se tiver uma coluna, entrada real
        if df.shape[1] == 1:
            dados_complexos = df.iloc[:, 0].to_numpy(dtype=np.complex128)
        # se tiver duas colunas, entrada complexa
        elif df.shape[1] == 2:
            real = df.iloc[:, 0].to_numpy()
            imag = df.iloc[:, 1].to_numpy()
            dados_complexos = real + 1j * imag

        return dados_complexos
    
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        exit()
    