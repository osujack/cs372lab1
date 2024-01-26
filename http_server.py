#       Author: Jackson Lee
#         Date: 01/26/2023
#       Course: CS 372 Winter 2024
#      Project: 1
#      Program: Sockets and HTTP
#  Description: Create a tiny browser and web-server using python sockets.

import socket  # import socket.py module to use the python socket API.
import random  # import random.py module to use the randomized integers as port number.

def create_http_server():
    # Server information
    host = "127.0.0.1"  # Local host loopback address
    """ port = random.randint(1024, 65535)  # Test Random port greater than 1023 """
    port = 8472         # Random port number greater than 1023

    # Create a listening socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one incoming connection

    print(f"Server listening on http://{host}:{port}/") # Display port number being used

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
                response = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"\
                           "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
                client_socket.sendall(response.encode())
                print(response)

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

# Citation for the following Constants: socket.AF_INET, socket.SOCK_STREAM
# Citation for the following Socket Objects: socket.bind, socket.listen
# Date: 01/25/2024
# Based on: Constants and Objects definition and examples for
#           socket.AF_INET, socket.SOCK_STREAM, socket.bind, socket.listen
# Source URL: https://docs.python.org/3/library/socket.html

# Citation for the following python built-in exceptions: KeyboardInterrupt
# Date: 01/25/2024
# Based on: exception definition and use case for KeyboardInterrupt
# Source URL: https://docs.python.org/3/library/exceptions.html
#