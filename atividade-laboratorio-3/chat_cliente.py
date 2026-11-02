import socket
import threading
import sys

HOST = '127.0.0.1'
PORTA = 9000

def receber_mensagens(sock):
    """Thread dedicada à escuta e apresentação das mensagens recebidas."""
    while True:
        try:
            mensagem = sock.recv(1024).decode('utf-8')
            if not mensagem:
                print("\n[INFO] Ligação com o servidor encerrada.")
                break
            print(f"\r{mensagem}")
            print("> ", end="", flush=True)
        except Exception:
            print("\n[ERRO] Ocorreu uma falha na ligação com o servidor.")
            break
    sock.close()
    sys.exit()

def iniciar_cliente():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORTA))
    except ConnectionRefusedError:
        print("[ERRO] Não foi possível ligar ao servidor. Certifique-se de que o servidor está ativo.")
        return

    nome = input("Introduza o seu nome de utilizador: ").strip()
    sock.send(nome.encode('utf-8'))
    print(f"[CONECTADO] Bem-vindo ao chat, {nome}! Digite as suas mensagens abaixo (ou '/sair'):\n")

    # Inicia a thread responsável por escutar as mensagens dos outros clientes
    thread_rececao = threading.Thread(target=receber_mensagens, args=(sock,), daemon=True)
    thread_rececao.start()

    # Thread principal encarregada de ler a entrada do utilizador
    while True:
        try:
            mensagem = input("> ")
            if mensagem.strip().lower() == "/sair":
                print("[INFO] A terminar a sessão...")
                sock.close()
                break
            if mensagem.strip():
                sock.send(mensagem.encode('utf-8'))
        except (KeyboardInterrupt, EOFError):
            print("\n[INFO] Sessão interrompida.")
            sock.close()
            break

if __name__ == "__main__":
    iniciar_cliente()