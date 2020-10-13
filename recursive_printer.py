import os
arr = os.listdir("Documents/python_git")
for val in arr:
    if(val.endswith(".py")):
        print(val)
