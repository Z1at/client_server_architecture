# Import socket module
import socket
import threading


# local host IP '127.0.0.1'
host = '127.0.0.1'

# Define the port on which you want to connect
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server on local computer
s.connect((host, port))


name = input("enter your name: ")
print("You have entered the chat")


def send():
    while True:
        msg = input()
        s.send((name + " " + msg).encode('utf-8'))


def receive():
    while True:
        data = s.recv(1024)

        # print the received message
        # here it would be a reverse of sent message
        print(str(data.decode('utf-8')))


def main():
    snd = threading.Thread(target=send).start()
    rcv = threading.Thread(target=receive).start()


if __name__ == '__main__':
    main()
