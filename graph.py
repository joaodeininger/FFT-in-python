import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def converter_complexo_python(s):
    """
    Converte strings do formato padrão Python '(r+ij)' para objetos complexos.
    Remove parênteses se existirem.
    """
    try:
        s = str(s).replace('(', '').replace(')', '')
        return complex(s)
    except ValueError:
        return complex(0)

# --- INÍCIO DO PROGRAMA ---

print("=== Gerador de Gráficos de Sinais (Python) ===")

# 1. Input do Nome do Arquivo
arquivo = input("Nome do arquivo (ex: sinal_fft.csv): ")
caminho = f"resultados/{arquivo}"

if not os.path.exists(caminho):
    print(f"Erro: Arquivo '{caminho}' não encontrado.")
    exit()

# 2. Input do Tipo de Gráfico
print("\nSelecione o tipo de sinal:")
print("1 - Sinal Real (ex: áudio, senoides, dados brutos)")
print("2 - Sinal Complexo (ex: Saída de FFT/DFT)")
opcao = input("Digite o número (1 ou 2): ").strip()

# Leitura do Arquivo
try:
    if opcao == '2':
        # Se é complexo, aplicamos o conversor na coluna 0
        dados = pd.read_csv(caminho, header=None, converters={0: converter_complexo_python})
        y_vals = dados.iloc[:, 0].values # Vetor de números complexos
    else:
        # Se é real, leitura padrão
        dados = pd.read_csv(caminho, header=None)
        y_vals = dados.iloc[:, 0].values # Vetor de floats
        
    N = len(y_vals)
    n = np.arange(N)

except Exception as e:
    print(f"Erro ao ler os dados: {e}")
    print("Dica: Verifique se o arquivo não tem cabeçalho ou caracteres estranhos.")
    exit()

# 3. Geração dos Gráficos
plt.figure(figsize=(10, 7))

if opcao == '2':
    # === MODO FFT / COMPLEXO ===
    # Calcula Magnitude e Fase
    magnitude = np.abs(y_vals)
    fase = np.angle(y_vals)

    # Plot 1: Magnitude
    plt.subplot(2, 1, 1)
    plt.stem(n, magnitude)
    plt.title("Magnitude |X[n]|")
    plt.ylabel("Amplitude")
    plt.grid(True, linestyle='--', alpha=0.7)

    # Plot 2: Fase
    plt.subplot(2, 1, 2)
    plt.stem(n, fase)
    plt.title("Fase (Radianos)")
    plt.xlabel("n (Amostras)")
    plt.ylabel("Fase")
    plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], 
               [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$']) # Formatação bonita para pi
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()

else:
    # === MODO REAL ===
    plt.stem(n, y_vals)
    plt.axhline(0, color="black", linewidth=1)
    plt.title("Sinal em Tempo Discreto")
    plt.xlabel("n (Amostras)")
    plt.ylabel("Amplitude x[n]")
    plt.grid(True, linestyle='--', alpha=0.7)

print("Gerando gráfico...")
plt.show()