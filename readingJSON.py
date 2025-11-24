import json

#open the file
#use with so that the file memory is freed up when we're done (no need for file.close())
with open("secret stuff/calendar.json", "r") as file:
    #this loads the json into a dictionary
    data = json.load(file)
    print(data)
    #print it cleaner
    print(json.dumps(data, indent=4))

#print all events in the file:
print(data["events"])
print(type(data["events"]))
print("\n\n\n\n\n\n\n\n")
#our goal:
#loop through events and print the event followed by the days off:
print("DAYS OFF!")
#note events is a list
for item in data["events"]:
    # print(type(event), event)
    print(item["event"])
    for day in item["days"]:
        print(f"- {day}")
 
 
    