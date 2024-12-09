import socket

# Função do cliente
def cliente():
    host = '127.0.0.1'
    port = 12345

    # Configurar o cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            x = input("Digite o valor de x (ou 'sair' para encerrar): ")
            if x.lower() == 'sair':
                client_socket.send(b"sair")
                print("Cliente desconectado.")
                break
            y = input("Digite o valor de y: ")
            n = input("Digite o valor de n: ")

            # Enviar dados ao servidor
            client_socket.send(f"{x} {y} {n}".encode())
            resultado = client_socket.recv(1024).decode()  # Receber resultado do servidor
            print(f"Resultado: {resultado}")

    except KeyboardInterrupt:
        print("\nCliente encerrado manualmente.")
    finally:
        client_socket.close()

if __name__ == '__main__':
    cliente()
