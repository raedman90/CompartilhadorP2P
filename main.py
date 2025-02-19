import threading
from server.server import start_server
from client.client import start_client

def main():
    mode = input("Digite 'servidor' para rodar como servidor ou 'cliente' para rodar como cliente: ")
    if mode == "servidor":
        start_server()
    elif mode == "cliente":
        server_ip = input("Digite o IP do servidor: ")
        threading.Thread(target=start_client).start()

if __name__ == "__main__":
    main()