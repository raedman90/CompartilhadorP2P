import socket
import os
from client.config import SERVER_IP, PORT

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))
    
    ip_address = socket.gethostbyname(socket.gethostname())
    client.sendall(f'JOIN {ip_address}\n'.encode())

    response = client.recv(1024).decode().strip()
    print("[Servidor]:", response)

    if response != "CONFIRMJOIN":
        print("[ERRO] O servidor não confirmou a conexão.")
        client.close()
        return

    public_dir = "./public"
    if not os.path.exists(public_dir):
        os.makedirs(public_dir)

    for file in os.listdir(public_dir):
        file_path = os.path.join(public_dir, file)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            create_file_msg = f'CREATEFILE {file} {size}\n'
            client.sendall(create_file_msg.encode())
            response = client.recv(1024).decode().strip()
            print("[Servidor]:", response)

    while True:
        cmd = input("\nDigite um comando: ")
        
        client.sendall(f'{cmd}\n'.encode())

        if cmd.startswith("CREATEFILE"):
            response = client.recv(1024).decode().strip()
            print("[Servidor]:", response)
            continue 

        if cmd.startswith("SEARCH"):
            print("[Cliente] Buscando arquivos...")
            while True:
                response = client.recv(1024).decode().strip()
                if response == "NORESULT":
                    print("Nenhum arquivo encontrado.")
                    break
                elif response == "ENDSEARCH":
                    print("[Cliente] Busca concluída.")
                    break
                elif response.startswith("FILE"):
                    print("[Servidor]:", response)
            continue

        response = client.recv(1024).decode().strip()
        print("[Servidor]:", response)

        if cmd.startswith("LEAVE"):
            break

    client.close()
