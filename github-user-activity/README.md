# Github User Activity

Um script simples que utiliza a API oficial do GitHub para imprimir a atividade recente de um usuário.

Apenas alguns dos eventos foram codificados, em casos que o usuário teve um evento "novo", o retorno será um **GenericEvent**, especificando o evento desconhecido.

## Como executar

### Pré-requisitos
- Python 3.12 ou superior instalado

### Instalação e execução

1. Clone o repositório:
   ```sh
   git clone https://github.com/olucaxx/roadmap.sh-backend
   cd roadmap.sh-backend/github-user-activity
    ```
2. (Opcional) Crie um ambiente virtual:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate     # Windows
    ```
3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
4. Instale o pacote:
    ```sh
    pip install .
    ```
5. Execute com:
    ```sh
    github-activity <username> 
    ```
    Para uma descrição mais detalhada, use `github-activity -h`
