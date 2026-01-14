import time

import numpy as np
import pandas as pd

import fft as ft

# inicia o timer para medir o tempo de execução do código
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
    exit()

N = len(dados_complexos)

print("---Escolha uma das opções abaixo: ---")
print("1 - FFT por decimação no tempo")
print("2 - FFT por decimação no frequência")
print("0 - Sair")

opcao = int(input("Opção: "))

if opcao == 0:
    exit()

elif opcao == 1:
    # chama a fft por decimação no tempo
    X = ft.t_fft(dados_complexos)

elif opcao == 2:
    # chama a fft por decimação no frequência
    X = ft.f_fft(dados_complexos)

else:
    print("Opção inválida!")
    exit()

# arredondamento de numeros (util para uso do pi, que acaba ficando muito grande)
y = np.round(X, decimals=10)

# exibe o resultado
print(y)

# finaliza o timer e exibe o tempo de execução
fim = time.time()
print(f"Tempo de execução: {fim - inicio:.6f} segundos")
