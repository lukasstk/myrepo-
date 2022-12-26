from helper import validate_and_execute, user_input_message  # * imports everything


# user input \n creates a new line (one enter ), must be in the string, input is always interpreted as a String
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()

message = "sometext"  # string
days = 20  # int
price = 19.99  # float
valid_number = True  # boolean
list_of_days = [20, 30, 50]  # list with int
list_of_months = ["January", "February", "March"]  # list with str
set_of_days = {20, 30, 50}  # set with int/str
days_and_unit = {"days": 10, "unit": "hours"}  # dictionary
