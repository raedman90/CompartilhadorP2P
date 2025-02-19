import socket
from server.file_manager import all_files

def handle_client(conn, addr):
    ip_address = addr[0]
    
    try:
        data = conn.recv(1024).decode().strip()
        command = data.split()

        if command[0] == "JOIN":
            print(f"[SERVIDOR] Cliente {command[1]} conectou.")
            conn.sendall(b'CONFIRMJOIN\n')
        else:
            print(f"[ERRO] Comando inesperado do cliente {ip_address}: {data}")
            conn.close()
            return

        while True:
            try:
                data = conn.recv(1024).decode().strip()
                if not data:
                    break
                command = data.split()

                if command[0] == "CREATEFILE":
                    filename = command[1]
                    size = int(command[2]) if len(command) > 2 else 0
                    if ip_address not in all_files:
                        all_files[ip_address] = []
                    all_files[ip_address].append({"filename": filename, "size": size})
                    print(f"[SERVIDOR] Arquivo registrado: {filename} de {ip_address} ({size} bytes)")
                    conn.sendall(f'CONFIRMCREATEFILE {filename}\n'.encode())

                elif command[0] == "DELETEFILE":
                    filename = command[1]
                    if ip_address in all_files:
                        all_files[ip_address] = [f for f in all_files[ip_address] if f["filename"] != filename]
                    conn.sendall(f'CONFIRMDELETEFILE {filename}\n'.encode())

                elif command[0] == "SEARCH":
                    pattern = command[1]
                    print(f"[SERVIDOR] Buscando arquivos com padrão: {pattern}")

                    result = []
                    for ip, files in all_files.items():
                        for file in files:
                            if pattern in file["filename"]:
                                result.append(f'FILE {file["filename"]} {ip} {file["size"]}\n')

                    if result:
                        conn.sendall("".join(result).encode())
                    else:
                        conn.sendall(b'NORESULT\n')

                    conn.sendall(b'ENDSEARCH\n')

                elif command[0] == "LEAVE":
                    if ip_address in all_files:
                        del all_files[ip_address]
                    conn.sendall(b'CONFIRMLEAVE\n')
                    break

            except Exception as e:
                print(f"Erro ao processar comando de {ip_address}: {e}")
                break

    except Exception as e:
        print(f"Erro ao processar conexão inicial de {ip_address}: {e}")

    print(f"[DESCONECTADO] Cliente {ip_address} saiu.")
    conn.close()
