import socket

RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html

<h1>Hello world</h1>
<p>tttt</p>""".replace(b"\n", b"\r\n")


with socket.socket() as s:
    s.bind(("127.0.0.1", 5433))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    while True:
        conn, addr = s.accept()
        with conn:
          data = conn.recv(1024)
          conn.sendall(RESPONSE)
