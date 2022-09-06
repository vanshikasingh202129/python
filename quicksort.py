
def partition(l,r,nums):
    # Last element will be the pivot and the first element the pointer
    pivot = nums[r]
    ptr = l
    for i in range(l,r):
        if nums[i] <= pivot:
        # Swapping values smaller than the pivot to the front
            nums[i] , nums[ptr] = nums[ptr] , nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort(l,r,nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l,r,nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums

mynums = [4,8,3,9,0]
print(quicksort(0,len(mynums)-1,mynums))

 