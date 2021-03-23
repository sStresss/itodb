import socket
import time
data = ''
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65101  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    while data == '':
        try:
            s.connect((HOST, PORT))
            data = 'SENDINGDATA'
            data = data.encode()
            s.sendall(data)
            data = s.recv(1024)
            print('123')
            time.sleep(0.2)
        except:
            print("waiting....")
            time.sleep(0.2)


print('Received', repr(data))