import socket
import time
import os

RESPONSE = """\
HTTP/1.1 200 OK

<H1>Hello world{}</H1>""".replace("\n", "\r\n")


with socket.socket() as s:
    s.bind(("127.0.0.1", 5434))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    while True:
        conn, addr = s.accept()
        pid = os.fork()
        if pid == 0:
            s.close()
            conn.sendall(RESPONSE.format(os.getpid()).encode())
            time.sleep(10)
            conn.close()
            os._exit(0)
        else:
            conn.close()
    
