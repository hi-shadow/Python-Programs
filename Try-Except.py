num_1 = 10
num_2 = 0
# print("dision", num_1 / num_2)
# print("this line is very important")  # not show bcz error occured

try:
    print("dision", num_1 / num_2)
except Exception as e:
    print(e)
    print("error occured")

print("this line is very important")  # not show bcz error occured
