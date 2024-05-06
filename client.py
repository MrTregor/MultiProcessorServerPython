import socket


def start_client():
    # Создаем клиентский сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 8080))

    # Отправляем сообщение серверу
    message = "Hello from client!".encode()
    client_socket.sendall(message)

    # Получаем ответ от сервера
    response = client_socket.recv(1024)
    print(f"Received response from server: {response.decode()}")

    # Закрываем соединение
    client_socket.close()


if __name__ == "__main__":
    start_client()
