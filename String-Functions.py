str = "Gautam"
print()
print(str)
print(str[1])  # 1st index character
# print(str[90])  # error  bcz index out of bound

# String Slicing

print(str[0:6])  # prints index 0 to 5 characters
print(str[1:6])  # prints index 1 to 5 characters
print(str[0:90])  # prints  0 to 90 index characters  if 90 are possible or not

print(len(str))  # length of string


# skip every  2nd indexed character of string like (GAUTAM = G_U_ A_)
print(str[0::2])
# print Oth index character and after that it jumps to 2345432's character (if it possible either its run as normally no any error)
print(str[0::2345432])

print(str[0::1])  # print full
print(str[-2:])  # prints from reverce index gaut'am' and prints
print(str[-2:-3])  # prints from reverce index g'autam' and prints

print(str[::-1])  # reverse the string
