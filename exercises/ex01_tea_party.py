"""Exercise 1, planning a cozy tea party!"""

___author___ = "730661650"


def main_planner(guests: int) -> None:
    """this function will define and lay the grounds for calling
    a "main" function, which will give outputs for all
    of the other defined functions within this script"""
    # must construct various print statements for each function below
    # must first define the variables
    # we will define the number of tea bags by calling the tea_bags function
    # define the number of treats by calling the treats function
    # define the cost by calling the cost function
    # must print with the same string literals from the instructions in quotes, followed by the variables
    number_of_teabags = tea_bags(guests)
    number_of_treats = treats(guests)
    total_cost = cost(number_of_teabags, number_of_treats)
    print("Tea bags:", number_of_teabags)
    print("Treats:", number_of_treats)
    print("Cost:", total_cost)


def tea_bags(people: int) -> int:
    # slightly confused on what to write for the return function
    # realized it is just people * 2 following the return, no parentheses
    return people * 2


def treats(people: int) -> int:
    # do we do return 1.5 x tea_bags? I am confused on how to write this
    # must add a variable to set equal to the result of the tea_bags function
    number_of_teabags = tea_bags(people)
    number_of_treats = number_of_teabags * 1.5
    # how should i format return statement?
    # must add int before the parentheses
    # number_of_treats inside the parentheses
    return int(number_of_treats)


def cost(tea_count: int, treat_count: int) -> float:
    """this function calculates the total cost
    of the tea bags and treats based on the quantity of people"""
    # must use * for multiplication, multiply teas by .5 and treats by .75, then add to get total
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
