import json
import csv
import pandas as pd
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), "data"))

#pass which index of questions to get
class QA():
    @staticmethod
    def writeQA():
        questions = []

        with open(os.path.join(__location__, 'data.json'),"r+") as config:
                d = json.load(config)
    
        for i in range(1,100000):
            try:
                questions.append(d[f"questions {i}"])
            except:
                break 
            else:
                continue 

        with open('test.csv', 'w+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = [i for i in questions[0].keys()])
            writer.writeheader()
            writer.writerows(questions)

        print("wrote")