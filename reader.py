import csv, pickle, json, sys

file_content = []

with open("ford_escort.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        file_content.append(line)

file_content[2][1] = 27
print(file_content[2][1])

with open("ford_escort_2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for line in file_content:
        writer.writerow(line)

line_count = 0