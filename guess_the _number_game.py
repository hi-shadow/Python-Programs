
no=20
guess_left = 10

while(guess_left>=0):
    inp = int(input("Enter Your Number"))
    guess_left-=1

    if(inp>no):
        print("Greater")
        print("yout have " , guess_left , "guesses left")
    elif(inp==no):
        print("Congratulation You Guess Right")
        break
    else:
        print("Lesser")
        print("yout have " , guess_left , "guesses left")

