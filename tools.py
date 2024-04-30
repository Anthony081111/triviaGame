import random

import math_tools as mtools


def get_help():
    help_screen = """
    >Resetting: Want a different mode? Well, just type "reset" on the help screen prompt and it will stop.
    >Override codes: "whoops" will mark an incorrect question as correct when it asks you if you're ready, 
    but only in certain modes. 
    >Yes or no shortcuts: "y" and "n" can be used to answer as "yes" or "no". 
    >Answers are not case sensitive.
    >Reporting: If a question is insulting or not appropriate, you can type "report" after the question or answer.
    >Score without overrides: This is your score, not counting the override codes.
    >You can't get a negative score.
    >Modes:
    -->Normal: The normal way to play: Override codes, "I don't know" allowed.
    -->Timed: Can have any other mode mixed in. Timed just adds a timer per question of your choosing.
    -->Hard: No overrides and "I don't know" allowed.
    -->Expert: You have 3 health. No overrides and a light punishment for "I don't know".
    -->Free: No points, just basic fun."""
    return help_screen


def get_dict():
    """Return the dictionaries."""
    # Here is where you may enter in questions and answers.
    question_list = []       # Enter in your question here.
    q_and_a_dict = {}        # Enter in your question WITH the answer(as the definition) here.
    return question_list, q_and_a_dict


def mode_responder(mode):
    """Select a mode based on an input from the main program."""
    how_much_time = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    timed = False
    extra_text = ""
    time_dict = {5: 3, 10: 2.5, 15: 2, 30: 1.75, 45: 1.5, 60: 1.25}
    multiplier = 1
    choice_loop = True
    stopped = False

    if mode == "free":
        while choice_loop:
            confirmation = input("Are you sure you would like Free mode?").lower()
            if confirmation == "y" or confirmation == "yes":
                return "free", timed, how_much_time, False, multiplier
            elif confirmation == "n" or confirmation == "no":
                choice_loop = False

    elif mode == "timed":
        timed = True
        timed_loop = True
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure you want Timed mode?").lower()
            if confirmation == "n" and confirmation == "no":
                timed = False
                timed_loop = False
            elif confirmation == "y" or confirmation == "yes":
                choice_loop = False
        choice_loop1 = True
        while timed_loop:
            while choice_loop1:
                try:
                    how_much_time = int(input("How much time per question: 5, 10, 15, 30, 45, 60"))
                    choice_loop1 = False
                except ValueError:
                    print("Please enter in a valid time limit.")
            choice_loop2 = True
            while choice_loop2:
                if how_much_time == 5 or how_much_time == 10 or how_much_time == 15 or how_much_time == 30 or \
                        how_much_time == 45 or how_much_time == 60:
                    confirmation = input(f"Are you sure you would like {how_much_time} seconds? This will give you a "
                                         f"{multiplier}x multiplier.").lower()
                    multiplier *= time_dict[how_much_time]
                    if confirmation == "y" or confirmation == "yes":
                        mode = input("Select your second mode: Normal, Hard, Expert").lower()
                        choice_loop2 = False
                        timed_loop = False
                        extra_text = " and Timed"
                else:
                    print("Please enter in a valid time limit.")
                    choice_loop2 = False

    if mode == "hard":
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure that you want Hard mode enabled? "
                                 f"This will give you a {multiplier * 2} multiplier.").lower()
            if confirmation == "y" or confirmation == "yes":
                choice_loop = False
                multiplier *= 2
                return "hard", timed, how_much_time, False, multiplier
            elif confirmation == "n" or confirmation == "no":
                choice_loop = False

    elif mode == "expert":
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure that you want Expert mode enabled? "
                                 f"This will give you a {multiplier * 4} multiplier.").lower()
            if confirmation == "y" or confirmation == "yes":
                choice_loop = False
                multiplier *= 4
                return "expert", timed, how_much_time, False, multiplier
            elif confirmation == "n" or confirmation == "no":
                choice_loop = False

    elif mode == "expert+":
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure that you want Expert mode enabled? "
                                 f"This will give you a {multiplier * 8} multiplier.")
            if confirmation == "y" or confirmation == "yes":
                choice_loop = False
                multiplier *= 8
                return "expert+", timed, how_much_time, False, multiplier
            elif confirmation == "n" or confirmation == "no":
                choice_loop = False

    else:
        print(f"Defaulting to Normal{extra_text} mode.")
        return "normal", timed, how_much_time, False, multiplier


def display_stats(timed, average, questions_survived, questions_correct, questions_incorrect, questions_idk,
                  questions_override, questions_time_out, longest, shortest, overscore, score, highest):
    """Display all of your stats."""

    if timed:
        timed_text = f"Questions answered too late:                    {questions_time_out}\n"
    else:
        timed_text = ""

    print(f"""Stats:
    Questions survived:                             {questions_survived}
    Questions answered correctly:                   {questions_correct}
    Questions answered incorrectly:                 {questions_incorrect}
    Questions answered with "I don't know":         {questions_idk}
    Questions with an override code used:           {questions_override}
    {timed_text}
    Correct question percentage:                    {mtools.get_percent(questions_survived, questions_correct)}%
    Incorrect question percentage:                  {mtools.get_percent(questions_survived, questions_incorrect)}%
    Unknown question percentage:                    {mtools.get_percent(questions_survived, questions_idk)}%

    Longest question time:                          {mtools.round_to_decimal(longest, 2)}
    Shortest question time:                         {mtools.round_to_decimal(shortest, 2)}
    Average time per question:                      {mtools.round_to_decimal(average, 2)}

    Score with overrides:                           {overscore}
    Score without overrides:                        {score}
    Highest possible score:                         {highest}
    """)


def display_bonuses(timed, average, questions_survived, questions_correct, questions_incorrect, questions_idk,
                    questions_time_out, questions_override, longest, shortest, overscore, score, highest, multiplier,
                    master, code, all_answered):
    bonus_score = score

    if questions_survived == questions_correct:
        print(f"Complete success                                +{10*multiplier}")
        bonus_score += 10*multiplier
    if mtools.get_percent(questions_survived, questions_correct) >= 90:
        print(f"A-range                                         +{5*multiplier}")
        bonus_score += 5*multiplier
    if mtools.get_percent(questions_survived, questions_correct) <= 59:
        print(f"F-range                                         +{multiplier}")
        bonus_score += multiplier
    if mtools.get_percent(questions_survived, questions_correct) == 50:
        print(f"Half and half                                   +{2*multiplier}")
        bonus_score += 2*multiplier
    if questions_survived == questions_incorrect:
        print(f"Complete failure                                +1")
        bonus_score += 1
    if master:
        print(f"Master difficulty                               +{25*multiplier}")
        bonus_score += 25*multiplier
    if mtools.get_percent(questions_survived, questions_override) >= 50:
        print(f"Cheater                                         +1")
        bonus_score += 1
    if questions_survived == questions_override:
        print(f"Complete cheater                                +5")
        bonus_score += 5
    if code:
        print(f"Secret code                                     +1")
        bonus_score += 1
    if mtools.get_percent(questions_survived, questions_idk) >= 50:
        print(f"No clue                                         +3")
        bonus_score += 3
    if questions_survived == questions_idk:
        print(f"Completely clueless                             +5")
        bonus_score += 5
    if shortest < 1:
        print(f"Lightening speed                                +{10*multiplier}")
        bonus_score += 10*multiplier
    if longest >= 180:
        print(f"Slow                                            +{multiplier}")
        bonus_score += multiplier
    if shortest >= 180:
        print(f"That's the fastest you can go?                  +{2*multiplier}")
        bonus_score += 2*multiplier
    if all_answered:
        print(f"All questions answered                          +{questions_survived*multiplier}")
        bonus_score += questions_survived*multiplier

        print(f"Score with bonuses:                             {bonus_score}")

    """
    Bonuses:
    I really want to give you a negative score      +{-2*multiplier}
    Funny numbered score                            +{score}
    """


def chance_points(seed, multiplier, card_used=None):
    points_list = [int(str(seed)[-1]) / 10, int(str(seed)[-3]) * 10 + int(str(seed)[-2])]
    max_max_points = max(points_list)
    max_min_points = min(points_list)
    points_list.clear()
    points_list = [int(str(seed)[-4]) / 10, int(str(seed)[-6]) * 10 + int(str(seed)[-5])]
    min_max_points = max(points_list)
    min_min_points = min(points_list)

    max_points = random.randint(max_min_points, max_max_points)
    min_points = random.randint(min_min_points, min_max_points)
    max_points *= multiplier
    min_points *= multiplier


if __name__ == "__main__":
    print("Wrong file doofus.")
