from wsgiref.simple_server import make_server

def app(environment, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/html")]
    start_response(status, headers)
    return [b"<h1>hello world</h1>"]

if __name__ == "__main__":
    s = make_server("127.0.0.1", 5433, app)
    s.serve_forever()

