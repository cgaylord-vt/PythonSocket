# An example program for TCP socket programming
# This is an "echo" client -- send a message, receive a message

import socket

# Connect the socket to the port where the server is listening
server_address = ('localhost', 55542)
print('connecting to {} port {}'.format(*server_address))
# Create a TCP/IP socket
#sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
#sock.connect(server_address)
# socket.create_connection is a convenience function that does
# what socket.socket + socket.connect do.
sock = socket.create_connection(server_address)

try:
    # Send data
    message = b'This is our message. It is very long but will only be transmitted in chunks of 16 at a time'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
