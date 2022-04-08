from http.server import BaseHTTPRequestHandler
import Server

server_address = ('localhost', 8080)
while True:

    request_handler = Server.RequestHandler(BaseHTTPRequestHandler)

    Server.running_server(request_handler, server_address)

