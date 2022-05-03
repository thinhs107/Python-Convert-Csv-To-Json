import csv
import json


def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data

        for rows in csvReader:
            # Assuiming a column named to 'ID' to
            # be the primary key
            key = rows['ID']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    # Add comments

if __name__ == '__main__':
    csvFilePath = r'D:\PycharmProjects\pythonProject\List_Of_Coutries_Currency.csv'
    jsonFilePath = r'D:\PycharmProjects\pythonProject\List_Of_Countries_Currency.json'

    make_json(csvFilePath, jsonFilePath)

