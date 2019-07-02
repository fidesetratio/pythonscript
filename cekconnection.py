import socket

def is_connected():
    try:
        socket.create_connection(("www.google.co.id",80))
        return True
    except OSError:
        pass
    return False


print("check connection")

if is_connected():
    print("Internet is connected")
else:
    print("Internet is not connected")