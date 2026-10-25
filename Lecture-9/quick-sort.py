def partition(nums,low,high): 
    # consider the first element as pivot 
    pivot = low  
    left = low+1 
    right = high 
    while left< right: 
        # check left side elements 
       
        while left < high: 
            if nums[left] <= nums[pivot]:
                left += 1 # moving to next element 
            else: 
                # if the left value is not less than pivot 
                break 

        while right > low: 
            if nums[right] > nums[pivot]: 
                right -= 1 
            else: 
                # if the right value is not more than pivot 
                break 

        if left < right: # this will be true when we have a big value on left and small value on right 
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp 
    # we will be out of the while loop whenever we get the position of pivot element 
    # pivot element can be swapped with element at right + 1 index
    temp = nums[right]
    nums[right] = nums[pivot]
    nums[pivot] = temp 

    return right 



def quick_sort(nums,low,high):
    if low < high: 
        pivot_index = partition(nums,low,high) 

        # applying quick sort on the left half 
        quick_sort(nums,low,pivot_index-1)
        # applying quick sort on the right half 
        quick_sort(nums,pivot_index+1,high)

with open("Lecture-9/input.in","r") as file: 
    content = file.readlines()
    n = int(content[0])
    nums = [] 
    for i in range(1,n+1): 
        nums.append(int(content[i]))
    quick_sort(nums,0,n-1)
    with open("Lecture-9/output.out","w") as file: 
        file.writelines(",".join(list(map(str,nums))))