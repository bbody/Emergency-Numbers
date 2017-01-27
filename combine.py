from os import listdir
from os.path import isfile, join, splitext
import json

def main(path):
    output = {}
    for filename in listdir(path):
        country = splitext(filename)[0]
        extension = splitext(filename)[1]
        if isfile(join(path, filename)) and extension == ".json":
            files = country.split("|")
            if len(files) > 0:
                for e in files:
                    output[e] = open_country(join(path, filename))
            else:
                output[country] = open_country(join(path, filename))
    write_results(output)

def open_country(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_results(output):
    with open('countries.json', 'w') as outfile:
        json.dump(output, outfile, indent=4, sort_keys=True)
        
main("countries")
