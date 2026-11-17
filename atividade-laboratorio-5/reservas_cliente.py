import rpyc

HOST = "localhost"
PORTA = 18812

def exibir_mapa_assentos(conexao):
    """Obtém e apresenta no ecrã o mapa atualizado dos assentos."""
    mapa = dict(conexao.root.listar_assentos())
    print("\n--- MAPA DE ASSENTOS ---")
    for assento, estado in mapa.items():
        marcador = "[ ]" if estado == "Livre" else "[X]"
        print(f"  {marcador} {assento:<3} -> {estado}")
    print("------------------------")

def iniciar_cliente():
    try:
        conexao = rpyc.connect(HOST, PORTA)
    except ConnectionRefusedError:
        print("[ERRO] Não foi possível ligar ao servidor RPyC. Verifique se está em execução.")
        return

    nome_cliente = input("Introduza o seu nome: ").strip() or "Utilizador"
    print(f"\nBem-vindo(a), {nome_cliente}!")

    try:
        while True:
            exibir_mapa_assentos(conexao)
            escolha = input("Indique o assento a reservar (ex: A1) ou 'sair' para terminar: ").strip()

            if escolha.lower() in ("sair", "0", "exit"):
                print("[INFO] A encerrar a ligação com o servidor...")
                break

            if not escolha:
                continue

            sucesso, mensagem = conexao.root.reservar_assento(nome_cliente, escolha)
            if sucesso:
                print(f"[SUCESSO] {mensagem}")
            else:
                print(f"[AVISO] {mensagem}")

    except (KeyboardInterrupt, EOFError):
        print("\n[INFO] Sessão interrompida pelo utilizador.")
    finally:
        conexao.close()
        print("[CLIENTE] Ligação encerrada.")

if __name__ == "__main__":
    iniciar_cliente()