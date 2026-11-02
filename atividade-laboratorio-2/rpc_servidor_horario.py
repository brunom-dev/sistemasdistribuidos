import rpyc
from rpyc.utils.server import ThreadedServer
from datetime import datetime

class ServicoHorario(rpyc.Service):
    def on_connect(self, conn):
        print(f"[CONEXÃO] Cliente ligado com sucesso.")

    def on_disconnect(self, conn):
        print(f"[DESCONEXÃO] Cliente desligado.")

    def exposed_obter_horario(self):
        """Retorna o horário atual do sistema ao cliente."""
        horario_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[RPC] Procedimento 'obter_horario' executado: {horario_atual}")
        return horario_atual

def iniciar_servidor():
    porta = 18812  # Porta predefinida do RPyC
    servidor = ThreadedServer(ServicoHorario, port=porta)
    print(f"[SERVIDOR RPC] A escutar pedidos na porta {porta}...")
    servidor.start()

if __name__ == "__main__":
    iniciar_servidor()