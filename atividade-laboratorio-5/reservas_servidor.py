import threading
import rpyc
from rpyc.utils.server import ThreadedServer

class ServicoReservas(rpyc.Service):
    """
    Serviço RPyC com estado partilhado em memória para gestão de reservas
    e controlo de concorrência através de exclusão mútua (Lock).
    """

    def __init__(self):
        self.assentos = {f"A{i}": None for i in range(1, 11)}
        self.lock = threading.Lock()

    def on_connect(self, conn):
        print("[CONEXÃO] Novo cliente ligado ao servidor de reservas.")

    def on_disconnect(self, conn):
        print("[DESCONEXÃO] Cliente desligado.")

    def exposed_listar_assentos(self):
        """Retorna o estado atual de cada assento (Livre / Reservado)."""
        with self.lock:
            mapa = tuple(
                (assento, "Livre" if ocupante is None else "Reservado")
                for assento, ocupante in self.assentos.items()
            )
        return mapa

    def exposed_reservar_assento(self, nome_cliente, assento):
        """Tenta reservar o assento indicado de forma atómica."""
        assento_id = assento.strip().upper()
        cliente_nome = nome_cliente.strip()

        with self.lock:
            if assento_id not in self.assentos:
                return (False, f"Assento '{assento_id}' inexistente. Escolha entre A1 e A10.")

            if self.assentos[assento_id] is not None:
                print(f"[CONFLITO] {cliente_nome} tentou reservar {assento_id}, mas já está ocupado.")
                return (False, "Assento já ocupado")

            # Efetua a reserva no estado partilhado
            self.assentos[assento_id] = cliente_nome
            print(f"[RESERVA] Assento {assento_id} reservado com sucesso para '{cliente_nome}'.")
            return (True, f"Reserva confirmada: assento {assento_id} atribuído a {cliente_nome}.")

def iniciar_servidor():
    porta = 18812
    servico_partilhado = ServicoReservas()
    servidor = ThreadedServer(
        servico_partilhado,
        port=porta,
        protocol_config={"allow_public_attrs": True}
    )
    print(f"[SERVIDOR RPyC] Sistema de Reserva de Assentos ativo na porta {porta}...")
    servidor.start()

if __name__ == "__main__":
    iniciar_servidor()