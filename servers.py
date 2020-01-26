from socket import *
import thread
import time

BUFF = 1024
HOST = '127.0.0.1'# must be input parameter @TODO
PORT = 9997 # must be input parameter @TODO\

arrAddresses = []
arrConnections = []


def response(key):
    return key

def handler(clientsock,addr):
    global arrConnections
    type = 0
    while 1:
        print "can we"
        if type<=0:
             data = clientsock.recv(BUFF)
             print str(data)
             datatmp = data.split(':')
             print datatmp[0]
             if len(data) >= 0 and datatmp[0].rstrip() == 'man':
                clientsock.send(response(' connected as manager'))
                type = 1
             if len(data) >= 0 and datatmp[0].rstrip()  == 'wor':
                 print 'worker begin'
                 arrConnections.append(clientsock)
                 addr += datatmp[1],
                 print 'address' + repr(addr)
                 arrAddresses.append(addr)
                 clientsock.send(response(' connected as worker'))
                 type = 2                
        if type == 1:
            try:
                r = manager_process(clientsock,addr)
            except:
               print "cannot recieve data"
               break
             
        if type == 2:
          try:
            r = worker_process(clientsock,addr)
          except:
               print "cannot recieve data"
               break
            
        if r <=0 : break
    clientsock.close()
    print addr, "- closed connection" #log on console

def manager_process(clientsock,addr):
      try:
        data = clientsock.recv(BUFF)
      except:
        print 'cannot receive data'
      if not data:
       return -1
      print data
      if "list" == data.rstrip():
       data = list_connections()
      print repr(addr) + ' recv:' + repr(data)
      clientsock.send(response(data))
      print repr(addr) + ' sent:' + repr(response(data))
      if "close" == data.rstrip():
        clientsock.send(response('close'))      
        return -1
      return 1
        
        
def worker_process(clientsock,addr):
     try:
        data = clientsock.recv(BUFF)
     except:
        print 'cannot receive data'
        return -1
     if not data:
       return -1
     print data
     print repr(addr) + ' recv1:' + repr(data)
     clientsock.send(response(data))
     print repr(addr) + ' sent1:' + repr(response(data))
     if "close" == data.rstrip():
      clientsock.send(response('close'))   
      return -1
     return 1

        # type 'close' on client console to close connection from the server side
def refresh_connections(ref):  # used to remove any lost connections
   global arrConnections, arrAddresses
   print 'heihei'
   while True:
    for intCounter, conn in enumerate(arrConnections):
        try:
            conn.send(str.encode("test"))  # test to see if connection is active
        except Exception as msg:
           print 'remove him : %s', msg
           del arrAddresses[intCounter]
           del arrConnections[intCounter]
          #  conn.close()        
    time.sleep(3)
  
def list_connections():
  global arrConnections,arrAddresses
 # refresh_connections()
  print "refresh connection first"
  if len(arrConnections) > 0:
   strClients = ""
   for intCounter, conn in enumerate(arrConnections):
    strClients += str(intCounter) + 4*" " + str(arrAddresses[intCounter][0]) + 4*" " + \
     str(arrAddresses[intCounter][1]) + 4*" " + str(arrAddresses[intCounter][2]) + 4*" "+ "\n"
   print 'list connections'+strClients
   return strClients
  else:
   print("No connections.")
   return 'No Connections'

if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    thread.start_new_thread(refresh_connections,('refresh',))
    while 1:
        print 'waiting for connection... listening on port', PORT
        clientsock, addr = serversock.accept()
        clientsock.setblocking(1)
        print '...connected from:', addr
        thread.start_new_thread(handler, (clientsock, addr))
