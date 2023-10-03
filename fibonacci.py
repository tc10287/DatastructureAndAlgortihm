def fibo(a): #concept: third number of fibonacci is the addition of first and second
    if(a<1):
        return 1
    else:
        return(fibo(a-1)+fibo(a-2))

term= int(input("enter the number of terms for fibonnaci series\n"))
for x in range(term):   #for loop is used to print out all the values
    print(fibo(x))



