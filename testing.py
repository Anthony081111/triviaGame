mode = "normal"

mode_lol_indexes = {"normal": 0, "hard": 1, "expert": 2, "expert+": 3}
mode_list_of_lists = [["normal", [10, 75]], ["hard", [0, 50]], ["expert", [0, 25]], ["expert+", [0, 10]]]
mode_percent_range = mode_list_of_lists[mode_lol_indexes[mode]][1]
print(mode_percent_range)
