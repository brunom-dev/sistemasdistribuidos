import socket
import threading
from datetime import datetime
import time

def lidar_com_cliente(conexao, endereco):
    print(f"[NOVA CONEXÃO] Cliente conectado: {endereco}")

    time.sleep(3)

    horario_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conexao.send(horario_atual.encode('utf-8'))
    
    conexao.close()
    print(f"[DESCONECTADO] Cliente {endereco} desconectado.")

def iniciar_servidor():
    host = '127.0.0.1'
    porta = 7000
    
    #socket IPv4 (AF_INET) e TCP (SOCK_STREAM)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    
    print(f"[ESCUTANDO] Servidor de Horário escutando na porta {porta}...")

    while True:
        conexao, endereco = servidor.accept()
        
        thread = threading.Thread(target=lidar_com_cliente, args=(conexao, endereco))
        thread.start()
        print(f"[THREADS ATIVAS] {threading.active_count() - 1}")

if __name__ == "__main__":
    iniciar_servidor()