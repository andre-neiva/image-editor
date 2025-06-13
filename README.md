# Editor de Imagens - Projeto SIN392

Este é um editor de imagens desenvolvido como parte do projeto da disciplina **SIN392 – Processamento Digital de Imagens**, com o objetivo de aplicar operações fundamentais de processamento espacial e frequência em imagens digitais, utilizando a linguagem Python com a biblioteca PyQt5 para a interface gráfica.

O sistema permite o carregamento de imagens, aplicação de diversos filtros e transformações, e visualização de resultados em tempo real.

## Tecnologias utilizadas
- Python 3.10+
- PyQt5
- OpenCV
- NumPy
- Matplotlib
- SciPy

## Funcionalidades implementadas

#### 📂 Gerenciamento de Arquivos
- Carregar imagem RGB ou tons de cinza
- Conversão automática para tons de cinza
- Salvar imagem processada
- Reverter imagem para o estado original

#### ⚙️ Processamento Espacial
- Alargamento de contraste
- Equalização de histograma
- Cálculo e exibição de histograma

#### 🧹 Filtros Passa-Baixa (manuais)
- Média
- Mediana
- Gaussiano
- Mínimo
- Máximo

#### 🔍 Filtros Passa-Alta
- Sobel
- Prewitt
- Roberts
- Laplaciano

#### 🧬 Morfologia Matemática
- Erosão
- Dilatação

#### 📉 Segmentação
- Limiarização automática com Otsu

#### ⚡ Domínio da Frequência
- Transformada de Fourier
- Visualização do espectro de magnitude


## Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sin392-image-editor.git
   cd sin392-image-editor

2. Crie e ative o ambiente virtual:
     ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Linux/macOS

3. Instale as dependências
    ```bash
    pip install -r requirements.txt

4. Execute a aplicação
    ```bash
    python main.py



Projeto desenvolvido por André Paz da Silva Neiva, sob orientação da disciplina SIN392 – Processamento de Imagens, Universidade Federal de Viçosa.
