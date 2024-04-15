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
    -->Expert: You have 3 lives. No overrides and a light punishment for "I don't know".
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
                        timed_loop = False
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
            confirmation = input("Are you sure that you want Expert mode enabled? "
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


def get_average_list(selected_list):
    """Get the average of a list."""
    items = len(selected_list)
    total = 0
    for i in range(items):
        total += selected_list[i]
    average = total/items
    return average


def get_percent(whole, part):
    """Get the percent of two numbers. If the part is equal to 0, the percent will be 0."""
    try:
        int(whole)
        int(part)
    except KeyError:
        print("Invalid inputs.")
        return "N/A"
    try:
        percent = whole/part * 100
    except ZeroDivisionError:
        percent = 0
    return percent


def display_stats(timed, average, questions_survived, questions_correct, questions_incorrect, questions_idk,
                  questions_time_out, longest, shortest, overscore, score, highest):
    """Display all of your stats."""

    if timed:
        timed_text = f"Questions answered too late:                   {questions_time_out}\n"
    else:
        timed_text = ""

    print(f"""Stats:
    Questions survived:                             {questions_survived}
    Questions answered correctly:                   {questions_correct}
    Questions answered incorrectly:                 {questions_incorrect}
    Questions answered with "I don't know":         {questions_idk}
    {timed_text}
    Correct question percentage:                    {get_percent(questions_survived, questions_correct)}%
    Incorrect question percentage:                  {get_percent(questions_survived, questions_incorrect)}%
    Unknown question percentage:                    {get_percent(questions_survived, questions_idk)}%

    Longest question time:                          {longest}
    Shortest question time:                         {shortest}
    Average time per question:                      {average}

    Score with overrides:                           {overscore}
    Score without overrides:                        {score}
    Highest possible score:                         {highest}
    """)


def check_negative(number):
    """Check if a number is negative. If it is, set it to 0."""
    if number + abs(number) == 0:
        number = 0
    return number


if __name__ == "__main__":
    print("Wrong file doofus.")
