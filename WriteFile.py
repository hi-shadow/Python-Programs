# W mode : first clear a file and after that add
# a mode :  add content to the file

# filepointer = open("01_Example.txt ", "w")
# filepointer = open("01_Example.txt ", "a")
# charactor = filepointer.write("Hii My Name Is Gautam \n")
# print(charactor)


# handle read and right mode both
# R+ mode : read and write both mode


filepointer = open("01_Example.txt ", "r+")
filepointer.write("i am a student of kamani science collage")
print(filepointer.read())


filepointer.close()
