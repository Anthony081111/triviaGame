"""This module reads and saves scores for the trivia program"""
import json


def create_json_file(dict_file):
    try:
        with open("scores.json", "w") as outfile:
            json.dump(dict_file, outfile)
            return
    except Exception as e:
        print(f"Exception message: {str(e)}")
        quit()


def save_scores(name, score):
    """Save a new player's score or modify an already existing player"""
    # see if the player is already listed in the scores file.
    try:
        with open("scores.json", "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f"Exception message: {str(e)}")
        print("Scores not saved.")
        quit()
    list_of_players = data.keys()
    print(list_of_players)
    if name in list_of_players:
        hscore = data[name]["highscore"]
        if hscore < score:
            data[name]["highscore"] = score

        data[name]["totalscore"] += score
        data[name]["attempts"] += 1

    else:
        data.update({name: {"highscore": score, "totalscore": score, "attempts": 1}})
    create_json_file(data)


if __name__ == "__main__":
    scores_dict = {
        "player1": {"highscore": 30, "totalscore": 200, "attempts": 25},
        "player2": {"highscore": 30, "totalscore": 200, "attempts": 25}
    }
    create_json_file(scores_dict)
    name = "player3"
    score = 33
    save_scores(name, score)
