"""
· If the file is not found, print “no high scores file located”
· If the file is found:
Open the file (use a “with” statement) and load the csv into a 2D list of values
Loop through the 2D array and print a table that looks like the following:
§ Reminders:
· You can print 30 hashtags with print(“#” * 30)
· You can pad strings with str.ljust(num) or str.rjust(num)
If there are less than 10 records, only print the records you have.
"""

import json
import os
import csv

INPUT_FILE = "highscores.csv"
    
def open_file():
    if not os.path.exists(INPUT_FILE):
        print("no high scores file located")
        return []
    with open(INPUT_FILE, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        rows = []
        for row in csv_reader:
            rows.append(row)
        return rows
    
def main():
    openfile = open_file()
    memory_game = (openfile)
    with open("highscores.csv", "w") as file:
        file.write(json.dumps(memory_game, indent=4))

if __name__ == "__main__":
    main()