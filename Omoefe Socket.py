import socket
from datetime import datetime
import threading
from queue import Queue

#This is to prevent duplicate entries
print_lock = threading.Lock()


print("WELCOME!")
print("This socket scanner will scan for open & closed ports")


host = input("Enter Host To Scan : ")
ip = socket.gethostbyname((host))

print("-" * 80)
print("                  Please wait, Scanning The host -------.", ip)

t1 = datetime.now()
def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip,port))
        if result == 0:
            print("\n Port %d is open" % (port))
            sock.close()
        else:
            print("\n Port %d is close" % (port))
    except:
        pass

#I'm adding threader so the scan can work quickly

def threader():
    while True:
        worker = q.get() #Get a worker from the queue
        scan(worker)    #scan is a function & it run the job with available worker in quene
        q.task_done()   #complete the job
q = Queue()

for x in range(99):
    t = threading.Thread(target=threader)
    t.daemon=True
    t.start()

for worker in range(1, 1026):
    q.put(worker)

q.join()


t2 = datetime.now()

total = t2-t1
print("Scanning completed", total)
