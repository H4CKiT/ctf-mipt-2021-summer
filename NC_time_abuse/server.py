import socket
import threading
import time


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(50)
        while True:
            client, address = self.sock.accept()
            client.gettimeout()
            client.settimeout(60)
            threading.Thread(target=self.listenToClient, args=(client, address)).start()

    def listenToClient(self, client, address):
        print(f"New connection {address}")
        size = 1024
        while True:
            try:
                data = client.recv(size)
                data = data[:-1]
                if data:
                    # Set the response to echo back the recieved data
                    print(data)
                    client.send("Hello my friend, now try to guess the password[0-9a-zA-Z)):\n".encode('utf-8'))
                    print("Hello guess", address)
                else:
                    client.shutdown(2)
                    client.close()
                    print('Close connection', address)
                    return False
                while True:
                    data = client.recv(size)
                    data = data[:-1]
                    if data:
                        # Set the response to echo back the recieved data
                        print("Password try", data, address)
                        password = b'ReaLlyNicEgueSs1337maYbeNOt'
                        if data == password:
                            client.send(f"Yeah, it's correct, your flag is {'mipt_ctf_wait_for_flag'}\n".encode('utf-8'))
                            print("Nice guess", address)
                            client.shutdown()
                            client.close()
                            print('Close connection', address)
                            return False
                        else:
                            for i in range(min(len(password), len(data))):
                                if password[i] == data[i]:
                                    time.sleep(1)
                                else:
                                    break
                            client.send(f"Go sleep. It's too hard for you\n".encode('utf-8'))
                            print("Nice try", address)
                    else:
                        client.shutdown(2)
                        client.close()
                        print('Close connection', address)
                        return False
            except:
                client.shutdown(2)
                client.close()
                print('Close connection', address)
                return False


if __name__ == "__main__":
    ThreadedServer('0.0.0.0', 8889).listen()
