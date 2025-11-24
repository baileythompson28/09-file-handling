import csv

#when dealing with files (csv or not) use WITH
with open("Dragon-Ball-Z.csv", "r") as file:
    csv_reader = csv.reader(file) 
    #gives us a cursor pointing at the first row of the file:
    first = next(csv_reader) # first line
    for row in csv_reader:
        for idx, label in enumerate(first):
            print(f"{label}: {row[idx]}")
        print()

        
with open("Dragon-Ball-Z.csv", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()