import random


def random_item_from_list(selected_list, minimum=None, maximum=None):
    try:
        selector = random.randint(minimum, maximum)
    except TypeError:
        selector = random.randint(0, len(selected_list) - 1)
    selected_item = selected_list[selector]
    return selected_item


def select_item_from_list(selected_list, minimum=None, maximum=None):
    keep_going = True
    choice_loop = True

    while keep_going:
        try:
            selector = random.randint(minimum, maximum)
        except TypeError:
            selector = random.randint(0, len(selected_list) - 1)
        selected_item = selected_list[selector]

        while choice_loop:
            okay = input(f"Is this item okay: \n{selected_item}").lower()
            if okay == "y" or okay == "yes":
                return selected_item
            elif okay == "n" or okay == "no":
                selected_list.remove(selected_item)
                print("Okay.")
                break
            else:
                print("Please answer with yes or no.")


def check_negative(number):
    """Check if a number is negative. If it is, set it to 0."""
    if number + abs(number) == 0:
        number = 0
    return number


def get_total_list(selected_list):
    """Get the total of a list."""
    total = 0
    for i in selected_list:
        try:
            total += i
        except TypeError:
            print("Invalid item in list(Error Code 311)")
            quit(311)
    return total


def get_average_list(selected_list):
    average = 0
    total = get_total_list(selected_list)
    try:
        average = total / len(selected_list)
    except ZeroDivisionError:
        print("Empty list, cannot calculate average(Error Code 321)")
        quit(321)
    return average


def get_percent(whole, part):
    """Get the percent of two numbers. If the part is equal to 0, the percent will be 0."""
    try:
        int(whole)
        int(part)
    except KeyError:
        print("Invalid inputs(Error Code 312)")
        quit(312)
    try:
        percent = whole/part * 100
    except ZeroDivisionError:
        print("Part is zero, cannot divide by zero(Warning Code 311)")
        percent = 0
    return percent


def round_to_decimal(number, power_of_ten):
    """Round to the nearest decimal place"""
    number *= 10 ^ power_of_ten
    number = round(number)
    number /= 10 ^ power_of_ten
    return number


def get_percent_change(whole, part):
    """Get the percent increase of two numbers."""
    if whole == part:
        return 0
    difference = abs(whole - part)
    try:
        percent = (difference / whole) * 100
    except ZeroDivisionError:
        print("Whole is zero, cannot divide by zero(Warning Code 312)")
        percent = 0
    return percent
