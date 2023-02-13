file = open("01_Example.txt")

print(file.readline())
print(file.tell())  # prints the character number where you are
print(file.readline())
file.seek(0)  # place the character number
print(file.tell())  # prints the character number where you are
print(file.readline())


file.close()
