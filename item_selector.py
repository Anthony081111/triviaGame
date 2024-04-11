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
                # selected_list.remove()                      I don't know how this works feel free to fix.
                print("Okay.")
                break
            else:
                print("Please answer with yes or no.")


# only for testing purposes.
if __name__ == "__main__":
    test_list1 = ["item0", "item1", "item2", "item3", "item4"]
    test_list2 = ["item0", "item1min", "item2", "item3max", "item4"]
    test_list3 = ["item0", "item1", "item2min&max", "item3", "item4"]
    for i in range(2):
        print(select_item_from_list(test_list1), "\n success")
        print(f"Times went through loop:  {i+1}")
