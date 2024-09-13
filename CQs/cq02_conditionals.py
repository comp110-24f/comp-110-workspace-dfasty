"""Challenge question 2! Working with conditions"""

__author__ = "730661650"


def guess_a_number() -> None:
    secret = int(7)
    user_input = input("Guess a number: ")
    print(f"Your guess was {user_input}")
    # see if the guess is too high, too low, or they got it
    if int(user_input) == secret:
        print("You got it!")
    elif int(user_input) > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    else:
        print("Your guess was too low! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
