file = open("text.txt", "r")
count = 0
for line in file:
    word = line.split(" ")
    count += len(word)

file.close()

print("The total num in the file is: ", count)