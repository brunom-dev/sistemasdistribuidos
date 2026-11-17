import socket
import time
import sys

HOST = '127.0.0.1'
PORTA = 10000
INTERVALO_ENVIO = 3

def iniciar_worker(worker_id):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"[WORKER ATIVO] Nó '{worker_id}' enviando Heartbeat a cada {INTERVALO_ENVIO} segundos...")

    try:
        while True:
            mensagem = f"PING {worker_id}"
            cliente.sendto(mensagem.encode('utf-8'), (HOST, PORTA))
            print(f"[ENVIADO] {mensagem}")
            time.sleep(INTERVALO_ENVIO)
    except KeyboardInterrupt:
        print(f"\n[ENCERRADO] Nó '{worker_id}' finalizado (simulando falha por colapso).")
    finally:
        cliente.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id_no = sys.argv[1]
    else:
        id_no = input("Informe o ID deste Nó (ex: Worker_1): ").strip() or "Worker_1"

    iniciar_worker(id_no)