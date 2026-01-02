import time

import numpy as np
import pandas as pd

import fft as ft

inicio = time.time()

try:
    df = pd.read_csv("entrada.txt", sep=" ", header=None)

    # se tiver uma coluna, entrada real
    if df.shape[1] == 1:
        dados_complexos = df.iloc[:, 0].to_numpy(dtype=np.complex128)

    # se tiver duas colunas, entrada complexa
    elif df.shape[1] == 2:
        real = df.iloc[:, 0].to_numpy()
        imag = df.iloc[:, 1].to_numpy()
        dados_complexos = real + 1j * imag
except Exception as e:
    print(f"Erro ao ler arquivo: {e}")
    dados_complexos = "Não foram encontrados dados!"

N = len(dados_complexos)

# zero-padding
if (N & (N - 1) != 0) or N == 0:
    print(
        f"⚠️ Aviso: O tamanho do sinal (N={N}) não é uma potência de 2. Realizando zero-padding..."
    )

    N_otimo = 2 ** np.ceil(np.log2(N))
    dados_complexos = np.pad(dados_complexos, (0, int(N_otimo - N)), "constant")
    N = len(dados_complexos)

# fft por decimação no tempo
X = ft.t_fft(dados_complexos)

# arredondamento
y = np.round(X, decimals=10)

print(y)

fim = time.time()
print(f"Tempo de execução: {fim - inicio:.6f} segundos")
