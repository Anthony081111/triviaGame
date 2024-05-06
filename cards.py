import random
import math_tools as mtools
import tools
import chance


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


def double(points):
    """Returns a doubled base point value, temporary"""
    return points * 2, True


def triple(points):
    """Returns a tripled base point value, temporary"""
    return points * 3, True


def add_one_multiplier(multiplier):
    """Returns a multiplier that's increased by one, permanent"""
    return multiplier + 1, False


def add_two_multiplier(multiplier, temp):
    """Returns a multiplier that's increased by two, may be either temporary or permanent"""
    return multiplier + 2, temp


def add_four_multiplier(multiplier):
    """Returns a multiplier that's increased by four, temporary"""
    return multiplier + 4, True


def times_one_one_half_multiplier(multiplier):
    """Returns a multiplier that's been multiplied by 1.5, permanent"""
    return multiplier * 1.5, False


def times_three_multiplier(multiplier):
    """Returns a multiplier that's been multiplied by three, temporary"""
    return multiplier * 3, True


def add_twenty_five_score(score):
    """Returns a score that's been increased by 25"""
    return score + 25, False


def double_score(score):
    """Returns a doubled score"""
    return score * 2, False


def mode_change(mode, temp, multiplier):
    """Change your mode to a mode similar to your current one"""
    mode_index_dict = {"normal": 0, "hard": 1, "expert": 2, "expert+": 3}
    mode_multiplier_dict = {"normal": 1, "hard": 2, "expert": 4, "expert+": 8}
    mode_list = ["normal", "hard", "expert", "expert+"]
    if mode != "normal" and mode != "expert+":
        choice_loop = True
        while choice_loop:
            mode_input = input(f"What mode will you switch to: "
                               f"{mode_list[mode_index_dict[mode] - 1]} or {mode_list[mode_index_dict[mode] + 1]}")
            if mode_input == mode_list[mode_index_dict[mode] - 1] or mode_input == mode_list[mode_index_dict[mode] + 1]:
                multiplier /= mode_multiplier_dict[mode]
                multiplier *= mode_multiplier_dict[mode_input]
                return mode_input, multiplier, temp
            elif mode_input == mode:
                print("That is your current mode. It is too late to turn back.")
            elif mode_input in mode_list:
                print("That mode is too distant from your own. You must pick a different one.")

    elif mode == "normal":
        print("Switching to Hard mode.")
        return "hard", multiplier * 2, temp
    elif mode == "expert+":
        print("Switching to Expert mode")
        return "expert", multiplier / 2, temp



