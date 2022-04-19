import json
import csv
import pandas as pd
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#pass which index of questions to get
def getQuestions(n):
    with open(os.path.join(__location__, 'data.json'),"r+") as config:
            d = json.load(config)
    return d[f"questions {n}"]

questions = []

for i in range(1,10000):
    try:
        questions.append(getQuestions(i))
    except:
        break
    else:
        continue

print(questions)


with open('test.csv', 'w+') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = [i for i in questions[0].keys()])
    writer.writeheader()
    writer.writerows(questions)

    print("wrote")