import socket
import os
import typing
import mimetypes



SERVER_ROOT = os.path.abspath("www")
print(SERVER_ROOT)


RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 15

<h1>Hello world</h1>""".replace(b"\n", b"\r\n")

BAD_RESPONSE = b"""\
HTTP/1.1 400 Bad Request
Content-type: text/plain
Content-length: 13

Bad Reuquest""".replace(b"\n", b"\r\n")

METHOD_NOT_ALLOWED_RESPONSE = b"""\
HTTP/1.1 405 Method Not Allowed
Content-type: text/plain
Content-length: 17

Method Not Allowed""".replace(b"\n", b"\r\n")

NOT_FOUND_RESPONSE = b"""\
HTTP/1.1 404 Not Found
Content-type: text/plain
Content-length: 9

Not Found""".replace(b"\n", b"\r\n")



FILE_RESPONSE_TEMPLATE = """\
HTTP/1.1 200 OK
Content-type: {content_type}
Content-length: {content_length}

""".replace("\n", "\r\n")

def iter_lines(socket: socket.socket, bufsize: int = 16_384) -> typing.Generator[bytes, None, bytes]:
    buff = b""
    while True:
        data = socket.recv(bufsize)
        if not data:
            return b""
        buff += data
        while True:
            try:
                i = buff.index(b"\r\n")
                line, buff = buff[:i], buff[i+2:]
                if not line:
                    return buff
                yield line
            except:
                break

class Request(typing.NamedTuple):

    method: str
    path: str
    headers: typing.Mapping[str, str]

    @classmethod
    def from_socket(cls, sock: socket.socket) -> "Request":
 
        lines = iter_lines(sock)

        try:
            request_line = next(lines).decode("ascii")
        except StopIteration:
            raise ValueError("Request line is missing")

        try:
            method, path, _ = request_line.split(" ")
        except ValueError:
            raise ValueError("..........")

        headers = {}
 
        for line in lines:
            try:
                name, _, value = line.decode("ascii").partition(":")
                headers[name.lower()] = value.lstrip()
            except ValueError:
                raise ValueError(f"Malformed header line {line!r}")
            
        return cls(method=method.upper(), path=path ,headers=headers)


def serve_file(sock: socket.socket, path: str) -> None:
    if path == "/":
        path = "/index.html"
    abspath = os.path.normcase(os.path.join(SERVER_ROOT, path.lstrip()))
    print(abspath)
    # if not abspath.startswith(SERVER_ROOT):
    #     sock.sendall(NOT_FOUND_RESPONSE)
    #     return
    try:
        with open("www/index.html", "rb") as f:
            stat = os.fstat(f.fileno())
            content_type, encoding = mimetypes.guess_type(abspath)
            if content_type is None:
                content_type = "application/octet-stream"
            if encoding is not None:
                content_type += f"; charset={encoding}"

            response_headers = FILE_RESPONSE_TEMPLATE.format(
                content_type=content_type,
                content_length=stat.st_size,
            ).encode("ascii")
            sock.sendall(response_headers)
            sock.sendfile(f)
    except FileNotFoundError:
        sock.sendall(NOT_FOUND_RESPONSE)
        return


with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 5433))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        with conn:
            request = Request.from_socket(conn)
            serve_file(conn, request.path)
            # conn.sendall(RESPONSE)

