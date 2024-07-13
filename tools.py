import math_tools as mtools
# hi


def get_help():
    help_screen = """
>Resetting: Want a different mode or mistyped one? Well, just type "reset" on the help screen prompt 
and it will stop.
>Override codes: "whoops" will mark an incorrect question as correct when it asks you if you're ready, 
but only in normal or free mode. 
>Yes or no shortcuts: "y" and "n" can be used to answer as "yes" or "no". 
>Answers are not case sensitive.
>Score without overrides: This is your score, not counting the override codes.
>You can't get a negative score.
>Modes:
-->Normal: The normal way to play: Override codes, "I don't know" allowed.
-->Timed: Can have any other mode mixed in. Timed just adds a timer per question of your choosing.
-->Hard: No overrides and "I don't know" allowed.
-->Expert: You have 5 health. No overrides and a light punishment for "I don't know".
-->Expert+: You have 3 health. No overrides and a light punishment for "I don't know".
-->Free: No points, just basic fun."""
    return help_screen


def mode_responder(mode):
    """Select a mode based on an input from the main program."""
    how_much_time = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    timed = False
    time_dict = {5: 3, 10: 2.5, 15: 2, 30: 1.75, 45: 1.5, 60: 1.25}
    multiplier = 1
    choice_loop = True

    if mode == "free":
        while choice_loop:
            confirmation = input("Are you sure you would like Free mode?").lower()
            if confirmation == "y" or confirmation == "yes":
                return "free", timed, how_much_time, False, multiplier
            elif confirmation == "n" or confirmation == "no":
                return 0, 0, 0, True, 0

    elif mode == "timed":
        timed = True
        timed_loop = True
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure you want Timed mode?").lower()
            if confirmation == "n" or confirmation == "no":
                return 0, 0, 0, True, 0
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
                choice_loop1 = True
                if how_much_time == 5 or how_much_time == 10 or how_much_time == 15 or how_much_time == 30 or \
                        how_much_time == 45 or how_much_time == 60:
                    confirmation = input(f"Are you sure you would like {how_much_time} seconds? This will give you a "
                                         f"{time_dict[how_much_time]}x multiplier.").lower()
                    multiplier = time_dict[how_much_time]
                    if confirmation == "y" or confirmation == "yes":
                        mode = input("Select your second mode: Normal, Hard, Expert").lower()
                        choice_loop2 = False
                        timed_loop = False
                    elif confirmation == "n" or confirmation == "no":
                        choice_loop2 = False
                else:
                    print("Please enter in a valid time limit.")
                    choice_loop2 = False

    if mode == "normal":
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure that you want normal mode enabled? "
                                 f"This will give you a {multiplier}x multiplier.")
            if confirmation == "y" or confirmation == "yes":
                return "normal", timed, how_much_time, False, multiplier
            elif confirmation == "n" or confirmation == "no":
                return 0, 0, 0, True, 0

    elif mode == "hard":
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure that you want Hard mode enabled? "
                                 f"This will give you a {multiplier * 2}x multiplier.").lower()
            if confirmation == "y" or confirmation == "yes":
                multiplier *= 2
                return "hard", timed, how_much_time, False, multiplier
            elif confirmation == "n" or confirmation == "no":
                return 0, 0, 0, True, 0

    elif mode == "expert":
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure that you want Expert mode enabled? "
                                 f"This will give you a {multiplier * 4}x multiplier.").lower()
            if confirmation == "y" or confirmation == "yes":
                multiplier *= 4
                return "expert", timed, how_much_time, False, multiplier
            elif confirmation == "n" or confirmation == "no":
                return 0, 0, 0, True, 0

    elif mode == "expert+":
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure that you want Expert+ mode enabled? "
                                 f"This will give you a {multiplier * 8}x multiplier.")
            if confirmation == "y" or confirmation == "yes":
                multiplier *= 8
                return "expert+", timed, how_much_time, False, multiplier
            elif confirmation == "n" or confirmation == "no":
                return 0, 0, 0, True, 0

    elif mode == "master":
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure that you want Master mode enabled? "
                                 "This will give you a 10x multiplier. You cannot have timed mode enabled with this "
                                 "mode. You'll lose all of your points if you don't answer each question "
                                 "correctly within 10 seconds. You must answer all the questions with one life.")
            if confirmation == "y" or confirmation == "yes":
                multiplier = 10
                return "master", True, 10, False, multiplier
            elif confirmation == "n" or confirmation == "no":
                return 0, 0, 0, True, 0



def display_stats(timed, average, questions_survived, questions_correct, questions_incorrect, questions_idk,
                  questions_override, questions_time_out, longest, shortest, overscore, score, highest):
    """Display all of your stats."""

    if timed:
        timed_text = f"Questions answered too late:                    {questions_time_out}\n"
        more_timed_text = f"Questions answered too late percentage:         " \
                          f"{mtools.get_percent(questions_survived, questions_time_out)}%\n"
    else:
        timed_text = ""
        more_timed_text = ""
    print(f"")
    print(f"""Stats:
    Questions survived:                             {questions_survived}
    Questions answered correctly:                   {questions_correct}
    Questions answered incorrectly:                 {questions_incorrect}
    Questions answered with "I don't know":         {questions_idk}
    Questions with an override code used:           {questions_override}
    {timed_text}
    Correct question percentage:                    {mtools.round_to_decimal(mtools.get_percent(questions_survived, questions_correct), 2)}%
    Incorrect question percentage:                  {mtools.round_to_decimal(mtools.get_percent(questions_survived, questions_incorrect), 2)}%
    Unknown question percentage:                    {mtools.round_to_decimal(mtools.get_percent(questions_survived, questions_idk), 2)}%
    {more_timed_text}
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
        print(f"    Complete success                                +{10*multiplier}")
        bonus_score += 10*multiplier
    if mtools.get_percent(questions_survived, questions_correct) >= 90:
        print(f"    A-range                                         +{5*multiplier}")
        bonus_score += 5*multiplier
    if mtools.get_percent(questions_survived, questions_correct) <= 59:
        print(f"    F-range                                         +{multiplier}")
        bonus_score += multiplier
    if mtools.get_percent(questions_survived, questions_correct) == 50:
        print(f"    Half and half                                   +{2*multiplier}")
        bonus_score += 2*multiplier
    if questions_survived == questions_incorrect:
        print(f"    Complete failure                                +1")
        bonus_score += 1
    if mtools.get_percent(questions_survived, questions_override) >= 50:
        print(f"    Cheater                                         +1")
        bonus_score += 1
    if questions_survived == questions_override:
        print(f"    Complete cheater                                +5")
        bonus_score += 5
    if code:
        print(f"    Secret code                                     +1")
        bonus_score += 1
    if mtools.get_percent(questions_survived, questions_idk) >= 50:
        print(f"    No clue                                         +3")
        bonus_score += 3
    if questions_survived == questions_idk:
        print(f"    Completely clueless                             +5")
        bonus_score += 5
    if shortest < 1:
        print(f"    Lightening speed                                +{10*multiplier}")
        bonus_score += 10*multiplier
    if longest >= 180:
        print(f"    Slow                                            +{multiplier}")
        bonus_score += multiplier
    if shortest >= 180:
        print(f"    That's the fastest you can go?                  +{2*multiplier}")
        bonus_score += 2*multiplier
    if all_answered:
        print(f"    All questions answered                          +{questions_survived*multiplier}")
        bonus_score += questions_survived*multiplier

    print(f"    Score with bonuses:                             {bonus_score}")

    """
    Bonuses:
    I really want to give you a negative score      +{-2*multiplier}
    Funny numbered score                            +{score}
    """


if __name__ == "__main__":
    print("Wrong file doofus.")
