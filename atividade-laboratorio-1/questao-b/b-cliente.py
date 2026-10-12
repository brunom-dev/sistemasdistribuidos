import socket

def iniciar_cliente():
    host = '127.0.0.1'
    porta = 8000
    
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))


    mensagem = "Olá, Mundo Distribuído"
    print(f"[ENVIANDO] {mensagem}")
    
    cliente.send(mensagem.encode('utf-8'))

    resposta = cliente.recv(1024).decode('utf-8')
    print(f"[RESPOSTA DO SERVIDOR] {resposta}")

    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()