import csv

# Sample CSV reading
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)