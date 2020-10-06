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

    