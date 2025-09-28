# ⛽ Analisador de Custo de Combustível v2 (Streamlit App)

> **Status do Projeto:** ✔️ Funcional (utilizando dados simulados)

## 📄 Descrição

Este projeto é a segunda etapa de um roadmap de aprendizado em Python, evoluindo de um simples script de console para uma aplicação web interativa construída com o framework Streamlit. A aplicação tem como objetivo ajudar um motorista a determinar qual posto de gasolina é a opção mais econômica, levando em conta não apenas o preço do combustível, mas também a distância e o custo de deslocamento até cada local.

A interface gráfica permite uma experiência de usuário mais rica, utilizando a geolocalização do navegador para simular uma busca por postos próximos e apresentando os resultados de forma clara e organizada.

## ✨ Agradecimentos

Este projeto foi desenvolvido como um exercício de aprendizado guiado, contando com a assistência da Inteligência Artificial Gemini do Google (atuando como "Parceiro de Programação"). A IA foi fundamental no fornecimento de diretrizes sobre a estrutura do código, depuração de erros, melhores práticas de desenvolvimento (como o gerenciamento de estado no Streamlit) e na elaboração de estratégias para contornar desafios, como a simulação de dados de API.

## 🚀 Funcionalidades Principais

-   **Interface Gráfica Interativa:** Desenvolvida com Streamlit para uma experiência de usuário limpa e moderna.
-   **Geolocalização do Navegador:** Captura as coordenadas de latitude e longitude do usuário para servir como ponto de partida para as buscas.
-   **Busca de Postos (Simulada):** Utiliza uma lista de dados fixa (*mock data*) para simular a resposta de uma API, permitindo que a aplicação seja totalmente funcional sem uma chave de API real.
-   **Entrada de Dados Dinâmica:** Permite ao usuário inserir o preço do combustível para cada posto encontrado.
-   **Cálculo de Distância:** Implementa a fórmula de Haversine para calcular a distância geodésica entre o usuário e cada posto.
-   **Análise de Custo Completa:** Calcula o custo total, incluindo o deslocamento (ida e volta) e o valor do abastecimento.
-   **Exibição Clara do Resultado:** Apresenta a melhor opção de forma destacada e oferece uma tabela comparativa com todos os postos analisados.

---

## 🛠️ Como Executar o Projeto

Siga os passos abaixo para executar a aplicação em sua máquina local.

### Pré-requisitos

-   [Python 3.8+](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/) (para clonar o repositório)

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/AlerandroPesanha/projeto-combustivel.git](https://github.com/AlerandroPesanha/projeto-combustivel.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd projeto-combustivel
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no Mac/Linux
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Execução

Com o ambiente virtual ativo, execute o seguinte comando no terminal:

```bash
streamlit run main.py
```
---

## 💻 Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

O projeto foi desenvolvido inteiramente com bibliotecas e freameworks do Python 3, necessitando de instalação de pacotes externos.

---

## 📝 Limitações

Este é um projeto de estudo e possui um escopo simplificado. As seguintes variáveis não são consideradas nos cálculos:

-   Condições de trânsito em tempo real.
-   Custos adicionais como pedágios.
-   Variações no consumo do veículo (ex: trânsito urbano vs. estrada).

---

## 👨‍💻 Autor

Feito por **Altamiro Vianna**.

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/seu-usuario)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/altamiro-vianna/)