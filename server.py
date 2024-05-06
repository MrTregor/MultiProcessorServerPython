import socket
import multiprocessing


def handle_client(client_socket):
    # Получаем сообщение от клиента
    message = client_socket.recv(1024)
    print(f"Received message from client: {message.decode()}")

    # Отправляем ответ клиенту
    client_socket.sendall(b"Hello from server!")

    # Закрываем соединение
    client_socket.close()


def start_server():
    # Создаем серверный сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(5)

    print("Server started. Waiting for connections...")

    while True:
        # Accept incoming connections
        client_socket, address = server_socket.accept()
        print(f"Connected by {address}")

        # Создаем новый процесс для обслуживания клиента
        process = multiprocessing.Process(target=handle_client, args=(client_socket,))
        process.start()


if __name__ == "__main__":
    start_server()
