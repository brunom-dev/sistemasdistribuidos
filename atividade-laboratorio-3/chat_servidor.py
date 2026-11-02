import socket
import threading

HOST = '127.0.0.1'
PORTA = 9000

clientes = []
nomes = {}
lock = threading.Lock()

def broadcast(mensagem, remetente=None):
    """Envia uma mensagem para todos os clientes, exceto opcionalmente o remetente."""
    with lock:
        for cliente in clientes:
            if cliente != remetente:
                try:
                    cliente.send(mensagem)
                except Exception:
                    # Falha de envio; remoção tratada na thread do respetivo cliente
                    pass

def gerir_cliente(conexao, endereco):
    """Gerência a receção contínua de mensagens de um cliente específico."""
    nome_cliente = ""
    try:
        # Recebe o nome/apelido inicial do utilizador
        nome_cliente = conexao.recv(1024).decode('utf-8').strip()
        with lock:
            clientes.append(conexao)
            nomes[conexao] = nome_cliente

        mensagem_entrada = f"\n[SISTEMA] {nome_cliente} entrou no chat!\n".encode('utf-8')
        print(f"[NOVA LIGAÇÃO] {nome_cliente} ligado a partir de {endereco}")
        broadcast(mensagem_entrada, remetente=conexao)

        # Ciclo de receção de mensagens do cliente
        while True:
            dados = conexao.recv(1024)
            if not dados:
                break
            
            mensagem_formatada = f"[{nome_cliente}]: {dados.decode('utf-8')}".encode('utf-8')
            broadcast(mensagem_formatada, remetente=conexao)

    except (ConnectionResetError, ConnectionAbortedError):
        pass
    finally:
        # Limpeza e remoção do cliente desconectado
        with lock:
            if conexao in clientes:
                clientes.remove(conexao)
            if conexao in nomes:
                del nomes[conexao]
        
        conexao.close()
        mensagem_saida = f"\n[SISTEMA] {nome_cliente} saiu do chat.\n".encode('utf-8')
        print(f"[DESLIGADO] {nome_cliente} ({endereco}) desconectou-se.")
        broadcast(mensagem_saida)

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORTA))
    servidor.listen()
    print(f"[SERVIDOR ATIVO] Servidor de Chat a escutar na porta {PORTA}...")

    while True:
        conexao, endereco = servidor.accept()
        # Inicia uma thread para cada ligação aceite
        thread_cliente = threading.Thread(target=gerir_cliente, args=(conexao, endereco), daemon=True)
        thread_cliente.start()

if __name__ == "__main__":
    iniciar_servidor()