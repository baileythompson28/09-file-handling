filename = "drinks.txt"
# "r" is the mode (read). There are several, but the basics are r, w, a
my_file = open(filename, "r")
# print(my_file)
# get the contents of the file:
content = my_file.read()


# closing is important to free up system resources
print(content)
my_file.close()
# closing and reopening to put cursor back at start of file
my_file = open(filename, "r")
# read a file line by line:
for line in my_file:
    print(line)
my_file.close()

# or use the readlines method:
my_file = open(filename, "r")
lines = my_file.readlines()
for index, line in enumerate(lines):
    print(f"{index}  {line.strip()}")
my_file.close()
 