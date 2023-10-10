import queue
stack = queue.LifoQueue()
stack.put(23)
stack.put(123)
stack.put(243)
e=stack.get()
print(e)
print(not stack)
print(stack.qsize())

