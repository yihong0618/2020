import http.client
from wsgiref.simple_server import make_server
from wsgiref.headers import Headers
from urllib.parse import parse_qs


class Requset:

    def __init__(self, environ):
        self.environ = environ

    @property
    def args(self):
        arguments = parse_qs(self.environ["QUERY_STRING"])
        return {k: v[0] for k,v in arguments.items()}

    @property
    def path(self):
        return self.environ["PATH_INFO"]


class Response:

    def __init__(self, response=None, status=200, charset="utf-8", content_type="text/html"):
        self._headers = Headers()
        self.response = [] if response is None else response
        self.charset = charset
        self.content_type = f"{content_type}; {charset}"
        self._headers.add_header("content_type", content_type)
        self._status = status

    @property
    def status(self):
        status_string = http.client.responses.get(self._status, 'UNKNOWN')
        return '{status} {status_string}'.format(
            status=self._status, status_string=status_string)

    @property
    def headers(self):
        return self._headers.items()

    def __iter__(self):
        for v in self.response:
            if isinstance(v, bytes):
                yield v
            else:
                yield v.encode(self.charset)


class Route:
    def __init__(self):
        pass


def request_application(func):
    def _(environ, start_response):
        request = Requset(environ)
        response = func(request)
        start_response(response.status, response.headers)
        return iter(response)
    return _


def app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/html")]
    args = parse_qs(environ["QUERY_STRING"])
    start_response(status, headers)
    return [b"<h1>hello world</h1>"]

@request_application
def wsgi_app(request):
    print(request.path)
    name = request.args.get("name", "test")
    return Response([f"<h1>Hello {name}</h1>"])

if __name__ == "__main__":
    s = make_server("127.0.0.1", 5433, wsgi_app)
    s.serve_forever()

