import socket


r = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 15

<h1>Hello world</h1>""".replace(b"\n", b"\r\n")


with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 5433))
    s.listen(5)
    conn, addr = s.accept()
    print(f"New connection from {addr}.")
    with conn:
        conn.sendall(r)

