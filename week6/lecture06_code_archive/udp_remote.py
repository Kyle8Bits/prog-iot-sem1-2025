#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_remote.py
# UDP client and server for talking over the network

import argparse
import random
import socket

MAX_BYTES = 65535 # Maximum size for UDP datagram (less overhead)

def server(interface, port):
    """
    Runs a UDP server that listens on the given interface and port.
    This server simulates packet loss by randomly dropping incoming datagrams.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Allow quick reuse of the port for fast restarts
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    print(f"Listening at {sock.getsockname()}...")
    try:
        while True:
            data, address = sock.recvfrom(MAX_BYTES)
            # Simulate packet loss
            if random.random() < 0.5:
                print(f"Pretending to drop packet from {address}")
                continue
            text = data.decode('utf-8', errors='replace')
            print(f"The client at {address} says {text!r}")
            message = f"Your data was {len(data)} bytes long"
            sock.sendto(message.encode('utf-8'), address)
    except KeyboardInterrupt:
        print("\nServer shutting down gracefully.")
    finally:
        print("Closing socket")
        sock.close()

def client(hostname, port):
    """
    Runs a UDP client that sends a message to the server and waits for a reply.
    Uses an exponential backoff strategy when waiting for a response.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((hostname, port))
    print(f"Client socket name is {sock.getsockname()}")

    delay = 0.1  # seconds
    text = "This is another message"
    data = text.encode('utf-8')
    while True:
        sock.send(data)
        print(f"Waiting up to {delay:.1f} seconds for a reply")
        sock.settimeout(delay)
        try:
            response = sock.recv(MAX_BYTES)
            break  # Reply received; exit loop.
        except socket.timeout as exc:
            delay *= 2  # Exponential backoff; wait even longer for the next request
            print("Timeout; increasing delay and retrying...")
            if delay > 2.0:
                raise RuntimeError("I think the server is down") from exc

    print(f"The server says {response.decode('utf-8')!r}")


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP,'
                                     ' pretending packets are often dropped')
    parser.add_argument('role', choices=choices, help='which role to take')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1080,
                        help='UDP port (default 1080)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
