import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(("localhost", 10000))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    print(f"Connection from {addr}")
    from_client = ''.encode('utf-8')

    while True:
        data = conn.recv(4096)
        if not data: 
            break
        from_client += data
        print(from_client.decode('utf-8'))

        message = "I am server"
        conn.send(message.encode('utf-8'))
        