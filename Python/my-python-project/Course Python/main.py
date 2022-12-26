from Rest import calculate_to_unit, name_of_unit


def days_to_units(number_of_days):  # functions and function parameters
    # condition_check = number_of_days > 0
    # print(type(condition_check)) checks the datatype of a variable
    return f"{number_of_days} days are {number_of_days * calculate_to_unit} {name_of_unit}"


def validate_and_execute():
    try:  # user_input.isdigit():  # isdigit() only allows positive int

        user_input_number = int(number_of_days_element)

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)  # save a step, no need to assign a variable,
            # int(number_of_days_element) instead of user_input_number
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter a valid positive number!")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")
    # user_input_number = int(user_input) casting a String to an int
    # else:
    # return "you entered a negative value, so no conversion for you!", unnecessary cause is.digit() checks that


# user input \n creates a new line (one enter ), must be in the string, input is always interpreted as a String
user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hours!\n")
    list_of_days = user_input.split(", ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for number_of_days_element in set(list_of_days):  # converts a string to a list datatype,
        # .split splits the List in the character ", ", set doesn't allow duplicate values
        validate_and_execute()
