n = int(input("enter any number of your choose\n"))
def fact(n):
    if n <= 0:
        return -1
    else:
        return n*fact(n-1)
print(fact(n))
#this gives the right answer but in negative sign

