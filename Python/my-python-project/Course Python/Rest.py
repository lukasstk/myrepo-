print("Yeet")  # String
print(2)  # int
print(3.5)  # float
print(20 * 24 * 60)
print("20 days are " + str(50) + " minutes")
print(f"20 days are {20 * 24 * 60} minutes")

# variable to calculate days in seconds
calculate_to_unit = 24
name_of_unit = "hours"
print(f"35 days are {35 * calculate_to_unit} {name_of_unit}")
print(f"50 days are {50 * calculate_to_unit} {name_of_unit}")
print(f"110 days are {110 * 24 * 60 * 60} Seconds")


def scope_check(number_of_days):  # Scope local variable:number_of_days / global variable:name_of_unit
    my_variable = "variable inside function"
    print(name_of_unit)
    print(number_of_days)
    print(my_variable)


scope_check(20)
