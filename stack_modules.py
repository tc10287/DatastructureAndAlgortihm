import collections #importing collections module
stack = collections.deque() #collections has a class called deque
stack.append(12)
stack.append(122)
stack.append(112)
stack.append(1223)
print(stack)
stack.pop()
stack.pop()
print(not stack) #checks if stack is empty or not
print(stack)
print(stack[-1]) #returns the top of the stack