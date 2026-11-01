def merge_sort(nums,low,high):
    if low < high: 
        mid = (high+low)//2 
        merge_sort(nums,low,mid) # this splits the left side 
        merge_sort(nums,mid+1,high)# this splits the right side 
        merge(nums,low,mid,high)

def merge(nums,low,mid,high):  
    length1 = mid - low 
    length2 = high - mid+1 
    length3 = length1 + length2 
    list3 = [0 for i in range(length3)]
    p1 = low # points to list 1 
    p2 = mid+1 # points to list 2 
    p3 = 0 # points to list 3 
    while p1 <= mid and p2 <= high: 
        if nums[p1] < nums[p2]: 
            list3[p3] = nums[p1] # placing the smallest element 
            # move the pointers 
            p1 += 1 
        else: 
            list3[p3] = nums[p2]
            p2 += 1 
        p3 += 1 

    # if list 1 elements are left copy them directly 
    while p1 <= mid: 
        list3[p3] = nums[p1]
        p3 += 1 
        p1 += 1 

    # if list 2 elements are left copy them directly 
    while p2 <= high: 
        list3[p3] = nums[p2]
        p3 += 1 
        p2 += 1 

    p1 = low 
    p3 = 0 
    while p1 <= high and p3 < length3: 
        nums[p1] = list3[p3]
        p1 += 1 
        p3 += 1 

nums = [8,7,6,5,4,3,2,1]
merge_sort(nums,0,len(nums)-1)
print(nums)