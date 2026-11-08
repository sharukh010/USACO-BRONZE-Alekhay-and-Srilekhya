input_file = "Lecture-12/cowsignal.in"
output_file = "Lecture-12/cowsignal.out"

def scale_cols(line,k): 
    scaled_row = ""
    for char in line: 
        scaled_row += char * k 
    return scaled_row

def scale_row(line,k): 
    with open(output_file,"a") as file:
        for i in range(k): 
            print(line,file=file)

lines = []
m = 0 
n = 0 
k = 0
pattern = []  
#reading the input from the file 
with open(input_file,"r") as file: 
    lines = file.readlines()
    m,n,k = map(int,lines[0].split())
    for line in lines[1:]: 
        pattern.append(line.replace("\n",""))


for line in pattern: 
    scaled_row = scale_cols(line,k)
    scale_row(scaled_row,k)


"""
abc
def

scale_cols: 
aabbcc

scale_row: 
aabbcc
aabbcc

ddeeff

ddeeff
ddeeff


"""