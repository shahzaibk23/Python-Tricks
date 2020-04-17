#-----------------Queueu------------
import queue

#-----------FIFO-Queue-----

fifoQueue = queue.Queue(maxsize=20)
fifoQueue.put(5)
fifoQueue.put(4)
fifoQueue.put(3)

print("----------FIFO--------")

print(fifoQueue.get())
print(fifoQueue.get())
print(fifoQueue.get())

#--------LIFO-Queue-------

lifoQueue = queue.LifoQueue()
lifoQueue.put(5)
lifoQueue.put(4)
lifoQueue.put(3)

print("----------LIFO--------")

print(lifoQueue.get())
print(lifoQueue.get())
print(lifoQueue.get())

#-------Priority_Queue----- Mimimum priority

priorityQueue = queue.PriorityQueue()
priorityQueue.put(10)
priorityQueue.put(3)
priorityQueue.put(5)

print("---------- Minimum Priority -------")

print(priorityQueue.get())
print(priorityQueue.get())
print(priorityQueue.get())

#-------Priority_Queue----- Maximum priority

priorityQueue = queue.PriorityQueue()

# all values should be -ve for maximum priority
priorityQueue.put(-10)
priorityQueue.put(-3)
priorityQueue.put(-5)

print("---------- Maximum Priority -------")

print(priorityQueue.get())
print(priorityQueue.get())
print(priorityQueue.get())