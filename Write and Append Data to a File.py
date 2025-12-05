text = input("Enter text to write to the file: ")
file = open("output.txt", "w")
file.write(text + "\n")
file.close()
print("Data successfully written to output.txt.\n")

more = input("Enter additional text to append: ")
file = open("output.txt", "a")
file.write(more + "\n")
file.close()
print("Data successfully appended.\n")

file = open("output.txt", "r")
content = file.read()
file.close()

print("Final content of output.txt:")
print(content)
