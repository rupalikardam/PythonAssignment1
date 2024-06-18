n= input("user imput in file: ")
x = "input.txt"
with open(x,"w") as file :
    file.write(n)

print("the string ", n, "is written in the file")

with open(x,"r") as file:
    y=file.read()

print(y)


