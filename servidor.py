# server.py
import socket
import threading
from vectorClock import VectorClock

class Server:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.vector_clock = VectorClock(['server'])


    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024).decode('ascii')
                self.vector_clock.increment('server')
                print(f"{message}")
                print(f"(vector clock: {self.vector_clock})")
                self.broadcast(message.encode('ascii'), client)
            except:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                break

    def broadcast(self, message, client):
        for c in clients:
            if c != client:
                c.send(message)

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")
            clients.append(client)
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

if __name__ == "__main__":
    clients = []
    server = Server()
    server.receive()
