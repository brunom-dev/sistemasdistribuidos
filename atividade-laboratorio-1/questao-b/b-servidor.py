import socket

def iniciar_servidor():
    host = '127.0.0.1'
    porta = 8000
    
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    
    print(f"[ESCUTANDO] Servidor de Reversão escutando na porta {porta}...")

    while True:
        conexao, endereco = servidor.accept()
        print(f"[NOVA CONEXÃO] Cliente conectado: {endereco}")
        
        mensagem_recebida = conexao.recv(1024).decode('utf-8')
        
        if mensagem_recebida:
            print(f"[MENSAGEM RECEBIDA] {mensagem_recebida}")
            
            mensagem_revertida = mensagem_recebida[::-1]
            print(f"[MENSAGEM REVERTIDA] {mensagem_revertida}")
            
            conexao.send(mensagem_revertida.encode('utf-8'))
            
        conexao.close()
        print(f"[DESCONECTADO] Cliente {endereco} finalizado.\n")

if __name__ == "__main__":
    iniciar_servidor()