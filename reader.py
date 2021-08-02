#python reader.py *src* *dst* *change*

import csv, pickle, json, sys

file_content = []

def read_json(file_content):
    with open(sys.argv[1], "r") as file:
        file_content += json.loads(file.read())
        return True

def read_pickle(file_content):
    with open(sys.argv[1], "rb") as file:
        file_content += pickle.loads(file.read())
        return True

def read_csv(file_content):
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        for line in reader:
            file_content.append(line)

extension = sys.argv[1].split(".")[-1]
if extension == "csv":
    read_csv(file_content)
elif extension == "json":
    read_json(file_content)
elif extension == "pickle":
    read_pickle(file_content)
else:
    print("Błędny format pliku docelowego")

for param in sys.argv[3:]:
    print(param.split(","))
    param_list = param.split(",")
    file_content[int(param_list[0])-1][int(param_list[1])-1] = param_list[2]

print(file_content)

extension = sys.argv[2].split(".")[-1]
if extension == "csv":
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.writer(file)
        for line in file_content:
            writer.writerow(line)
elif extension == "json":
    with open(sys.argv[2], "w", newline="") as file:
        file_content_json = json.dumps(file_content)
        file.write(file_content_json)
elif extension == "pickle":
    with open(sys.argv[2], "wb") as file:
        file_content_pickle = pickle.dumps(file_content)
        file.write(file_content_pickle)
else:
    print("Błędny format pliku docelowego")
