a = 10


def func_1():
    a = 1

    def inner_func():
        global a
        a += 20
        print("inner function but  globle variable a = ", a)
    inner_func()
    print("after calling inner function a = ", a)


func_1()
