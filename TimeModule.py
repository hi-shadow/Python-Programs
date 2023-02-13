import time

initial = time.time()  # gives a time in accurate miliseconds
print(initial)

# if you want to print local-time you can use
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

# time.sleep()  function is use like setTimeout in javaScript
i = 0
while (i < 10):
    print("hello wolrd")
    i += 1
    time.sleep(2)  # delay execution  2 seconds of every time looping statement
