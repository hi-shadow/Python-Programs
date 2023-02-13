filepointer = open("01_Example.txt")
# content = filepointer.read(3)  # only 3 character read
content2 = filepointer.read()
# all character read but upper statement are already readed 3 charactor so it read after 3 charactor

# print(content)  # print 3 character

print(content2)  # print all charactor after that 3 charactor

# Iterate charator using for loop [if use for loop no content are not already readed]

# for line in content2:
#     print(line)


# Iterate lines using for loop

# for line in filepointer:
# print(line)

# print(filepointer.readline())
# print(filepointer.readline())
# print(filepointer.readline())

# print(filepointer.readlines())
filepointer.close()
