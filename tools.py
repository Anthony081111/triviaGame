def get_help():
    help_screen = """
    >Resetting: Want a different mode? Well, just type "reset" on the help screen prompt and it will stop.
    >Override codes: "whoops" will mark an incorrect question as correct when it asks you if you're ready, 
    but only in certain modes. 
    >Yes or no shortcuts: "y" and "n" can be used to answer as "yes" or "no". 
    >Answers are not case sensitive.
    >Reporting: If a question is insulting or not appropriate, you can type "report" after the question or answer.
    >Score without overrides: This is your score, not counting the override codes.
    >Modes:
    -->Normal: The normal way to play: Override codes, "I don't know" allowed.
    -->Timed: Can have any other mode mixed in. Timed just adds a timer per question of your choosing.
    -->Hard: No overrides and "I don't know" allowed.
    -->Expert: You have 3 lives. No overrides and a light punishment for "I don't know".
    -->Free: No points, just basic fun."""
    return help_screen


def get_dict():
    # Here is where you may enter in questions and answers.
    question_list = []       # Enter in your question here.
    q_and_a_dict = {}        # Enter in your question WITH the answer(as the definition) here.
    return question_list, q_and_a_dict


def mode_responder(mode):
    how_much_time = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    timed = False
    extra_text = ""
    time_dict = {5: 3, 10: 2.5, 15: 2, 30: 1.75, 45: 1.5, 60: 1.25}
    multiplier = 1
    choice_loop = True

    if mode == "free":
        while choice_loop:
            confirmation = input("Are you sure you would like Free mode? "
                                 "This will permanently set your multiplier to 0.").lower()
            if confirmation == "y" or confirmation == "yes":
                return False, "free", False, False, True, False, 0, how_much_time
            elif confirmation == "n" or confirmation == "no":
                choice_loop = False

    elif mode == "timed":
        timed_loop = True
        timed = True
        while timed_loop:
            choice_loop = True
            while choice_loop:
                try:
                    how_much_time = int(input("How much time per question: 5, 10, 15, 30, 45, 60"))
                    choice_loop = False
                except ValueError:
                    print("Please enter in a valid time limit.")
            choice_loop = True
            while choice_loop:
                if how_much_time == 5 or how_much_time == 10 or how_much_time == 15 or how_much_time == 30 or \
                        how_much_time == 45 or how_much_time == 60:
                    multiplier *= time_dict[how_much_time]
                    confirmation = input(f"Are you sure you would like {how_much_time} seconds? This will give you a "
                                         f"{multiplier}x multiplier.").lower()
                    if confirmation == "y" or confirmation == "yes":
                        mode = input("Select your second mode: Normal, Hard, Expert").lower()
                        choice_loop = False
                        extra_text = " and Timed"
                else:
                    print("Please enter in a valid time limit.")
                    choice_loop = False

    if mode == "hard":
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure that you want Hard mode enabled? "
                                 "This will give you a 2x multiplier.").lower()
            if confirmation == "y" or confirmation == "yes":
                choice_loop = False
                multiplier *= 2
                return False, "hard", timed, True, False, False, multiplier, how_much_time
            elif confirmation == "n" or confirmation == "no":
                choice_loop = False

    elif mode == "expert":
        choice_loop = True
        while choice_loop:
            confirmation = input("Are you sure that you want Hard mode enabled? "
                                 "This will give you a 4x multiplier.").lower()
            if confirmation == "y" or confirmation == "yes":
                choice_loop = False
                multiplier *= 4
                return False, "expert", timed, True, False, True, multiplier, how_much_time
            elif confirmation == "n" or confirmation == "no":
                choice_loop = False

    else:
        print(f"Defaulting to Normal{extra_text} mode.")
        return False, "normal", timed, False, False, False, multiplier, how_much_time
