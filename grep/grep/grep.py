file_name = input("Enter the file name: ")
pattern = input("Enter the pattern to search for: ")

file = open(file_name, 'r')
line = file.readline()

while line:
    if pattern in line:
        print(line)
    line = file.readline()
