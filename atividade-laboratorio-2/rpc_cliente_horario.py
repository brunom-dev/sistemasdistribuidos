import rpyc

def iniciar_cliente():
    host = "localhost"
    porta = 18812

    print("[CLIENTE] A estabelecer ligação ao servidor RPC...")
    
    # Estabelece a ligação RPC com o servidor
    conexao = rpyc.connect(host, porta)

    # Invocação do procedimento remoto (RPC) através do objeto 'root'
    horario_servidor = conexao.root.obter_horario()
    print(f"[RESPOSTA RPC] Horário atual obtido do servidor: {horario_servidor}")

    # Encerra a ligação
    conexao.close()
    print("[CLIENTE] Ligação encerrada.")

if __name__ == "__main__":
    iniciar_cliente()