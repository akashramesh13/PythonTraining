import pprint

participants = ["Celina", "Akash", "Santhosh", "Himanshu", "Vamsi", "Janani", "Avik", "Tamilpriya"]
participants_dict = {x: participant for x, participant in enumerate(participants)}
print("Before pprint: ", end="")
print(participants_dict)
pp = pprint.PrettyPrinter(indent=4)
print("After pprint: ")
pp.pprint(participants_dict)