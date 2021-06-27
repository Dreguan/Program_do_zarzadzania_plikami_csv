import csv, pickle, json, sys

file_content = []

with open(sys.argv[1], "r") as file:
    reader = csv.reader(file)
    for line in reader:
        file_content.append(line)

for param in sys.argv[3:]:
    print(param.split(","))
    param_list = param.split(",")
    file_content[int(param_list[0])-1][int(param_list[1])-1] = param_list[2]

with open(sys.argv[2], "w", newline="") as file:
    writer = csv.writer(file)
    for line in file_content:
        writer.writerow(line)
