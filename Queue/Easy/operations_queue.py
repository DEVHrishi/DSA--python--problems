from queue import Queue
# Initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize
# of the Queue
print(q.qsize())

# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
q.put('d')

# Return Boolean for Full
# Queue
print("\nFull: ", q.full())

# Removing element from queue

print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
print("Front element : ", q.queue[0])
print("Rear element : ", q.queue[-1])

