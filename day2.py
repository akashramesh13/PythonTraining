#FizzBuzz
N = int(input())

for i in range(1,N+1):
    if i%15==0:
        print("Fizz Buzz")
    elif i%3==0: 
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Guessing game

#Max number of attempts is 10
# The else block will execute if the user doesn't guess in 10 tries since it would've "break"-ed out otherwise
actual_number = 76
tries = 1
while(tries <= 10):
    guessed_number = int(input("Guess the number:\n"))
    if(actual_number == guessed_number):
        print(f"Hooray!!! You've guessed the number in {tries} tries")
        break
    elif(actual_number > guessed_number):
        print("Try a larger value")
    else:
        print("Try a smaller value")
    tries += 1
#Goes here if the program does not break out therefore meaning that the user has failed to guess the number in 10 tries
else:
    print("You have used all 10 tries! Sorry!")

 # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
# else condition will work

num = 11
while num>0:
    num-=1
    if num%2==0:
        continue    
    print(num, end=", ")

    
else:
    print("All numbers are odd in the above example!")


#else condition wont work
num = 10
while num>0:
    if num%2==0:
        print("Breaking out, else wont work")
        break

    
else:
    print("This wont be executed!")
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# number squares multiplication using different ways

#using for-in loop
squares = {"1":1, "2": 4, "3": 9, "4": 16, "5": 25}
for num in squares:
    print(squares[num]*2)

#using keys
squares = {"1":1, "2": 4, "3": 9, "4": 16, "5": 25}

for key in squares.keys():
    squares[key] = squares[key] * 2
print(squares)


#using values
squares = {"1":1, "2": 4, "3": 9, "4": 16, "5": 25}
for values in squares.values():
    print(values*2)
    
#using items
squares = {"1":1, "2": 4, "3": 9, "4": 16, "5": 25}
for key, values in squares.items():
    squares[key] = values*2
print(squares)