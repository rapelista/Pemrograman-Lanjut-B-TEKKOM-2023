import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")

file = open("myfile.txt", "x")
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

f = open("myfile.txt", "r")
print(f.read())
f.close()

file = open("myfile.txt", "w")
file.write("This will remove the previous text")
file.close()

f = open("myfile.txt", "r")
print(f.read(10))
f.close()

file = open("myfile.txt", "a")
file.write("This will add this line")
file.close()

f = open("myfile.txt", "r")
print(f.read())
f.close()