from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import cgi


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith('/welcome'):
            try:
                file = open('welcome.html').read()
                self.send_response(200)
            except:
                file = 'File not found!'
                self.send_response(404)

            self.end_headers()
            self.wfile.write(bytes(file, 'utf-8'))

        if self.path.endswith('/vote'):
            try:
                file = open('vote_form.html').read()
                self.send_response(200)
            except:
                file = 'File not found!'
                self.send_response(404)

            self.end_headers()
            self.wfile.write(bytes(file, 'utf-8'))

    def do_POST(self):
        if self.path.endswith('/vote'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                first_name = fields.get('first_name')
                last_name = fields.get('last_name')
                sex = fields.get('sex')
                working = fields.get('working')

                print(first_name[0], last_name[0], sex[0], working[0])

            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()


def running_server(request_handler, server_address):
    while True:
        http_server = ThreadingHTTPServer(server_address, request_handler)
        print('Server is running...')
        http_server.serve_forever()
        try:
            http_server.serve_forever()
        except KeyboardInterrupt:
            http_server.server_close()


server_address = ('localhost', 8080)
running_server(RequestHandler, server_address)
