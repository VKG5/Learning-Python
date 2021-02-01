# importing the multiprocessing module 
import multiprocessing 
import os 

def worker1(): 
	# printing process id 
	print("ID of process running worker1: {}".format(os.getpid())) 
	for i in range(100):
		print("P1",i)

def worker2(): 
	# printing process id 
	print("ID of process running worker2: {}".format(os.getpid()))
	for i in range(100):
		print("P2",i)  

if __name__ == "__main__": 
	# printing main program process id 
	print("ID of main process: {}".format(os.getpid())) 

	# creating processes 
	p1 = multiprocessing.Process(target=worker1) 
	p2 = multiprocessing.Process(target=worker2) 

	# starting processes 
	p1.start() 
	p2.start() 

	# process IDs 
	print("ID of process p1: {}".format(p1.pid)) 
	print("ID of process p2: {}".format(p2.pid)) 

	# wait until processes are finished 
	p1.join() 
	p2.join() 

	# both processes finished 
	print("Both processes finished execution!") 

	# check if processes are alive 
	print("Process p1 is alive: {}".format(p1.is_alive())) 
	print("Process p2 is alive: {}".format(p2.is_alive())) 

	
import multiprocessing
import time


ls = []

def worker1(): 
	# printing process id 
  global ls
  v = []
  for i in range(100):
    for j in range(100):
      for k in range(100):
        v.append([i,j,k])
  ls.append(v)


def worker2(): 
	# printing process id 
  u = []
  global ls
  for i in range(100):
    for j in range(100):
      for k in range(100):
        u.append([i,j,k])
  ls.append(u)

start = time.time()
# creating processes 
p1 = multiprocessing.Process(target=worker1) 
p2 = multiprocessing.Process(target=worker2) 

# starting processes 
p1.start() 
p2.start() 

# wait until processes are finished 
p1.join() 
p2.join() 


end = time.time()
print(end - start)