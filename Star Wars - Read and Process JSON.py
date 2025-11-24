"""
Write a program to open the star_wars.json file, print all item names, then underneath that print their basic info.
Example:
Luke Skywalker
- Height: 172
- Mass: 77
- Hair Color: blonde
- Skin color: fair
- Eye color: blue
- Gender: male
"""

import json

with open("star_wars.json", "r") as file:
    data = json.load(file)

    for item in data["results"]:
        print(item["name"])
        print(f"- Height: {item['height']}")
        print(f"- Mass: {item['mass']}")
        print(f"- Hair Color: {item['hair_color']}")
        print(f"- Skin color: {item['skin_color']}")
        print(f"- Eye color: {item['eye_color']}")
        print(f"- Gender: {item['gender']}")
