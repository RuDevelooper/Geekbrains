class CBase:

    def __init__(self, sock):

        self.__sock = sock

    def send(self, data):

        data_json = json.dumps(data)
        data_buf = data_json.encode()
        self.__sock.send(data_buf)

    def recv(self):

        data_buf = self.__sock.recv(1024)
        data_json = data_buf.decode()
        data = json.loads(data_json)

        return data

class CClient(CBase):

    def __init__(self, host, port):
        super().__init__(sock)
        sock = socket.socket()
        sock.connect((host, port))

