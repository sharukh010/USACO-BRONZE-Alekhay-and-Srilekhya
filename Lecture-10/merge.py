def merge(list1,list2): 
    length1 = len(list1)
    length2 = len(list2)
    length3 = length1 + length2 
    list3 = [0 for i in range(length3)]
    p1 = 0 # points to list 1 
    p2 = 0 # points to list 2 
    p3 = 0 # points to list 3 
    while p1 < length1 and p2 < length2: 
        if list1[p1] < list2[p2]: 
            list3[p3] = list1[p1] # placing the smallest element 
            # move the pointers 
            p1 += 1 
        else: 
            list3[p3] = list2[p2]
            p2 += 1 
        p3 += 1 

    # if list 1 elements are left copy them directly 
    while p1 < length1: 
        list3[p3] = list1[p1]
        p3 += 1 
        p1 += 1 

    # if list 2 elements are left copy them directly 
    while p2 < length2: 
        list3[p3] = list2[p2]
        p3 += 1 
        p2 += 1 
    return list3

nums1 = [1,4,5,8]
nums2 = [2,3,6,7]
print(merge(nums1,nums2))