list_string = ["1", "2", "3", "4", "5"]

print(list_string)

# using for loop convert strings items into intiger
for i in range(len(list_string)):
    list_string[i] = int(list_string[i])

print(list_string)

# using map function
list_string = list(map(int, list_string))
# map syntext : map(which function does apply on each element  , on which list , set , tuple etc.)
# explain what i do in upper case :
# first i was give int function for applying on each element on list
# second i convert into a list so now can i print

print(list_string)

# map function is not only for those reasons to use
# another example

list_2nd = [1, 2, 3, 4, 5]


def squre(number):
    return number*number

list_squre = list(map(squre , list_2nd)) 
print(list_squre)