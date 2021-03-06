#echo_client

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print(f"connecting to {server_address[0]} port {server_address[1]}")
sock.connect(server_address)

try:
    message = input("Type your message:\n")
    print(f"sending {message}")
    sock.sendall(message.encode('utf-8'))

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        print(f"received {data}")

finally:
    print(f"closing socket")
    sock.close()

