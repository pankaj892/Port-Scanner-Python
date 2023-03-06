import socket
import threading
from queue import Queue

target = input("Enter the host to be scanned: ")
queue = Queue()
open_ports = []


#check if port is open
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


#fill queue with ports to scan
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


#thread worker function
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open".format(port))
            open_ports.append(port)


#fill queue with ports to scan
port_list = range(1, 1024)
fill_queue(port_list)
thread_list = []

#spawn threads
for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

#start all threads
for thread in thread_list:
    thread.start()

#wait for all threads to finish
for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)
