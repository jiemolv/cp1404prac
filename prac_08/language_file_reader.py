"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""
import csv
from programming_language import ProgrammingLanguage


def read_languages_csv(file_name):
    languages = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for row in reader:
            name, typing, reflection, year, pointer_arithmetic = row
            reflection = True if reflection == "Yes" else False
            pointer_arithmetic = True if pointer_arithmetic == "Yes" else False
            language = ProgrammingLanguage(name, typing, reflection, int(year), pointer_arithmetic)
            languages.append(language)
    return languages


if __name__ == "__main__":
    languages = read_languages_csv("languages.csv")
    print(languages)
