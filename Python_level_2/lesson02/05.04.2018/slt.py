
import select

sock = [ ... ] # Дочерние сокеты

while True:

    ready_for_read, ready_for_write, sock_with_error = select.select(sock, sock, sock, timeout = 1)

    for s in ready_for_read:

        s.recv(1024)

#############################################################################

while True:

    ready_for_read, _, _ = select.select(sock, [], [], timeout = 1)

    for s in ready_for_read:

        s.recv(1024)

