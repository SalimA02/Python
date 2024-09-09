import socket
import threading

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def receive_messages(self):
        try:
            while True:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"Server responded: {message}")
        except socket.error:
            print("Connection lost.")
            self.client_socket.close()

    def send_messages(self):
        try:
            while True:
                message = input()
                if message.lower() == "quit":
                    self.client_socket.sendall("".encode())
                    break
                self.client_socket.sendall(message.encode())
        except socket.error:
            print("Connection lost.")
            self.client_socket.close()

    def start(self):
        print("Connected to the server. You can now start chatting.")
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send_messages)
        send_thread.start()

if __name__ == "__main__":
    client = ChatClient('127.0.0.1', 12345)
    client.start()