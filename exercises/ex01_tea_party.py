"""Exercise 1, planning a cozy tea party!"""

__author__ = "730661650"


def main_planner(guests: int) -> None:
    """this function will define and lay the grounds for calling
    a "main" function, which will give outputs for all
    of the other defined functions within this script"""
    # must construct various print statements for each function below
    # we will define the number of tea bags by calling the tea_bags function
    # define the number of treats by calling the treats function
    # define the cost by calling the cost function
    # must print with the same string literals from the instructions in quotes, followed by the variables
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(int(cost(tea_bags(guests), treats(guests)) * 100) / 100.0))


def tea_bags(people: int) -> int:
    """function to give us total # of tea bags we need"""
    # slightly confused on what to write for the return function
    # realized it is just people * 2 following the return, no parentheses
    return people * 2


def treats(people: int) -> int:
    """function to give us total # of treats we need"""
    # Call tea_bags using a keyword argument
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """this function calculates the total cost
    of the tea bags and treats based on the quantity of people"""
    # must use * for multiplication, multiply teas by .5 and treats by .75, then add to get total
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
