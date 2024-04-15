# client.py
import socket
import threading
from vectorClock import VectorClock

class Client:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.nickname = input("Choose a nickname: ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.vector_clock = VectorClock([self.nickname])

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print("An error occured!")
                self.client.close()
                break

    def write(self):
        while True:
            message = f'{self.nickname}: {input("Type your message (close connection to exit the chat): ")}'
            if 'close connection' in message: 
                self.client.close()
                break
            else:
                self.vector_clock.increment(self.nickname)
                self.client.send(f"{message} (vector clock: {self.vector_clock})".encode('ascii'))

    def run(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

if __name__ == "__main__":
    client = Client()
    client.run()
