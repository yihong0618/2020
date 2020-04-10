from wsgiref.simple_server import make_server


def app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/html"), ("Contetnt-length", "200")]
    start_response(status, headers)
    yield b"hello"
    yield b"world"


if __name__ == "__main__":
    s = make_server("127.0.0.1", 5433, app)
    s.serve_forever()
