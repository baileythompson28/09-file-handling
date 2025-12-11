import json

SOURCE_FILE = "dish_assignments.json"
OUTPUT_FILE = "invite.txt"


def main():
    with open(SOURCE_FILE, "r") as file:
        data = json.load(file)
    #at this point data should be a list of dictionaries
    with open(OUTPUT_FILE, "w") as file:
        file.write(f"CMP would like to cordially tell you about (but not invite you to) our 2025 thanksgiving feast\n")
        file.write(f"We are excited to share that many of us are pitching in to make this wonderful meal\n")
        file.write(f"Check out what we are going to have\n")
        for entry in data:
            file.write(f"{entry["provider"]} is bringing {entry["servings"]} servings of {entry["dish"]}! " + f"Note: {entry["notes"]}\n")

if __name__ == "__main__":
    main()