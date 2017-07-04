# -*- coding: utf-8 -*-
"""
OnCue Projector
Copyright 2017 Andrew Wong <featherbear@navhaxs.au.eu.org>

The following code is licensed under the GNU Public License Version v3.0
"""


def APIserver():
    import socket
    import select
    CONNECTION_LIST = []  # list of socket clients
    RECV_BUFFER = 1024  # Advisable to keep it as an exponent of 2
    PORT = 2004
    CLIENTS = {}
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while True:
        try:
            server_socket.bind(("0.0.0.0", PORT))
            break
        except OSError:
            print("Port %s is in use, trying port %s" % (PORT, PORT + 1))
            PORT += 1

    server_socket.listen(10)

    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)

    def handleData(data, obj):
        post = None
        print(CLIENTS[obj.getpeername()] + ":", data)
        if data == "STATES":
            data = str(states)
        elif data == "APIOFF":
            data = "API disabled"
            post = _thread.exit
        elif data == "QUIT":
            data = "Quitting OnCue"
            post = app.exit

        obj.send(bytes(data, "utf-8"))
        if post: post()

    print("TCP API server started on port " + str(PORT))
    while True:
        read_sockets, _, _ = select.select(CONNECTION_LIST, [], [])
        for sock in read_sockets:

            # New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                print(server_socket, sockfd, addr)
                CONNECTION_LIST.append(sockfd)
                print("Client (%s, %s) connected" % addr)

            # Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    # In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = str(sock.recv(RECV_BUFFER), "utf-8")
                    pass
                    if sock.getpeername() not in CLIENTS:
                        # Register first message!
                        # if data matches regex format then assign, else disconnect

                        regex = re.search(r"^(\w+?),(\w+)(?:;\w+)*$", data)
                        if not regex: raise Exception("Disconnect")
                        client, intent = regex.groups()
                        intent = intent.split(";")
                        CLIENTS[sock.getpeername()] = client
                        sock.send(bytes(str(CLIENTS), "utf-8"))
                        print("Registered", sock.getpeername(), "as", data)
                    elif data:
                        handleData(data, sock)
                        # echo back the client message
                        # if data:
                        #   sock.send(bytes(data, "utf-8"))

                # client disconnected, so remove from socket list
                except Exception as e:
                    print("Exception:", e)
                    print("Client (%s, %s) disconnected" % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

                    # server_socket.close()
