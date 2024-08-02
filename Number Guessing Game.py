# importing library to generate random numbers
import random
# initializing count of chances at 0
count = 0
# setting the limit of total chances
chances = 7

# taking limits for the range
lower_range = int(input("Enter lower bound: "))
upper_range = int(input("Enter upper bound: "))

# generating a random number
random_number = random.randint(lower_range , upper_range)

while count < chances:
    count += 1

    number = int(input("Enter a number: "))
    if number == random_number:
        print("congratulations! You guessed correctly.")
        break
    else:
        print("Wrong Guess! Enter again...")
        # using nested loop to check if the guessed number is high or low than the original random number
        if number < random_number:
            print("Its Too low")
        else:
            print("Its Too high")


if count == chances and number != random_number:
    print("Better luck next time!")
    print(f"The correct number was {random_number}")

