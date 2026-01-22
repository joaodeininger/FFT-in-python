import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

### Esse arquivo gera gráficos de sinais discretos

# Recebe do usuário o nome do arquivo para gerar gráfico
arquivo = input(
    "Digite o nome do arquivo para gerar gráfico (o arquivo deve estar na pasta resultados): "
)

# Lê o arquivo na pasta resultados com o nome do arquivo que o usuário digitou
dados = pd.read_csv(f"resultados/{arquivo}")

# Se o CSV tiver apenas uma coluna
y_vals = dados.iloc[:, 0].values   # vetor 1D
N = len(y_vals)

# Tempo discreto
n = np.arange(N)

# Parâmetros do gráfico
plt.figure()
plt.stem(n, y_vals)
plt.axhline(0, color="black", linewidth=0.8)

plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("Sinal em Tempo Discreto")
plt.grid(True)
# Mostra o gráfico na janela do matplotlib, com opção de salvar a figura
plt.show()
