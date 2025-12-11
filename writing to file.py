import random
# simple write - use "w" - this will overwrite any existing file with that name.
file = open("output.txt", "w")
file.write("Sometimes I like my job...sometimes I don't. \n")
file.close()

# use "a" (for append) to just add to a file, not overwrite it.
file = open("output.txt", "a")
file.write("I just love teaching at ECTS...sometimes.\n")
file.close()

# silly stuff:
names = ["draven", "glen", "levi", "danylo", "mr. klins"]
descriptions = ["coding", "yelling at students", "spinning in chair", "losing all of their points", 
                "wishing thanksgiving was cancelled so blah blah blah"]


# it's going to be better (best practice) if we use "with"
with open("output.txt", "a") as file:
    for name in names:
        file.write(f"{name} is {random.choice(descriptions)}\n")


# handleing exceptions with file handling (reading)
try:
    with open("output.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file does not exist")
except IOError:
    print("IO error")

import csv
#creating our own csv:
# we have data in a 2d list

headers =   ["food", "rating", "maker"]
data = [
    ["mashed potatoes", 4, "bennett"],
    ["corn", 3, "glen"],
    ["turkey", 5, "michael"],
    ["stuffing", 10, "aiden"]
]

#writing
with open("thanksgiving.csv", "w", newline="") as file:
    #create a new csv_writer object:
    csv_writer = csv.writer(file)
    csv_writer.writerow(headers)
    csv_writer.writerow(data)

# #review : reading in a csv
# with open("thanksgiving.csv", "r") as file:
#     csv_reader = csv.reader(file)
#     #consume header:
#     next(csv_reader)
#     for row in csv_reader:
#         print(
#             f"{row[2]} made {row[0]} and it was {"good" if int(row[1]) > 4 else "meh"}")
        
import json
#create a list of dictionaries to save to file:
hippos = [
    {
        "topic": "Species",
        "fact": "There are two living species of hippopotamus: the common hippo and the pygmy hippo.",
        "scientific_name": "Hippopotamus amphibius"
    },
    {
        "topic": "Habitat",
        "fact": "Hippos live in sub-Saharan Africa, spending much of their time in rivers, lakes, and swamps.",
        "details": "Water keeps their skin from drying out and helps them stay cool."
    },
    {
        "topic": "Size",
        "fact": "Adult hippos typically weigh between 3,000 and 4,000 pounds.",
        "extra": "Males are usually larger than females."
    },
    {
        "topic": "Diet",
        "fact": "Hippos are herbivores and mainly graze on grasses at night.",
        "daily_intake_lbs": 80
    },
    {
        "topic": "Behavior",
        "fact": "Hippos are highly territorial in water but less aggressive on land.",
        "note": "They can run up to 20 mph despite their size."
    },
    {
        "topic": "Lifespan",
        "fact": "Hippos typically live 40–50 years in the wild.",
        "record": "The oldest known hippo lived to 61 in captivity."
    },
    {
        "topic": "Social Structure",
        "fact": "Hippos live in groups called pods, bloats, or herds.",
        "average_group_size": 10
    },
    {
        "topic": "Threats",
        "fact": "Major threats include habitat loss and illegal hunting.",
        "iucn_status": "Vulnerable"
    },
    {
        "topic": "Unique Trait",
        "fact": "Hippos secrete a natural reddish sunscreen substance often called 'blood sweat.'",
        "purpose": "It protects their skin and has antibacterial properties."
    },
    {
        "topic": "Reproduction",
        "fact": "Hippo calves are usually born underwater and weigh around 50–100 pounds.",
        "gestation_months": 8
    }
]

with open("hippos.json", "w") as file:
    json.dump(hippos, file, indent=4)