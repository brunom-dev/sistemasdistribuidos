import socket
import threading
import time

HOST = '127.0.0.1'
PORTA = 10000
TIMEOUT_SEGUNDOS = 8.0
INTERVALO_CHECAGEM = 1.0

# Estruturas partilhadas para rastrear o último sinal e o estado de cada nó
ultimos_sinais = {}
estado_workers = {}
lock = threading.Lock()

def checar_workers():
    """Thread periódica que verifica se algum Worker excedeu o tempo limite de 8s."""
    while True:
        time.sleep(INTERVALO_CHECAGEM)
        agora = time.time()

        with lock:
            for worker_id, ultimo_instante in list(ultimos_sinais.items()):
                tempo_inativo = agora - ultimo_instante

                if tempo_inativo > TIMEOUT_SEGUNDOS and estado_workers.get(worker_id) == "ONLINE":
                    estado_workers[worker_id] = "OFFLINE"
                    print(f"[ALERTA] O Nó {worker_id} está OFFLINE!")

def iniciar_monitor():
    # Socket UDP (Heartbeat)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((HOST, PORTA))

    print(f"[SERVIDOR MONITOR] Escutando sinais de Heartbeat em {HOST}:{PORTA}...")

    # Inicia a thread de verificação periódica em segundo plano
    thread_verificacao = threading.Thread(target=checar_workers, daemon=True)
    thread_verificacao.start()

    while True:
        try:
            dados, endereco = servidor.recvfrom(1024)
            mensagem = dados.decode('utf-8').strip()

            if mensagem.startswith("PING"):
                # Extrai o ID do nó
                worker_id = mensagem.replace("PING", "", 1).strip()
                if not worker_id:
                    worker_id = f"{endereco[0]}:{endereco[1]}"

                with lock:
                    ultimos_sinais[worker_id] = time.time()

                    if estado_workers.get(worker_id) != "ONLINE":
                        estado_workers[worker_id] = "ONLINE"
                        print(f"[CONECTADO] O Nó {worker_id} está ONLINE ({endereco[0]}:{endereco[1]}).")
                    else:
                        print(f"[HEARTBEAT] Sinal recebido de {worker_id}")

        except Exception as erro:
            print(f"[ERRO] Falha ao processar pacote: {erro}")

if __name__ == "__main__":
    iniciar_monitor()