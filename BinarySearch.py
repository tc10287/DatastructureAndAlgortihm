#Binary Search
"""Given an array of integers nums which is sorted in ascending order, an integer
target, write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1 """
def binary_search(nums, target): #this function takes in nums list and a target number
    start = 0
    end = len(nums)-1
    while start < end:
        mid = start + (end-start)//2
        if nums[mid] > target: #if target is smaller than the middle number, the middle index will be the end
            end = mid
        elif nums[mid] < target: #if target is larger than middle number, start number will be middle + 1
            start = mid+1
        else:
            return print("position of target is ", mid)
    return print(-1)
nums = [1, 4, 11, 23, 54, 436]
binary_search(nums, 54)
binary_search(nums, 4)
binary_search(nums, 254)
binary_search(nums, 23)
binary_search(nums, 11)

print(type(nums))
"""there was a tutorial about the condition if
if nums[mid]>target:
   end=mid-1
when I implemented that, for a list with even numbers, it won't show the
index of the odd number like number with index 1,3,5 
concept is during the while loop, if the number lies on the index 1 and start and end is both 1, 
then it returns -1 as if there's no number present even though there is

so the condition should be
if nums[mid]>target:
   end=mid
that works perfectly
"""
     
