def what_tens_place(number):
    tens_place = 1
    while number >= 10:
        number /= 10
        tens_place += 1
    return tens_place


print(what_tens_place(100))
