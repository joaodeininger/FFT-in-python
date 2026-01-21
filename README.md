# FFT & Discrete Signal Processing

Este projeto contém implementações em Python de algoritmos fundamentais de Processamento Digital de Sinais (DSP), com foco na Transformada Rápida de Fourier (FFT) e Convolução Linear.

## 🚀 Funcionalidades

- **FFT por Decimação no Tempo (DIT):** Implementação clássica de Cooley-Tukey que reordena os dados via *bit-reversal* antes do estágio de *butterflies*.
- **FFT por Decimação na Frequência (DIF):** Implementação que realiza os estágios de *butterflies* primeiro e reordena o resultado final.
- **Transformada Inversa (IFFT):** Cálculo da IFFT utilizando a relação de conjugação com a FFT.
- **Convolução Seccionada (Overlap-Add):** Algoritmo eficiente para realizar a convolução linear entre sinais longos e filtros, utilizando o domínio da frequência.
- **Zero-Padding Automático:** Ajuste automático do tamanho do sinal para a próxima potência de 2, otimizando a performance dos algoritmos.
- **Suporte a Dados Complexos:** Capacidade de ler e processar arquivos com entradas reais (uma coluna) ou complexas (duas colunas: real e imaginário).

## 📁 Estrutura do Projeto

- `fft.py`: Biblioteca principal contendo os núcleos de processamento (DIT-FFT, DIF-FFT, IFFT, Overlap-Add).
- `main.py`: Interface interativa via terminal para execução dos algoritmos e medição de tempo de performance.
- `convolution/`: Diretório contendo sinais de exemplo (`xn.txt` e `hn.txt`) para testes de convolução.
- `entrada.txt` / `entrada2.txt`: Arquivos de exemplo para teste da FFT.

## 🛠️ Como Usar

### Pré-requisitos
- Python 3.x
- NumPy
- Pandas

### Execução
Para iniciar o programa interativo, execute:
```bash
python main.py
```

Ao iniciar, você verá as seguintes opções:
1. **FFT por decimação no tempo**: Solicitará um arquivo de entrada e calculará a transformada.
2. **FFT por decimação na frequência**: Solicitará um arquivo de entrada e calculará a transformada.
3. **Convolução Seccionada**: Realizará a convolução entre os arquivos localizados na pasta `convolution/`.
0. **Sair**: Encerra o programa.

### Formato dos Arquivos de Entrada
Os arquivos devem estar em formato de texto (`.txt`) com valores separados por espaços:
- **Real:** Uma coluna de valores.
- **Complexo:** Duas colunas (a primeira para a parte real, a segunda para a parte imaginária).

## 📊 Exemplo de Implementação (Internal)

O projeto utiliza a estrutura de *Butterfly* para o cálculo da FFT, garantindo uma complexidade de $O(N \log N)$ em comparação ao $O(N^2)$ da DFT convencional.

```python
# Exemplo de chamada interna para FFT
import fft as ft
import numpy as np

sinal = np.array([1, 1, 1, 1, 0, 0, 0, 0])
resultado = ft.t_fft(sinal)
print(resultado)
```

## ✒️ Autores
Desenvolvido como ferramenta de estudo para algoritmos de processamento de sinais.
