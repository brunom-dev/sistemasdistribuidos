# Atividade Laboratório I - Sistemas Distribuídos

Repositório destinado à resolução da atividade de laboratório 1 da disciplina de Sistemas Distribuídos (Ciência da Computação).

## Tecnologias 

- Python 3.x
- Biblioteca nativa `socket` para comunicação de baixo nível (TCP/IP).
- Biblioteca nativa `threading` para concorrência no servidor.

## Como Executar

As atividades estão divididas em partes A e B. Para testar qualquer uma delas, é necessário iniciar o servidor primeiro e, em seguida, executar o cliente em um terminal separado.

### Letra A: Servidor Multithread de Horário

1. Abra um terminal e inicie o servidor:
    ```bash
    python a_servidor.py
    ```
2. Abra outro terminal e execute o cliente (você pode rodar o cliente múltiplas vezes simultaneamente para testar as threads):
    ```bash
    python a_cliente.py
    ```

### Letra B: Servidor de Reversão de String

1. Inicie o servidor:
    ```bash
    python b_servidor.py
    ```
2. Execute o cliente que enviará a mensagem "Olá, Mundo Distribuído":
    ```bash
    python a_cliente.py
    ```
