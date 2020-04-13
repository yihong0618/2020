from wsgiref.simple_server import make_server


class Hong:

    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        status = "200 OK"
        response_content = [("Content-type", "text/plain")]
        path = environ["PATH_INFO"]
        response_func = self.routes[path]
        start_response(status, response_content)
        return response_func(path)

    def route(self, route):
        def _(func):
            self.routes[route] = func
        return _


class Request:
    pass


class Reponse:

    def __init__(self, response):
        self.response = response

    def __iter__(self):
        for val in self.response:
            if isinstance(val, bytes):
                yield val
            else:
                yield val.encode()

h = Hong()


@h.route("/hello")
def hello(request):
    name = request.args.get("name", "?")
    return Reponse(f"Hello {name}")


@h.route("/bye")
def bye(request):
    return Reponse("bye")


if __name__ == "__main__":
    s = make_server("127.0.0.1", 5433, h)
    s.serve_forever()
