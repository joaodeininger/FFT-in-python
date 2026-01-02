import numpy as np


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


def t_fft(x):
    # Garante tipo complexo e cópia para não alterar o original externamente
    a = np.array(x, dtype=np.complex128)
    N = len(a)

    # propriedade das exponenciais na FFT
    k_indices = np.arange(N // 2)
    twiddle_table = np.exp(-2j * np.pi * k_indices / N)
    # Revertendo os bits na entrada para não precisar fazer na saída
    a = bit_reverse(a)

    # Butterfly
    # iterações da FFT (log2 N iterações)
    it = int(np.log2(N))

    for s in range(1, it + 1):
        m = 1 << s  # Tamanho do bloco atual (2, 4, 8...)
        m2 = m >> 1  # Metade do bloco

        # Passo (stride) na tabela de lookup
        # Se m=N, step=1. Se m=2, step=N/2.
        step = N // m

        for k in range(0, N, m):
            # Em vez de multiplicar w *= Wm iterativamente (que acumula erro numérico),
            # acessamos diretamente a tabela pelo índice j * step.
            for j in range(m2):
                # Acesso O(1) à tabela pré-calculada
                w = twiddle_table[j * step]

                t = w * a[k + j + m2]
                u = a[k + j]

                a[k + j] = u + t
                a[k + j + m2] = u - t

    return a


def f_fft(cpx, n, sign):
    return
