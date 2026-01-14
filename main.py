import time
from pandas import read_csv
import fft as ft
from numpy import round

print("---Escolha uma das opções abaixo: ---")
print("1 - FFT por decimação no tempo")
print("2 - FFT por decimação no frequência")
print("3 - Convolução Seccionada")
print("0 - Sair")

opcao = int(input("Opção: "))

if opcao == 0:
    exit()

elif opcao == 1:
    # chama a fft por decimação no tempo
    dados_complexos = ft.read_input()
    # inicia o timer para medir o tempo de execução do código
    inicio = time.time()
    y = ft.t_fft(dados_complexos)

elif opcao == 2:
    # chama a fft por decimação no frequência
    dados_complexos = ft.read_input()
    # inicia o timer para medir o tempo de execução do código
    inicio = time.time()
    y = ft.f_fft(dados_complexos)

elif opcao == 3:
    x = read_csv("convolution/xn.txt", sep=" ", header=None)
    h = read_csv("convolution/hn.txt", sep=" ", header=None)
    # inicia o timer para medir o tempo de execução do código
    inicio = time.time()
    # chama a convolução seccionada
    y = ft.seccionada(x, h)

else:
    print("Opção inválida!")
    exit()

# arredondamento de numeros (util para uso do pi, que acaba ficando muito grande)
y = round(y, decimals=10)

# exibe o resultado
print(y)

# finaliza o timer e exibe o tempo de execução
fim = time.time()
print(f"Tempo de execução: {fim - inicio:.6f} segundos")
