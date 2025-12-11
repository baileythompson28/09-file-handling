"""
The goal of this program will be to open the dishes csv and for each dish,
Ask the user who is bringing the dish. 
It will then produce a json file with the information on what needs brought. 
Each user will be able to add comments/notes about what they are bringing. 
"""
import csv
import os
import json

INPUT_FILE = "dishes.csv"

def get_dish_assignments(dishes):
    """Loops through a dishes 2d list
       Asks who is bringing the dish, asks for additional notes
       Stores the info in a dictionary and adds it to a list        
    """
    assignments = []
    for dish in dishes:
        entry = {}  # empty dictionary
        entry["provider"] = input(
            f"Who is bringing {dish[1]} servings of {dish[0]}? ").strip()
        entry["servings"] = dish[1]
        entry["dish"] = dish[0]
        entry["notes"] = input("Please add any notes: ")
        assignments.append(entry)
        # with open("onetimerun.txt", "a") as file:
        #     file.write(f"{entry["provider"]}\n{entry["notes"]}\n")
    return assignments

def get_dishes():
    if not os.path.exists(INPUT_FILE):
        print("File not found")
        return []
    with open(INPUT_FILE, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # consume the header row. We don't want that.
        rows = []
        for row in csv_reader:
            rows.append(row)
        return rows

def main():
    # declaring this here to pass to a file opening function
    # by declaring here, I can pass it by reference
    dishes = get_dishes()
    # print(dishes)
    assignments = get_dish_assignments(dishes)
    #print(assignments)
    with open("dish_assignments.json", "w") as file:
        file.write(json.dumps(assignments, indent=4))

if __name__ == "__main__":
    main()
 
 