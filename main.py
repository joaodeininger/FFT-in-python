import numpy as np

try:
    # arch = input("Digite o nome do arquivo de entrada: ")
    data_float = np.loadtxt(
        input("Digite o nome do arquivo de entrada: "), dtype=complex
    )
    entry = np.array(data_float)
except FileNotFoundError:
    # Lógica para lidar com o arquivo não encontrado
    print("Erro: O arquivo não foi encontrado!")
except IOError:
    # Lógica para outros erros de entrada/saída (como permissão)
    print("Erro: Problema de leitura/escrita no arquivo.")
except Exception as e:
    # Captura de qualquer outro erro inesperado
    print(f"Ocorreu um erro inesperado: {e}")

print("\n--- Resultado da Entrada ---")
print(entry)
print(f"Tamanho do array: {len(entry)}")
