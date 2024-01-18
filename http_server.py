#       Author: Jackson Lee
#         Date: 01/17/2023
#       Course: CS 372 Winter 2024
#      Project: 1
#      Program: Sockets and HTTP
#  Description: Create a tiny browser and web-server using python sockets.
#

import socket
import random

def create_http_server():
    # Server information
    host = "127.0.0.1"
    port = random.randint(1024, 65535)  # Random port greater than 1023

    # Create a listening socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one incoming connection

    print(f"Server listening on http://{host}:{port}/")

    try:
        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")

            try:
                # Read the request from the client
                request = client_socket.recv(1024).decode()
                print("Received Request:")
                print(request)

                # Send the HTML response
                response = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<html>completed</html>\r\n"
                client_socket.sendall(response.encode())

            finally:
                # Close the client socket
                client_socket.close()

    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        # Close the listening socket
        server_socket.close()

if __name__ == "__main__":
    create_http_server()