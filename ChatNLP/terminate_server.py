import socket

def terminate_server():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        message = "terminate"
        client_socket.sendall(message.encode())
    except socket.error:
        print("Connection lost.")

    client_socket.close()

if __name__ == "__main__":
    terminate_server()