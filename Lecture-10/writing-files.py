output_file_path = "Lecture-10/greetings.out"
input_file_path = "Lecture-10/names.in"

def greet(name): 
    return f"Hi, {name}"

with open(input_file_path,"r") as file: 
    names = file.readlines()
    for name in names: 
        message = greet(name)
        with open(output_file_path,"a") as file:
            # file.write(message)
            print(message,file=file,end="")