import socket

SERVER_IP = 'localhost'
SERVER_PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)

print('Servidor TCP rodando...')

while True:
    conn, addr = server_socket.accept()
    print('Conexão estabelecida!!!')

    while True:
        data = conn.recv(1024)
        if not data:
            break
        
        print('Mensagem recebida do cliente:', data.decode())

        result = ""

        for a in data.decode():
            if a.islower():
                result += a.upper()
            else:
                result += a.lower()

        conn.sendall(result.encode())
        print('Mensagem enviada para o cliente:', result)

    conn.close()
    print('Conexão encerrada!!!')

server_socket.close()