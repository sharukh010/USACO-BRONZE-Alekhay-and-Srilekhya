file_path = "Lecture-10/names.in"
with open(file_path,"r") as file: 
    contents = file.readlines()
    for i in range(len(contents)): 
        contents[i] = contents[i][0:-2]
        # "1\n" -> integer without removing "\n"
    print(contents)