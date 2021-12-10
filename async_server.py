import asyncio
import socket
import os
import argparse


def parse_cli():
    arg = argparse.ArgumentParser()
    arg.add_argument('-ip', help='IP-address your host', type=str)
    arg.add_argument('-p', help='Select port on your host', type=int)
    arg_value = arg.parse_args()
    if arg_value.ip and arg_value.p:
        return arg_value.ip, arg_value.p
    else:
        return '127.0.0.1', 5000


class Server:
    """ This class creates a socket and binds it to the 5000 port on the local machine,
        initializes the list of client sockets, and starts event loop for async methods """
    def __init__(self):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.server_sock.setblocking(False)
        self.server_sock.bind(parse_cli())
        self.server_sock.listen(5)
        self.clients = []
        asyncio.run(self.accept_connection())

    async def accept_connection(self):
        """ The main coroutine that accepts connections from clients and
            runs a coroutine that handle client messages """
        while True:
            loop = asyncio.get_event_loop()
            client_sock, client_adrr = await loop.sock_accept(self.server_sock)
            self.clients.append(client_sock)
            print(f'Client {client_adrr} connected to server')
            loop.create_task(self.message_handler(client_sock))

    async def message_handler(self, sock):
        """ This coroutine accepts client data and sends it to all other client sockets """
        while True:
            loop = asyncio.get_event_loop()
            client_message = await loop.sock_recv(sock, 1024)
            for sokt in self.clients:
                if sokt is not sock:
                    await loop.sock_sendall(sokt, client_message)


if __name__ == '__main__':
    try:
        Server()
    except KeyboardInterrupt:
        os.abort()
