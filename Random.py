import random

# genertaes random intiger numbers between 10 to 30
rand = random.randint(10, 30)

# if you want to choose in the list like this you have to use random.choice function

list_1 = ["gautam", "sagar", "nidhi", "hiral",
          "beenaben", "hasmukhbhai", "nimeshkumar"]

randomChoice = random.choice(list_1)
print(randomChoice)


# if you want to generate random number by system [numbers  , not intigers]

# it choose between 0 to 10 [with floting point] [if you want to choose between 1 -100 so *100]
random_numbers = random.random()
random_numbers = random.random() * 100

print(random_numbers)
