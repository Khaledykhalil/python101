

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours\n"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 60} minutes\n"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 3600} seconds\n"
    else:
        return "unsupported conversion unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        # we want to do conversions for positive integers only
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a zero value, please enter a positive number!\n")
        else:
            print("You entered a negative number, please enter a positive number!\n")
    except ValueError:
        print("Your value is not a valid number, don't ruin my program!!!\n")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion unit!\n")
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_units_dictionary = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(days_and_units_dictionary)
    print(type(days_and_units_dictionary))
    validate_and_execute()

"""
DATA TYPES (foundational):
message = ("enter some value")
days = 20
price = 9.99
valid_number = True
exit_input = False
list_of_days = [20, 40, 60, 80]
list_of_month = ["January", "February", "March", "April"]
set_of_days = {20, 35, 200}
day_and_unit_dictionary = {"days": 10, "unit": "hours"}
"""