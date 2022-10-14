import os

mapping = {}
with open(os.path.dirname(__file__)+"/../apache_logs_big", "r") as f:
    f.readline().split(" ")
    for line in f:
        resp = line.split(" ")[8]
        if resp not in mapping:
            mapping[resp] = 0
        mapping[resp] += 1
print(mapping)