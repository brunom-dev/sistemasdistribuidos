# Atividade Laboratório IV - Monitor de Heartbeat

Implementação de um mecanismo de deteção de falhas baseado em **Heartbeat** utilizando **sockets UDP** e **threads** em Python.

## Funcionamento
- **Worker (`heartbeat_worker.py`):** Envia sinais periódicos (`PING <ID>`) a cada **3 segundos** para o servidor.
- **Servidor Monitor (`heartbeat_monitor.py`):** Regista o último instante de comunicação de cada nó e verifica continuamente se algum nó ultrapassou **8 segundos** sem enviar sinais, emitindo um alerta de nó *OFFLINE*.

## Como Executar e Testar

1. **Inicie o Servidor Monitor** no primeiro terminal:
   ```bash
   python heartbeat_monitor.py