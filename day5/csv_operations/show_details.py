import csv
# vscode is considering my python path as default, works fine in IDE
#  so had to change path here.
path = "Documents/python_git/day5/csv_operations/participants.csv"
with open(path) as csv_file:  # read mode by default
    csv_reader = csv.DictReader(csv_file)
    for participant in csv_reader:
        print(
            f"{participant['name']} has {participant['experience(in_years)']} experience in "
            f"{participant['mastered_language']}")