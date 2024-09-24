"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730661650"


def input_word():
    user_input = input("Enter a 5-character word: ")
    if len(user_input) != 5:
        print("Error: Word must contain 5 characters.")
        # function should exit immediately if the length does not equal 5, so exit should be indented within the if statement
        exit()
    return user_input


def input_letter():
    user_input_1 = input("Enter a single character: ")
    # the length must only be one since it is a single character, does not equal is equal to !=
    if len(user_input_1) != 1:
        print("Error: Character must be a single character.")
        # exit must be indented within the if statement
        exit()
    return user_input_1


def contains_char(word: str, letter: str) -> None:
    print(f"Searching for {letter} in {word}")
    count = 0
    index = 0
    # if index is less than length of word, than index will increase until it is equal to length of word at which point the loop will cease
    while index < len(word):
        if word[index] == letter:
            print(f"{letter} found at index {index}")
            # count must be within the indent, as count must increase each time letter is found
            count += 1
        # index must NOT be indented or else the loop would be infinite since it would never increase
        index += 1
    # we want the function to return "No" instead of "0" if there are no instances of the letter
    # So, we must introduce an if else statement
    if count == 1:
        print(f"1 instance of {letter} found in {word}")
    elif count == 0:
        print(f"No instances of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


def main():
    contains_char(word=input_word(), letter=input_letter())


# to call the aggregated function
if __name__ == "__main__":
    main()
