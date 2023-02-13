def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number-1)


a = int(input("Enter Number You want ro factorial "))
print(factorial(a))
