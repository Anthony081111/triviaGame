""""""

import trivia_questions as tq
import math_tools as mtools
import tools
import trivia_scores as ts

import time
import csv

question_list, q_and_a_dict = tq.get_dict()

score = 0
overscore = 0
choice_loop = True
mode_loop = True

health = 15

questions_survived = 0
questions_incorrect = 0
questions_correct = 0
questions_idk = 0
questions_time_out = 0
questions_override = 0

time_list = []
total_time = 0
default_timer = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

bonus = False
all_answered = False
master = False
code = False

total_points = 0


print("Welcome to your standard trivia game! You are allowed to say, \"I don't know\" and you will not lose points.")
print("If the answer you said is close enough, you are allowed to type, \"whoops\" and it will mark the question as "
      "correct.")
print("To stop, type: \"stop\"")
name = input("What is your name? ")
while mode_loop:
    try:
        mode = input("Select your mode: Free, Normal, Hard, Expert, Expert+, Master, Timed").lower()
        mode, timed, timer, mode_loop, multiplier = tools.mode_responder(mode)
    except TypeError:
        pass
if mode == "master":
    master = True

help_maybe = input("If you would like to learn more, type: \"help\" and you'll be given a list of rules. If not, the "
                   "game will begin. ").lower()

if help_maybe == "help":
    print(tools.get_help())
elif help_maybe == "reset":
    quit()
elif help_maybe == "bonus" and master:
    print("Master difficulty is enabled. You cannot enable bonuses as well.")
elif help_maybe == "bonus":
    confirmation = input(f"Bonuses will mean your multiplier will be: {multiplier*0.5}. "
                         f"Do you want them enabled? ").lower()
    if confirmation == "y" or confirmation == "yes":
        multiplier *= 0.5
        bonus = True


for i in range(len(q_and_a_dict)):
    lost = False
    question = mtools.random_item_from_list(question_list)
    try:
        answer = q_and_a_dict[question].lower()
        printed_answer = q_and_a_dict[question]
    except KeyError:
        print(question)
        print("Sorry, the answer is not in the dictionary. We will fix this mistake when we can.")
        question_list.remove(question)
        break

    choice_loop = True
    while choice_loop:
        question_list.remove(question)
        start = time.time()
        guess = input(f"The question is: \n{question}\nYour answer: ").lower()
        end = time.time()
        if guess == answer:
            questions_correct += 1
            score += 1*multiplier
            overscore += 1*multiplier
            if mode == "free":
                print("Correct!")
                score += 1
                overscore += 1
            else:
                print(f"Correct! Your score now is: {overscore}")
            choice_loop = False
            ready = input("Type anything when ready. ").lower()

        elif guess.lower() == "i dont know" or guess.lower() == "i don't know" or guess.lower() == "idk":
            print(f"That's alright! The correct answer was: {printed_answer}")
            questions_idk += 1
            if mode == "normal" or mode == "hard":
                print(f"Your score is still: {overscore}")
            elif mode == "expert":
                score -= 1*(multiplier/2)
                overscore -= 1*(multiplier/2)
                print(f"Your score is now: {overscore}")
            elif mode == "expert+":
                score -= 1*multiplier
                overscore -= 1*multiplier
                print(f"Your score is now: {overscore}")
            elif mode == "free":
                print("That's okay!")
            elif mode == "master":
                health = 0
                score = 0
                overscore = 0
            choice_loop = False
            ready = input("Type anything when ready. ").lower()

        else:
            print(f"Sadly, that's incorrect. The correct answer was: {printed_answer}")
            questions_incorrect += 1
            if mode == "normal":
                score -= 1
                overscore -= 1
            elif mode == "hard":
                score -= 1*(multiplier/2)
                overscore -= 1*(multiplier/2)
            elif mode == "expert":
                score -= 1*multiplier
                overscore -= 1*multiplier
                health -= 3
                lost = True
            elif mode == "expert+":
                score -= 1*multiplier
                overscore -= 1*multiplier
                health -= 5
            elif mode == "master":
                score = 0
                overscore = 0
                health = 0
            choice_loop = False
            score = mtools.check_negative(score)
            overscore = mtools.check_negative(overscore)
            health = mtools.check_negative(health)
            if mode != "free":
                print(f"Your score is: {overscore}")
            ready = input("Type anything when ready. ").lower()
            if ready == "whoops" and (mode == "free" or mode == "normal"):
                questions_override += 1
                overscore += 2
                print(f"Oh! My bad! Your score is: {overscore}")
                ready = input("Type anything when ready. ").lower()

        elapsed_time = end - start
        time_list.append(elapsed_time)
        if timed and elapsed_time > timer+1:
            if mode == "normal":
                score -= 1*(multiplier/2)
                overscore -= 1*(multiplier/2)
            elif mode == "hard" or mode == "expert" or mode == "expert+":
                score -= 1*multiplier
                overscore -= 1*multiplier
                if not lost and mode == "expert":
                    health -= 3
                elif not lost and mode == "expert+":
                    health -= 5
            elif mode == "master":
                score = 0
                overscore = 0
                health = 0

            questions_time_out += 1
            score = mtools.check_negative(score)
            overscore = mtools.check_negative(overscore)
            health = mtools.check_negative(health)
            print(f"You took too long to enter your answer. Your score is now: {overscore}")

        if health < 1:
            try:
                shortest_time = min(time_list)
                longest_time = max(time_list)
            except ValueError:
                shortest_time = "N/A"
                longest_time = "N/A"
            average_time = mtools.get_average_list(time_list)
            stat_maybe = input(f"You're out of lives! Type anything to quit. ")


            stat_maybe.lower()

            if stat_maybe == "stats" or stat_maybe == "stat":
                tools.display_stats(timed, average_time, questions_survived, questions_correct, questions_incorrect,
                                    questions_idk, questions_override, questions_time_out, longest_time, shortest_time,
                                    overscore, score, total_points)
                if bonus:
                    tools.display_bonuses(timed, average_time, questions_survived, questions_correct,
                                          questions_incorrect, questions_idk, questions_time_out, questions_override,
                                          longest_time, shortest_time, overscore, score, total_points, multiplier,
                                          master, code, all_answered)
            ts.save_scores_csv(name, score)
            quit()

        questions_survived += 1
        total_points += 1*multiplier

        if ready == "stop":

            try:
                shortest_time = min(time_list)
                longest_time = max(time_list)
            except ValueError:
                shortest_time = "N/A"
                longest_time = "N/A"
            average_time = mtools.get_average_list(time_list)


            if mode == "free":
                stat_maybe = input("Okay! Thanks for playing! Type anything to quit. ")
            elif mode == "hard" or mode == "expert" or mode == "expert+":
                stat_maybe = input(f"Okay! Thanks for playing! Your score is: {score}. Type anything to quit. ")

            else:
                stat_maybe = input(f"Okay! Thanks for playing! Your score without overrides is: {score}. "
                                   f"Your score with overrides is: {overscore}. Type anything to quit. ")
            stat_maybe = stat_maybe.lower()

            if stat_maybe == "stats" or stat_maybe == "stat":
                tools.display_stats(timed, average_time, questions_survived, questions_correct, questions_incorrect,
                                    questions_idk, questions_override, questions_time_out, longest_time, shortest_time,
                                    overscore, score, total_points)
                if bonus:
                    tools.display_bonuses(timed, average_time, questions_survived, questions_correct,
                                          questions_incorrect, questions_idk, questions_time_out, questions_override,
                                          longest_time, shortest_time, overscore, score, total_points, multiplier,
                                          master, code, all_answered)
            ts.save_scores_csv(name, score)
            quit()

try:
    shortest_time = min(time_list)
    longest_time = max(time_list)
except ValueError:
    shortest_time = "N/A"
    longest_time = "N/A"
average_time = mtools.get_average_list(time_list)
all_answered = True

if mode == "free":
    stat_maybe = input(f"Oh! It looks like we're out of questions... somehow. Type anything to quit. ")
elif mode == "hard" or mode == "expert":
    stat_maybe = input(f"Oh! It looks like we're out of questions... somehow. But anyways, your score is: {score}. "
                       f"Type anything to quit. ")
else:
    stat_maybe = input(f"Oh! It looks like we're out of questions... somehow. But anyways, your score without "
                       f"overrides is: {score}. Your score with overrides is: {overscore}. Type anything to quit. ")
stat_maybe.lower()

if stat_maybe == "stats" or stat_maybe == "stat":
    tools.display_stats(timed, average_time, questions_survived, questions_correct, questions_incorrect, questions_idk,
                        questions_override, questions_time_out, longest_time, shortest_time, overscore, score,
                        total_points)
    if bonus:
        tools.display_bonuses(timed, average_time, questions_survived, questions_correct, questions_incorrect,
                              questions_idk, questions_time_out, questions_override, longest_time, shortest_time,
                              overscore, score, total_points, multiplier, master, code, all_answered)
ts.save_scores_csv(name, score)
