import random
min_value=1
max_value=6
roll_again = "y"
while roll_again == "y":
    print("Rolling the dice...")
    print("The values is....")
    value=random.randint(min_value, max_value)
    print(value)
    roll_again = input("Press 'y' to roll the dices again.")
print("Have a good day.")