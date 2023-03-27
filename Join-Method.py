list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_string = ["1", "2", "3 ", "4", "5", "6", "7", "8", "9", "10"]

# for item in list_number:
#     print(item , " , " ,end="")

# you can also add comma(,) via this method
# for item in list_number:
#     print(item , end=" , ")


# using JOIN method
#not work with "string".join(numbers)
list_new = " , ".join(list_string)
print(list_new)