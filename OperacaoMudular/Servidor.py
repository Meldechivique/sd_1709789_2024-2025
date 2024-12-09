import socket

# Função para calcular a operação modular
def calcular_modular(x, y, n):
    return (x * y) % n

# Função do servidor
def servidor():
    host = '127.0.0.1'
    port = 12345

    # Configurar o servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permitir reutilização da porta
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Servidor pronto para receber conexões...")

    try:
        # Aceitar conexão do cliente
        conn, addr = server_socket.accept()
        print(f"Conexão estabelecida com: {addr}")

        while True:
            data = conn.recv(1024).decode()  # Receber dados do cliente
            if not data or data.lower() == 'sair':  # Verificar se o cliente quer sair
                print("Cliente desconectou.")
                break

            # Processar os números recebidos
            try:
                x, y, n = map(int, data.split())
                resultado = calcular_modular(x, y, n)
                conn.send(str(resultado).encode())  # Enviar resultado ao cliente
                print(f"Recebido: x={x}, y={y}, n={n} | Resultado enviado: {resultado}")
            except ValueError:
                conn.send("Erro: Entrada inválida.".encode())  # Mensagem de erro

    except KeyboardInterrupt:
        print("\nServidor encerrado manualmente.")
    finally:
        conn.close()  # Fechar conexão
        server_socket.close()

if __name__ == '__main__':
    servidor()
