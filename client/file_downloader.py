import socket

def download_file(ip, filename, offset_start=0):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 1235))
    client.sendall(f'GET {filename} {offset_start}\n'.encode())
    
    with open(f'downloads/{filename}', 'wb') as f:
        while True:
            data = client.recv(4096)
            if not data:
                break
            f.write(data)
    client.close()
    print(f"Download de {filename} concluído!")