#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_local.py
# UDP client and server on localhost

import argparse
import socket
from datetime import datetime

MAX_BYTES = 65535 # Maximum size for UDP datagram (less overhead)

def server(port):
    """
    Runs a UDP server on the specified port.
    Receives messages and replies with their size.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Allow quick reuse of the port for fast restarts
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', port)) # restrict to the loopback interface
    print(f"Listening at {sock.getsockname()}...")
    try:
        while True:
            data, address = sock.recvfrom(MAX_BYTES)
            text = data.decode('utf-8', errors='replace')
            print(f"The client at {address} says {text!r}")
            text = f"Your data was {len(data)} bytes long"
            sock.sendto(text.encode('utf-8'), address)
    except KeyboardInterrupt:
        print("\nServer shutting down gracefully.")
    finally:
        print("Closing socket")
        sock.close()

def client(port):
    """
    Runs a UDP client that sends a message to the server.
    Receives a reply and prints it.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = f"The time is {datetime.now()}"
    data = text.encode('utf-8')
    try:
        sock.sendto(data, ('127.0.0.1', port))
        print(f"The OS assigned me the address {sock.getsockname()}")
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('utf-8')
        print(f"The server {address} replied {text!r}")
    finally:
        print("Closing socket")
        sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1080,
                        help='UDP port (default 1080)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
