"""This module reads and saves scores for the trivia program"""
import json
import csv


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


def save_scores_csv(name, score):
    try:
        with open("scores.csv", "r") as infile:
            reader = csv.reader(infile)
            data_list = []
            for row in reader:
                data = row
                data_list.append(data)
                print(data_list)
    except Exception as e:
        print(f"Exception message: {str(e)}")
        print("Scores not saved.")
        quit()
    for row in data_list:
        if name in row:
            for i in range(3):
                row[i+1] = int(row[i+1])
            row[2] += score
            row[1] = max([row[1], score])
            row[3] += 1
            save_csv(data_list)
            return
    data_list.append([name, score, score, 1])
    save_csv(data_list)


def save_csv(data_list):
    try:
        with open("scores.csv", "w", newline='') as file:
            write_csv = csv.writer(file)
            write_csv.writerows(data_list)
    except Exception as e:
        print(f"Exception message: {str(e)}")
        print("Scores not saved.")
        quit()

if __name__ == "__main__":
    scores_dict = {
        "player1": {"highscore": 30, "totalscore": 200, "attempts": 25},
        "player2": {"highscore": 30, "totalscore": 200, "attempts": 25}
    }
    # create_json_file(scores_dict)
    name = "named"
    score = 34
    # save_scores(name, score)
    save_scores_csv(name, score)
