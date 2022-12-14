#port scanner using python(socket library)
import socket
import time
import threading
from queue import Queue


socket.setdefaulttimeout(0.25)
lock = threading.Lock()

ip_address = input('IP Address: ')
host = socket.gethostbyname(ip_address)
print ('Scanning on IP Address: ', host)

def scan(port):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = sock.connect((host, port))
      with lock:
         print(port, 'is open')
      con.close()
   except:
      pass

def execute():
   while True:
      worker = queue.get()
      scan(worker)
      queue.task_done()
      
queue = Queue()
start_time = time.time()
   
for x in range(100):
   thread = threading.Thread(target = execute)
   thread.daemon = True
   thread.start()
   
for worker in range(1, 500):
   queue.put(worker)
   
queue.join()

print('Time taken:', time.time() - start_time)