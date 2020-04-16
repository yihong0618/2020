import socket
import io
import sys

class WSGIServer:

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        # create a socket serve
        self.listen_socket = listen_socket = socket.socket(
                self.address_family, self.socket_type)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(server_address)
        listen_socket.listen(self.request_queue_size)
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.port = port
        self.headers_set = []

    def set_app(self, application):
        self.application = application

    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            self.conn, addr = listen_socket.accept()
            self.handle_one_request()

    def handle_one_request(self):
        request_data = self.conn.recv(1024)
        self.request_data = request_data = request_data.decode("utf-8")
        print(''.join(
            f'< {line}\n' for line in request_data.splitlines()
        ))
        self.parse_result(request_data)
        env = self.get_environ()
        result = self.application(env, self.start_response)
        self.finish_response(result)

    def start_response(self, status, response_headers, exc_info=None):
        server_headers = [
            ('Date', 'Mon, 15 Jul 2019 5:54:48 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + server_headers]

    def parse_result(self, text):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip("\r\n")
        (self.request_method,
         self.path,
         self.request_line
        ) = request_line.split()
        print(self.path)

    def get_environ(self):
        env = {}
        env['wsgi.version']      = (1, 0)
        env['wsgi.url_scheme']   = 'http'
        env['wsgi.input']        = io.StringIO(self.request_data)
        env['wsgi.errors']       = sys.stderr
        env['wsgi.multithread']  = False
        env['wsgi.multiprocess'] = False
        env['wsgi.run_once']     = False
        # Required CGI variables
        env['REQUEST_METHOD']    = self.request_method    # GET
        env['PATH_INFO']         = self.path              # /hello
        env['SERVER_NAME']       = self.server_name       # localhost
        env['SERVER_PORT']       = str(self.port)  # 8888
        return env

    def finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            response = f'HTTP/1.1 {status}\r\n'
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += data.decode('utf-8')
            # Print formatted response data a la 'curl -v'
            print(''.join(
                f'> {line}\n' for line in response.splitlines()
            ))
            response_bytes = response.encode()
            self.conn.sendall(response_bytes)
        finally:
            self.conn.close()


def app(env, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/html")]
    start_response(status, headers)
    return [b"<h1>Hello World</h1>"]


if __name__ == "__main__":
    test = sys.argv[1]
    module, f = test.split(":")
    module = __import__(module)
    bpp = getattr(module, f)
    w = WSGIServer(("127.0.0.1", 5433))
    w.set_app(bpp)
    w.serve_forever()

