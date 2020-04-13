import socket
import typing


RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 15

<h1>Hello world</h1>""".replace(b"\n", b"\r\n")


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


with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 5433))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        with conn:
            for line in iter_lines(conn):
                print(line)
            conn.sendall(RESPONSE)

