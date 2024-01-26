#       Author: Jackson Lee
#         Date: 01/26/2023
#       Course: CS 372 Winter 2024
#      Project: 1
#      Program: Sockets and HTTP
#  Description: Create a simple python program that uses a socket to interact with a server.
#               Create a socket program to receive arbitrarily large file.

# import socket.py module to use the python socket API.
import socket

def interact_with_server():
    # Server information
    server_address = "gaia.cs.umass.edu"
    server_port = 80  # HTTP port

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_address, server_port))

        # Send a simple HTTP GET request
        request = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:{}\r\n\r\n".format(server_address)

        client_socket.sendall(request.encode())

        # Receive and print the server's response
        response = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data

        print("Server Response:")
        print(response.decode())

    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    interact_with_server()

# Citation for the following Constants: socket.AF_INET, socket.SOCK_STREAM
# Citation for the following Socket Objects: socket.connect, socket.sendall
# Date: 01/25/2024
# Based on: Constants and Objects definition and examples for
#           socket.AF_INET, socket.SOCK_STREAM, socket.connect, socket.sendall
# Source URL: https://docs.python.org/3/library/socket.html