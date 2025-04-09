#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter03/tcp_sixteen.py
# Simple TCP client and server that receive data in chunks, each with a maximum size of 16 bytes.

import argparse
import socket

def server(interface, port):
    """
    Listens on a given interface and a port, and receives a client message.
    Then sends the message back to the client.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow quick reuse of the port for fast restarts
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1) # The socket can now be used only to receive incoming connections
    print(f"Listening on {sock.getsockname()} ...")
    try:
        while True:
            print('Waiting to accept a new connection ...')
            client_sock, client_addr = sock.accept() # An entirely new socket for new conversation
            print(f"Accepted connection from {client_addr}")
            print(f"  Socket name: {client_sock.getsockname()}")
            print(f"  Socket peer: {client_sock.getpeername()}")
            try:
                while True:
                    data = client_sock.recv(16)
                    print(f"  Received: {data!r}")
                    if data:
                        print("  Sending data back to the client")
                        client_sock.sendall(data)
                    else:
                        print(f"  No more data from {client_addr}")
                        break
            finally:
                client_sock.close()
    except KeyboardInterrupt:
        print("\nServer shutting down gracefully.")
    finally:
        print("Closing socket")
        sock.close()

def client(host, port):
    """
    Connects to the server at a given host and port.
    Then sends and reads a message from/to a server.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f"Client has been assigned socket name: {sock.getsockname()}")
    try:
        # Send data
        message = b"This is a greeting from the client"
        sock.sendall(message)
        # Look for the response
        response = b""
        amount_expected = len(message)
        while len(response) < amount_expected:
            data = sock.recv(16)
            response += data
            print(f"Received: {data!r}")
        print(f"The server replied: {response!r}")
    finally:
        print("Closing socket")
        sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1080,
                        help='TCP port (default 1080)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
