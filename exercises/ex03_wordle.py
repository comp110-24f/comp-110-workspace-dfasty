"""Exercise 3, building a Wordle game."""

__author__ = "730661650"


def input_guess(secret_word_len: int) -> str:
    # we need an f string to call secret_word_len within the prompt with no spaces
    user_guess: str = input(f"Enter a {secret_word_len} character word:")
    # must create a while loop to continuously prompt the user to input a new word until it is equal to the length of the secret word
    while len(user_guess) != secret_word_len:
        print(f"That wasn't {secret_word_len} chars! Try again:")
        print(f"Enter a {secret_word_len} character word:")

    return user_guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """search secret_word to find a potential character match to char_guess"""
    assert len(char_guess) == 1
    index = 0
    # we need a while statement to iterate through each character within the word, relatively simple
    while index < len(secret_word):
        # now we need an if statement, the boolean will become true if the character being iterated through matches the guessed character, returns a boolean
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # we need to define a string variable that will be printed, and each time we receive a value it will be inputted into that string
    # we will define the string as result
    result: str = ""
    index = 0
    while index < len(guess):
        # going to need an if, elif, else function as we have 3 possible scenarios depending on where the letter is contained/ if it is contained
        if guess[index] == secret[index]:
            result += GREEN_BOX
        # confused on how to do this???
        # I see, we need to call the contains_char function with secret and guess[index] to test if guess[index] matches any letters from secret
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1

    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # we must define the total number of turns, which is 6 for a wordle game
    # current turn will begin with 1 and increase with each new typed word
    # we need a boolean type that will exit the while function if the user successfully guesses the word
    turns: int = 6
    current_turn: int = 1
    won_game: bool = False
    # for the while function to execute, current turn should be less than or equal to 6 and the player must not have won
    while current_turn <= turns and won_game == False:
        print(f"=== Turn {current_turn}/{turns} ===")
        # input_guess must be called with the length of the secret word as secret_word_len for the correct # of characters
        user_guess: str = input_guess(len(secret))
        result: str = emojified(user_guess, secret)
        print(result)
        # now we just need an if statement that decides whether or not the player has won yet
        if user_guess == secret:
            won_game = True

        else:
            current_turn += 1

    if won_game:
        print(f"You won in {current_turn}/{turns} turns!")
    else:
        print("Sorry, try again tomorrow!")
        quit()


if __name__ == "__main__":
    main(secret="codes")
