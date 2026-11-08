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

buckets = [] # this holds milk capacity 
sizes = [] # this holds bucket capacity 
with open(input_file,"r") as file: 
    lines = file.readlines()
    for line in lines: 
        line = line.replace("\n","")
        size,capacity = list(map(int,line.split()))
        sizes.append(size)
        buckets.append(capacity)

for i in range(100): 
    current_bucket = i % 3 
    next_bucket = (i + 1) % 3 
    leftover_milk,milk_capacity = shift_milk(buckets[current_bucket],sizes[next_bucket],buckets[next_bucket])
    buckets[current_bucket] = leftover_milk
    buckets[next_bucket] = milk_capacity

with open(output_file,"w") as file: 
    print(*buckets,sep="\n",file=file)