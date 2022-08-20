def mergesort(arr):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[(len(arr)//2):]

            #recursion
        mergesort(left)
        mergesort(right)

        #merge sort
        i = 0       #to keep check of left most index in left arr
        j = 0       #to keep check of left most index in right arr
        k = 0       #to keep the index of sorted arr

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                k +=1
                i +=1
            else:
                arr[k] = right[j]
                k += 1
                j += 1
        while i<len(left):
            arr[k] = left[i]
            k +=1
            i +=1
        while j<len(right):
            arr[k] = right[j]
            k += 1
            j += 1
my_arr = [0,5,9,4,7,2,3]
mergesort(my_arr)
print(my_arr)
        



