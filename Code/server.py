# import socket programming library
import socket

# import thread module
from _thread import *
import threads

# print_lock = threads.Lock()

clients = []


# thread function
def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024).decode('utf-8')

        # reverse the given string from client
        # data = data[::-1]

        name = data.split()[0]
        msg = " ".join(data.split()[1:])

        # send back reversed string to client
        for cl in clients:
            if cl != c:
                cl.send(("[" + name + "]: " + msg).encode('utf-8'))

    # connection closed
    # c.close()


def main():
    host = '127.0.0.1'

    # reserve a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        # print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        clients.append(c)
        start_new_thread(threaded, (c,))
    # s.close()


if __name__ == '__main__':
    main()
