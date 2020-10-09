import csv
with open("day5/csv_operations/participants.csv") as csv_file:  # read mode by default
    csv_reader = csv.DictReader(csv_file)
    for participant in csv_reader:
        print(
            f"{participant['name']} has {participant['experience(in_years)']} years of experience in "
            f"{participant['mastered_language']}")