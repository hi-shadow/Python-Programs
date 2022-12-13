a=int(input("Enter Your Age Number"))

def isDriving(a):
    if(a<18):
        result = ("You Cant Drive")
    elif(a==18):
        result = ("Let me Think")
    else:
        result = ("You Can Drive")
    return result

print(isDriving(a))
 