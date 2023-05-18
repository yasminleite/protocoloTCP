import socket

SERVER_IP = 'localhost'
SERVER_PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print('Conexão estabelecida com sucesso!')
except ConnectionRefusedError:
    print("O servidor não está aberto.")
    exit()

while True:
    message = input("Digite um texto: ")

    client_socket.sendall(message.encode())
    print(f'Mensagem enviada para o servidor: {message}')

    response = client_socket.recv(1024)
    print(f'Resposta recebida do servidor: {response.decode()}')

    c = input("Deseja continuar? (yes/no): ")

    if c.lower() != "yes":
        break

client_socket.close()