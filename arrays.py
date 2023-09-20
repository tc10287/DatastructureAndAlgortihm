from array import *
"""importing everything from array"""
array1 = array('i', [1, -23, 45, 67, -10])
for x in array1:
    print(x)
print("we're accesing the array from here")
print("element at index 3 is ", array1[3])
print("element at index 0 is ", array1[0])
print("we're going to use insertion method")
array1.insert(2,101)
array1.insert(0,24)
print("NEW ARRAY")
for x in array1:
    print(x)
print("we're going to use the deletion method")
array1.remove(-23)
array1.remove(45)
array1.remove(-10)
print("after deleting, here's the NEW ARRAY")
for x in array1:
    print(x)
print("we're going to search an element, the output should give us it's index")
print("index of 101 is ",array1.index(101))
print("index of 67 is ", array1.index(24))
print("lastly we're doing update some elements in the list")
array1[0]=1999
array1[3]=2023
for x in array1:
    print(x)
