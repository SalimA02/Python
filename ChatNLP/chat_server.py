import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.clients = []
        self.responses = {
            "hello": "Hello! Welcome to the chat server.",
            "what is a server": "A server is a computer program that provides a service to another computer program over a network.",
            "what is a client": "A client is a computer program that requests a service from a server over a network."
        }
        self.running = True

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.sendall(message.encode())
            except socket.error:
                self.clients.remove(client)

    def handle_client(self, client_socket):
        try:
            while self.running:
                message = client_socket.recv(1024).decode().lower()
                if message == "terminate":
                    self.terminate()
                    break
                print(f"Received: {message}")
                response = self.get_response(message)
                print(f"Responding: {response}")
                client_socket.sendall(response.encode())
        except socket.error:
            self.clients.remove(client_socket)
            client_socket.close()

    def get_response(self, message):
        for keyword, response in self.responses.items():
            if keyword in message:
                return response
        return "I'm not sure I understand."

    def start(self):
        print(f"Server listening on {self.host}:{self.port}")

        while self.running:
            try:
                client_socket, address = self.server_socket.accept()
                print(f"Connection from {address}")
                self.clients.append(client_socket)

                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
            except KeyboardInterrupt:
                self.terminate()
            except socket.error:
                break

    def terminate(self):
        self.running = False
        for client in self.clients:
            try:
                client.sendall("Chat Terminated.".encode())
                client.close()
            except socket.error:
                pass
        self.server_socket.close()
        print("Server shut down.")

if __name__ == "__main__":
    server = ChatServer('127.0.0.1', 12345)
    server.start()