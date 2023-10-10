#implement stack using list

stack =[]
def push():
    if len(stack)==limit:
        print("stack is full")
    else:
        element = input("enter an element to add")
        stack.append(element)
        print(stack)

def pop_out():
    x=stack.pop()
    print("deleted element is",x)
    print(stack)

limit=int(input("enter the limit of elements in stack"))
while True:
    choice = int(input("enter your choice 1. push 2. pop 3. quit"))
    if choice==1:
        push()
    elif choice==2:
        pop_out()
    elif choice==3:
        break
    else:
        print("enter a valid choice")

