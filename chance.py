import random
import math_tools as mtools


def choose_points(seed, multiplier):
    """Return an amount of points to add or deduce because of an incorrect or correct question.
    Based off of the multiplier"""
    points_list = [int(str(seed)[-1]) / 10, int(str(seed)[-3]) * 10 + int(str(seed)[-2])]
    max_max_points = max(points_list)
    max_min_points = min(points_list)
    points_list.clear()
    points_list = [int(str(seed)[-4]) / 10, int(str(seed)[-6]) * 10 + int(str(seed)[-5])]
    min_max_points = max(points_list)
    min_min_points = min(points_list)
    points_list.clear()

    max_points = random.randint(max_min_points, max_max_points)
    min_points = random.randint(min_min_points, min_max_points)
    points_list.append(max_points)
    points_list.append(min_points)
    max_points = max(points_list)
    min_points = min(points_list)
    max_points *= multiplier
    min_points *= multiplier
    return random.randint(min_points, max_points)


def redeem_points(seed, mode, points, timed):
    """Return points based off of the points deduced and the current mode"""
    mode_lol_indexes = {"normal": 0, "hard": 1, "expert": 2, "expert+": 3}
    mode_list_of_lists = [["normal", [10, 75]], ["hard", [0, 50]], ["expert", [0, 25]], ["expert+", [0, 10]]]
    if timed:
        mode_list_of_lists = [["normal", [25, 100]], ["hard", [10, 75]], ["expert", [0, 30]], ["expert+", [0, 15]]]
    mode_percent_range = mode_list_of_lists[mode_lol_indexes[mode]][1]
    if mtools.coin_flip():

        influencing_list = [int(str(seed)[-7]), int(str(seed)[-8])]
        max_max_influence = max(influencing_list)
        max_min_influence = min(influencing_list)
        influencing_list.clear()

        influencing_list = [int(str(seed)[-9]), int(str(seed)[-10])]
        min_max_influence = max(influencing_list)
        min_min_influence = min(influencing_list)

        min_percent = int(min(mode_percent_range)) + random.randint(min_min_influence, min_max_influence)
        max_percent = int(max(mode_percent_range)) + random.randint(max_min_influence, max_max_influence)
        percent_redemption = random.randint(min_percent, max_percent) / 100
        redemption_points = mtools.round_to_decimal(points * percent_redemption, 2)
        return redemption_points
    else:
        return 0


def revive(mode):
    """If the player is out of lives, there is a slim chance they will be revived. Returns the amount of health given
    back upon revival."""
    revival_chance = random.randint(1, 100)
    if revival_chance in range(1, 5):
        print("It's not over yet...")
        health_redeemed = random.randint(1, 100)
        if health_redeemed == 1:
            print("Full revival given!")
            return 15
        elif health_redeemed in range(2, 7):
            print("Full revival attempted, but malfunctioned")
            if mode == "expert":
                return 12
            elif mode == "expert+":
                return 10
        elif health_redeemed in range(7, 17):
            coin = mtools.coin_flip()
            if mode == "expert":
                if coin:
                    extra_text = "Stopped damage before severe consequence. Two lives left"
                    health = 6
                elif not coin:
                    extra_text = "Severe impact! One life left."
                    health = 3
            elif mode == "expert+":
                if coin:
                    extra_text = "No effect on current gamemode. Full revival given!"
                    health = 15
                elif not coin:
                    extra_text = "Little effect on current gamemode. Near-full revival given."
                    health = 10
            print(f"Expert mode malfunction... {extra_text}")
            return health

        elif health_redeemed in range(18, 28):
            coin = mtools.coin_flip()
            if mode == "expert":
                if coin:
                    extra_text = "No effect on current gamemode. Full revival given!"
                    health = 15
                elif not coin:
                    extra_text = "Little effect on current gamemode. Near-full revival given."
                    health = 12
            elif mode == "expert+":
                if coin:
                    extra_text = "Stopped damage before severe consequence. Two lives left"
                    health = 10
                elif not coin:
                    extra_text = "Severe impact! One life left!"
                    health = 5
            print(f"Expert+ mode malfunction... {extra_text}")
            return health


