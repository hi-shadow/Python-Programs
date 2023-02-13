def func_1(normalargs, *args, **kwargs):
    print("this is a normal argument", normalargs)

    for i in args:
        print(f"{i}")

    for item, value in kwargs.items():
        print(f"{item} and his profession is {value}")


dictionary = {"gautam": "programmer", "sagar": "Rx", "nidhi": "teacher"}
list_1 = ["gautam", "sagar", "nidhi", "hiral"]
func_1("hello bachho", *list_1, **dictionary)
