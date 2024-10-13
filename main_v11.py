calculations_to_hours = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculations_to_hours} {name_of_unit}\n"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        # we want to do conversions for positive integers only
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a zero value, please enter a positive number!\n")
        else:
            print("You entered a negative number, please enter a positive number!\n")
    except ValueError:
        print("Your value is not a valid number, don't ruin my program!!!\n")


user_input = ""

while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma seperated list and I will convert it into hours!\n")
    list_of_days = user_input.split(", ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):
        validate_and_execute()

