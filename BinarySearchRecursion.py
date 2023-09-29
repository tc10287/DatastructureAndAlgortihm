
def BinarySearch(nums,start,end,target):
    if(start<end):
        mid= start+(end-start)//2
        if(nums[mid]==target):
            return (print(mid))
        elif(nums[mid]<target):
            return (BinarySearch(nums,mid+1,end,target))
        elif(nums[mid]>target):
            return (BinarySearch(nums,start,mid,target))
    else:
        return (print(-1))

nums = [1, 4, 11, 23, 54, 436,678,679,2000]

BinarySearch(nums,0,len(nums),2000)
BinarySearch(nums,0,len(nums),23)
BinarySearch(nums,0,len(nums),4326)




