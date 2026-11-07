input_file = "Lecture-11/shell.in"
output_file = "Lecture-11/shell.out"
shells = [1,2,3]
simulation = []
swaps = []
guesses = []

   
with open(input_file,"r") as file: 
    contents = file.readlines()
    n = int(contents[0].replace("\n",""))
    for line in contents[1:]: 
        line = line.replace("\n","")
        a,b,g = list(map(int,line.split(" ")))
        swaps.append([a,b])
        guesses.append(g)

for swap in swaps: 
    a,b = swap 
    shells[a-1],shells[b-1] = shells[b-1],shells[a-1]
    simulation.append(shells.copy())
count = dict.fromkeys([1,2,3],0)
for shell in range(1,4): 
    for i in range(len(simulation)): 
        guess = guesses[i]
        if shell == simulation[i][guess-1]: 
            count[shell] += 1 
shell = 0 
max_count = -1
for key in count: 
    if count[key] > max_count: 
        max_count = count[key]
        shell = key 
with open(output_file,"w") as file: 
    print(shell,file=file)