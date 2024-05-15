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


def shuffle_list(selected_list):
    new_list = []
    index = len(selected_list)
    for i in range(index):
        item = selected_list[random.randint(0, len(selected_list) - 1)]
        selected_list.remove(item)
        new_list.append(item)
    return new_list


def check_negative(number):
    """Check if a number is negative. If it is, set it to 0."""
    if number + abs(number) == 0:
        number = 0
    return number


def check_negative_true_false(number):
    modified = check_negative(number)
    if modified != number:
        return True
    else:
        return False


def get_total_list(selected_list):
    """Get the total of a list."""
    total = 0
    for i in selected_list:
        try:
            total += i
        except TypeError:
            quit(58)
    return total


def get_average_list(selected_list):
    average = 0
    total = get_total_list(selected_list)
    try:
        average = total / len(selected_list)
    except ZeroDivisionError:
        quit(69)
    return average


def get_percent(whole, part):
    """Get the percent of two numbers. If the part is equal to 0, the percent will be 0."""
    try:
        int(whole)
        int(part)
    except KeyError:
        quit(79)
    try:
        percent = part/whole * 100
    except ZeroDivisionError:
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
        percent = 0
    return percent


def what_tens_place(number):
    tens_place = 1
    while number >= 10:
        number /= 10
        tens_place += 1
    return tens_place


def coin_flip():
    coin = random.randint(1, 2)
    if coin == 1:
        return False
    elif coin == 2:
        return True


def dice_roll(sides):
    if sides <= 2:
        print("Too few sides!")
        quit()
    return random.randint(1, sides)
