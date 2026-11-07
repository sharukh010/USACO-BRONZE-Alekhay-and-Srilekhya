input_file = "Lecture-11/mixmilk.in"
output_file = "Lecture-11/mixmilk.out"
def shift_milk(bucket1_milk_capacity,bucket2_capacity,bucket2_milk_capaciaty): 
    pb_milk_capacity = bucket1_milk_capacity
    total_capacity = bucket2_capacity # target bucket 
    milk_capacity = bucket2_milk_capaciaty # target bucket milk capacity 
    freespace = total_capacity - milk_capacity
    shifted_milk = min(pb_milk_capacity,freespace)
    milk_capacity += shifted_milk
    leftover_milk = pb_milk_capacity - freespace 
    if leftover_milk < 0: 
        leftover_milk = 0 
    return leftover_milk,milk_capacity

buckets = []
sizes = []
with open(input_file,"r") as file: 
    lines = file.readlines()
    for line in lines: 
        line = line.replace("\n","")
        size,capacity = list(map(int,line.split()))
        sizes.append(size)
        buckets.append(capacity)

print(buckets)
print(sizes)