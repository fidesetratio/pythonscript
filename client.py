import socket
import sys

type = 'wor'

def main():
    connection_handling = 0
    global type;
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 9997

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    print("Enter 'quit' to exit")
    done = False
    while not done:
        if connection_handling <= 0:
          print type
          soc.send(type+':'+str(get_platform()))
          data = soc.recv(1024)
          print data
          connection_handling = 1         
        port = soc.send(raw_input("enter port:"))
        data = soc.recv(1024)
        if "close" == data.rstrip():
          print data
          break
        print "send data.."
        print data
    soc.send(b'--quit--')
    soc.close()

import sys

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]
    
if __name__ == "__main__":
    main()
