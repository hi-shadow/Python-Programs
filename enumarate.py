list_one = ["zero", "one", "two", "three", "four", "five"]
i = 0
for index, value in enumerate(list_one):
    if index % 2 != 0:
        print(f"please buy {value}")
print("end of loop")
