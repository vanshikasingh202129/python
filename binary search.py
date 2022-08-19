def BinarySearch(nums,low,high,x):
    if (low>high):
        return -1
    mid = low+(high-low)//2
    if (x == nums[mid]):
        return mid
    else:
        if (x<nums[mid]):
            return BinarySearch(nums,low,mid-1,x)
        else:
            return BinarySearch(nums,mid+1,high,x)
nums = [1,2,3,4,5,6,7]
x = 7
print(BinarySearch(nums,1,7,x))
print("hello")

    