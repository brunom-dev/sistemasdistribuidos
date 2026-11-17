# Atividade Laboratório SD - Sistema de Reserva de Assentos (Estado Partilhado)

Aplicação distribuída de reserva de assentos desenvolvida em Python com **RPyC**, explorando o conceito de **estado partilhado** em memória e **controlo de concorrência** através de exclusão mútua (`threading.Lock`).

## Funcionalidades
- **Estado Partilhado:** Gestão centralizada da disponibilidade dos assentos (`A1` a `A10`) na memória do servidor.
- **Controlo de Concorrência:** Garantia de atomicidade nas reservas simultâneas, evitando condições de corrida e devolvendo `"Assento já ocupado"` em caso de conflito.
- **Cliente Interativo:** Consulta contínua do mapa de assentos e envio de múltiplos pedidos de reserva.

## Como Executar

1. **Iniciar o Servidor RPyC:**
   ```bash
   python reservas_servidor.py