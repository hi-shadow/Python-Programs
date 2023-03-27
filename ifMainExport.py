def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1-num2


def mul(num1, num2):
    return num1*num2


def div(num1, num2):
    return num1/num2


print(" file internal name is : ", __name__)
if __name__ == '__main__':
    print((add(5, 5)))
    print((sub(5, 5)))
    print((mul(5, 5)))
    print((div(5, 5)))
