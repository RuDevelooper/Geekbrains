
import socketserver

class CTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        self.request.recv(1024)

        self.request.send(b"asd")

server = socketserver.TCPServer(("127.0.0.1", "7777"), CTCPHandler)

server.serve_forever()

