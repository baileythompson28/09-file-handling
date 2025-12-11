"""
What we will need to do:
- Load 2 files
-- adventure.json - stores the steps to the story
-- past_adventures - stores completed aventures

- Load adventure file
-- If not found, exit program
- Load past adventures
-- If it does not exist just create an empty list. 
- Display a menu
"""
import os
import json
from helpers import type_print

adventure_file = "adventure.json"
past_adventures_file = "past_adventures.json"


def load_adventure(filename):
    with open(filename, "r") as file:
        adventure = json.load(file)

    return adventure


def get_valid_input(step_text, options):
    """
    accepts an options list and gets an index of a valid choice
    returns that index
    sample input:
    [
        { "choice_text": "Knock on the door", "next_id": "cottage" },
        { "choice_text": "Walk past quietly", "next_id": "wolves" }
    ]
    """
    while True:
        type_print(step_text)
        for idx, option in enumerate(options):
            print(f"{idx} : {option["choice_text"]}")
        try:
            choice = int(input("please enter your choice -> ").strip())
        except:
            print("please enter a valid integer")
            continue
        if not 0 <= choice < len(options):
            print(
                f"invalid input. please enter a number between 0 and {len(options)-1}")
        else:
            return choice


def get_username():
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        else:
            print("Enter atleast one character")


def get_step_dict(step, choice):
    current_step = {
        "step_text": step["text"],
        "choices": [val["choice_text"] for val in step["options"]],
        "choice": step["options"][choice]["choice_text"]
    }
    return current_step


def do_adventure(adventure):
    """
    ASSUMES adventure has a start_id key, and a nodes key. 
    identify starting step. Display the text for the step and the options.
        allow the user to choose an option and then display that step. 
    """
    story = {"name": get_username()}
    current_step = adventure["start_id"]
    current_node = adventure["nodes"][current_step]
    story["steps"] = []
    # print(json.dumps(current_node, indent=4))
    while len(current_node["options"]) > 0:
        options = current_node["options"]

        choice = get_valid_input(current_node["text"], options)
        story["steps"].append(get_step_dict(current_node, choice))
        current_step = options[choice]["next_id"]
        current_node = adventure["nodes"][current_step]

    print(current_node["text"])
    story["ending"] = current_node["ending"]
    return story


def load_past_adventures(filename):
    """
    loads the json array stored in the filename and returns it
    if it's not found, an empty list is returned
    """
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except:
                return []
    else:
        print("no past adventures found")
        return []


def print_past_adventure(past_adventure):
    print(f"Explorer: {past_adventure["name"]}")
    print(f"Ending: {past_adventure["ending"]}")
    for idx, step in enumerate(past_adventure["steps"]):
        print(f"Step {idx+1}:")
        print(f"{" " * 4}{step["step_text"]}")
        print(f"{" " * 4}Choices:")
        for i, v in enumerate(step["choices"]):
            print(f"{str(i+1).rjust(10)}) {v}")
        print(f"{" " * 4}Chosen: {step["choice"]}")
        print()


def handle_past_adventures(past_adventures):
    """expects a list of past adventures"""
    if not past_adventures:
        print("No past adventures found yet. Be the first brave explorer!")
    else:
        while True:
            print("Past Adventures:")
            for idx, adv in enumerate(past_adventures):
                print(f"{idx+1}) {adv["name"]} - Ending: {adv["ending"]}")
            choice = input(
                "Enter the number of an adventure to view, or 0 to return to the main menu: ").strip()
            try:
                choice = int(choice)
                choice -= 1
            except:
                print("please enter a valid int")
                continue
            if choice == -1:
                return
            elif choice < 0 or choice >= len(past_adventures):
                print("please choose a number in range")
            else:
                print_past_adventure(past_adventures[choice-1])


def save_past_adventures(past_adventures):
    with open(past_adventures_file, "w") as file:
        file.write(json.dumps(past_adventures, indent=4))


def do_main_menu(adventure, past_adventures:list):
    while True:
        print("""================================
Welcome to the JSON Adventure!
===============================
1) Start a new adventure
2) View past explorers' stories
3) Quit""")
        choice = input("Enter your choice -> ").strip()
        if choice in ["1", "2", "3"]:
            if choice == "1":
                user_adventure = do_adventure(adventure)
                past_adventures.append(user_adventure)
                save_past_adventures(past_adventures)
            elif choice == "2":
                handle_past_adventures(past_adventures)
            else:
                return
        else:
            print("invalid input")


def main():
    # deterimine if adventure_file exists:
    if not os.path.exists(adventure_file):
        print("Adventure file not found")
        exit()  # just bail
    adventure = load_adventure(adventure_file)
    past_adventures = load_past_adventures(past_adventures_file)
    do_main_menu(adventure, past_adventures)


if __name__ == "__main__":
    main()