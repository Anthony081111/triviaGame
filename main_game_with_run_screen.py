import item_selector as select
import tools

import time

# question_list, q_and_a_dict = tools.get_dict()

question_list = ["Q1", "Q2", "Q3"]
q_and_a_dict = {"Q1": "A1", "Q2": "A2", "Q3": "A3"}
score = 0
overscore = 0
set_number_i = 2
choice_loop = True
mode_loop = True
lives = 3

timed = False
hard = False
free = False
expert = False
multiplier = 1

print("Welcome to your standard trivia game! You are allowed to say, \"I don't know\" and you will not lose points.")
print("If the answer you said is close enough, you are allowed to type, \"whoops\" and it will mark the question as "
      "correct.")
print("To stop, type: \"stop\"")
while mode_loop:
    mode = input("Select your mode: Normal, Timed, Hard, Free, Expert").lower()
    mode_loop, mode, timed, hard, free, expert, multiplier, timer = tools.mode_responder(mode)

help_maybe = input("If you would like to learn more, type, \"help\" and you'll be given a list of rules. If not, the "
                   "game will begin").lower()

if help_maybe == "help":
    print(tools.get_help())
elif help_maybe == "reset":
    quit()

for i in range(len(q_and_a_dict)):
    question = select.random_item_from_list(question_list)
    try:
        answer = q_and_a_dict[question]
    except KeyError:
        print("Sorry, the answer is not in the dictionary. We will fix this mistake when we can.")
        question_list.remove(question)
        break

    choice_loop = True
    while choice_loop:
        question_list.remove(question)
        guess = input(f"The question is: \n{question}\nYour answer:")
        if guess == answer:
            score += 1*multiplier
            overscore += 1*multiplier
            if free:
                print("Correct!")
            elif not free:
                print(f"Correct! Your score now is: {overscore}")
            choice_loop = False
            ready = input("Type anything when ready.").lower()

        elif guess.lower() == "i dont know" or guess.lower() == "i don't know" or guess.lower() == "idk":
            print(f"That's alright! The correct answer was: {answer}")
            if not expert:
                print(f"Your score is still: {overscore}")
            elif expert:
                score -= 1*(multiplier/2)
                print(f"Your score is now: {score}")
            choice_loop = False
            ready = input("Type anything when ready.").lower()

        else:
            print(f"Sadly, that's incorrect. The correct answer was: {answer}")
            if not free:
                score -= 1
                overscore -= 1
            elif hard and not expert:
                score -= 1*(multiplier/2)
            elif expert:
                score -= 1*multiplier
                lives -= 1
            choice_loop = False
            ready = input("Type anything when ready.").lower()
            if ready == "whoops" and not hard:
                overscore += 2
                print(f"Oh! My bad! Your score is: {overscore}")
                ready = input("Type anything when ready.").lower()

        if ready == "stop":
            if free:
                print("Okay! Thanks for playing!")
            elif hard:
                print(f"Okay! Thanks for playing! Your score is: {score}.")
            else:
                print(f"Okay! Thanks for playing! Your score without overrides is: {score}. "
                      f"Your score with overrides is: {overscore}.")
            quit()


if free:
    print(f"Oh! It looks like we're out of questions... somehow. But anyways, thanks for playing!.")
elif hard:
    print(f"Oh! It looks like we're out of questions... somehow. But anyways, your score is: {score}.")
else:
    print(f"Oh! It looks like we're out of questions... somehow. But anyways, your score without overrides is: {score}."
          f"Your score with overrides is: {overscore}.")
