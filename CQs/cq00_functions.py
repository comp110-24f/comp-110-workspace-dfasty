"""Functions Challenge Question 1"""

__author__ = "730661650"


def mimic(message: str) -> str:
    """Function that repeats input"""
    return message


def main() -> None:
    """Function prints the result of calling the mimic function with the message"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
