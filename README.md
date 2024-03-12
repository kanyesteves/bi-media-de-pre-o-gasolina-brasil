# Analise dos preços dos combustíveis no brasil

Este guia fornece instruções passo a passo para configurar e executar seu projeto pessoal em uma máquina Linux.


## Pré-requisitos

1. **Sistema Operacional Linux:** Este guia pressupõe que você está usando uma distribuição Linux.

2. **Python 3:** Certifique-se de ter o Python 3 instalado. Se não estiver instalado, você pode instalá-lo usando o seguinte comando:

        sudo apt-get update
        sudo apt-get install python3

## Configurando o Ambiente Virtual

1. **Crie um Ambiente Virtual e ative**:
    Vá para o diretório do seu projeto, crie um ambiente virtual e ative-o.

        cd caminho/do/seu-projeto
        python3 -m venv venv
        source venv/bin/activate

## Instalação das Dependências

1. **Rode o comando para instalar as dependências:**

        pip install -r requirements.txt

## Execute o projeto

1. **Rodar o BI:**

        cd src/
        streamlit run bi.py

1. **Acessar o ETL:**

        jupyter lab
