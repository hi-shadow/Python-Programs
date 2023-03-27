import time

time_initial = time.time()

for i in range(100):
    print("Gautam")

print("for loop executed in", time.time() - time_initial, "seconds.")

time2_initial = time.time()
iteration = 0
while iteration < 100:
    print("Gautam")
    iteration += 1

print("While loop run in ", time.time() - time2_initial, "seconds")

