import random
import math_tools as mtools


def chance_points(seed, multiplier):
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


def redeem_points(seed, mode, points):
    """Return points based off of the points deduced and the current mode"""
    mode_lol_indexes = {"normal": 0, "hard": 1, "expert": 2, "expert+": 3}
    mode_list_of_lists = [["normal", [10, 75]], ["hard", [0, 50]], ["expert", [0, 25]], ["expert+", [0, 10]]]
    mode_percent_range = mode_list_of_lists[mode_lol_indexes[mode]][1]

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


def cards(seed, mode, points, hand, deck):
    card_list = ["double", "triple", "safety", "half", "+1 multiplier", "+2 multiplier", "*1.5 multiplier",
                 "+2 temp multiplier", "+4 temp multiplier", "*3 temp multiplier", "+25 score", "*2 score", "free idk",
                 "mode swap", "temp mode swap"]
    choice_loop = True
    while choice_loop:
        card_action = input("What card_action action would you like to use? ").lower()

        if card_action == "play":
            play_loop = True
            while play_loop:
                card_played = input("What card would you like to play?").lower()
                if card_played in hand:
                    confirm_loop = True
                    while confirm_loop:
                        confirmation = input(f"Are you sure you would like to play the card, "
                                             f"\"{card_played}\"?").lower()
                        if confirmation == "y" or confirmation == "yes":
                            pass
                        elif confirmation == "n" or confirmation == "no":
                            confirm_loop = False
                elif card_played in card_list:
                    print("You do not own that card.")
                elif card_played == "cancel":
                    play_loop = False

        elif card_action == "trade":
            trade_loop = True
            while trade_loop:
                card_traded = input("What card would you like to trade?").lower()
                if card_traded in hand:
                    confirm_loop = True
                    while confirm_loop:
                        confirmation = input(f"Are you sure you would like to play the card, "
                                             f"\"{card_traded}\"?").lower()
                        if confirmation == "y" or confirmation == "yes":
                            length = len(hand)
                            for i in range(length):
                                deck.append(card_traded)
                                hand.remove(card_traded)
                                hand.append(deck[0])
                                deck.remove(deck[0])
                            deck = mtools.shuffle_list(deck)
                        elif confirmation == "n" or confirmation == "no":
                            confirm_loop = False
                elif card_traded in card_list:
                    print("You do not own that card.")
                elif card_traded == "cancel":
                    trade_loop = False

        elif card_action == "refresh":
            confirm_loop = True
            while confirm_loop:
                confirmation = input("Are you sure you would like to refresh your entire hand?").lower()
                if confirmation == "y" or confirmation == "yes":
                    length = len(hand)
                    for i in range(length):
                        deck.append(hand[0])
                        hand.remove(hand[0])
                        hand.append(deck[0])
                        deck.remove(deck[0])
                    deck = mtools.shuffle_list(deck)
                if confirmation == "n" or confirmation == "no":
                    confirm_loop = False
