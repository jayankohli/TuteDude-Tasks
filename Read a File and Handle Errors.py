import os

if os.path.exists("sample.txt"):
    print("Reading file content:")
    file = open("sample.txt", "r")
    lines = file.readlines()
    file.close()
    
    count = 1
    for line in lines:
        print("Line", count, ":", line.strip())
        count += 1
else:
    print("Error: The file 'sample.txt' was not found.")
