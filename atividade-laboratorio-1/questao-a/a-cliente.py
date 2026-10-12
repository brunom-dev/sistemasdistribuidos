import socket

def iniciar_cliente():
    host = '127.0.0.1'
    porta = 7000
    
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))

    horario = cliente.recv(1024).decode('utf-8')
    print(f"[RESPOSTA DO SERVIDOR] O horário atual é: {horario}")
    
    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()