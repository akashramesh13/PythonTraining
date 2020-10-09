import sys
# getting all arguments after python3 command
# storing it in list [args]
args = sys.argv
i = 0
for arg in args:
    print(f"argument {i} is: {arg}")
    i+=1