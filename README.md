# FFT & Processamento Digital de Sinais

Este projeto contém implementações em Python de algoritmos fundamentais de Processamento Digital de Sinais (DSP), permitindo calcular a Transformada Rápida de Fourier (FFT) e realizar Convoluções Lineares. Além do processamento, o projeto conta com ferramentas para visualização gráfica dos sinais.

## 🚀 Funcionalidades

- **FFT por Decimação no Tempo (DIT):** Algoritmo clássico de Cooley-Tukey com estagios de *bit-reversal*.
- **FFT por Decimação na Frequência (DIF):** Implementação alternativa da FFT onde o *bit-reversal* ocorre ao final.
- **Convolução Seccionada (Overlap-Add):** Método eficiente para convolução de sinais longos utilizando processamento em blocos no domínio da frequência.
- **Zero-Padding Automático:** Ajuste automático do tamanho dos sinais para potências de 2, otimizando o cálculo da FFT.
- **Visualização Gráfica:** Módulo dedicado (`graph.py`) para plotagem de sinais reais ou complexos (Magnitude e Fase).

## 📁 Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **`fft.py`**: Biblioteca central com as implementações dos algoritmos (DIT, DIF, IFFT, Overlap-Add).
- **`main.py`**: Interface interativa de linha de comando para execução dos algoritmos.
- **`graph.py`**: Script para geração de gráficos a partir dos resultados salvos.
- **`entradas/`**: Diretório destinado aos arquivos de entrada (sinais a serem processados).
- **`resultados/`**: Diretório onde os arquivos de saída (processados) são salvos automaticamente.
- **`convolution/`**: Contém arquivos de teste padrão (`xn.txt` e `hn.txt`) utilizados na opção de Convolução Seccionada.
- **`graficos/`**: Diretório reservado para salvar ou armazenar plotagens.

## 🛠️ Como Usar

### Pré-requisitos
Certifique-se de ter as seguintes bibliotecas instaladas:
- Python 3.x
- NumPy
- Pandas
- Matplotlib

É recomendado criar um ambiente virtual para instalar as dependências, porém como são usadas poucas bibliotecas, não é extremamente necessário. Seguem os comandos para utilizar os programas do projeto.

### Instalação:
```bash
pip install numpy pandas matplotlib
```

### 1. Executando o Processamento (`main.py`)
Para realizar os cálculos, execute:
```bash
python main.py
```
O menu interativo apresentará as opções:
1. **FFT por decimação no tempo**: Solicita o nome de um arquivo na pasta `entradas/`, processa e salva em `resultados/`.
2. **FFT por decimação na frequência**: Similar à opção 1, mas usando o algoritmo DIF.
3. **Convolução Seccionada**: Utiliza automaticamente os arquivos `convolution/xn.txt` (sinal) e `convolution/hn.txt` (filtro).

> **Nota:** Ao solicitar o arquivo de entrada, digite apenas o nome (ex: `sinal.txt`). Ele deve estar previamente salvo dentro da pasta `entradas/`.

### 2. Visualizando os Resultados (`graph.py`)
Para ver os gráficos dos sinais processados:
```bash
python graph.py
```
1. O script pedirá o nome do arquivo de resultado (que deve estar na pasta `resultados/`).
2. Selecione o tipo de visualização:
   - **1 - Sinal Real:** Plota a amplitude no tempo (ideal para áudio ou sinais brutos).
   - **2 - Sinal Complexo:** Gera dois gráficos: Magnitude e Fase (ideal para visualizar a saída da FFT).

## 📄 Formato dos Arquivos
Os arquivos de texto devem conter valores numéricos separados por espaços ou tabulações:
- **Sinal Real:** Apenas uma coluna de valores.
- **Sinal Complexo:** Duas colunas, sendo a primeira a parte Real e a segunda a Imaginária.

## ✒️ Autores
Desenvolvido como ferramenta de estudo e aplicação de algoritmos de Processamento Digital de Sinais.
