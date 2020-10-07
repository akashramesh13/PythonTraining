# Multiples of 3 using range function
num = 3
lower_limit = 1
upper_limit = 11
for i in range(lower_limit, upper_limit + 1):
    print(f" {num} * {i} = {i * num}", end=", \t")



#------------------------------------------------------------------------------------------------------------------------------

# dictionary comprehension

colours = [
    (0, "Red"),
    (1, "Green"),
    (2, "Blue")
]

colour_dict = {int(colour[0]): colour[1] for colour in colours}
# colour_dict = {0: 'Red', 1: 'Green', 2: 'Blue'}
your_colour = int(input("Enter your colour choice number: "))
if your_colour in colour_dict:
    print(colour_dict[your_colour])
else:
    print("Your colour does not exist!")



#------------------------------------------------------------------------------------------------------------------------------

# sum of var args 
# I have used add as my function just to make the distinction clearer.
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

nums = [1, 2, 3]
sol = add(*nums)
if sol == sum(nums):
    print("It works")
else:
    print("It failed")


#------------------------------------------------------------------------------------------------------------------------------

# I had practised some class related programs as well

#parent class
class Car:
    accelerate = 10

    def __init__(self):
        print("Car class object created")

    def acc(self):
        self.accelerate += 10
        print(f"acceleration = {self.accelerate}mph")

# is a relationship with car ( Honda is a Car )
class Honda(Car):
    def __init__(self):
        super().__init__()
        print("Honda class object created")

    def decelerate(self):
        self.accelerate -= 5
        print(f"decelrated: speed = {self.accelerate} mph")

#object of Honda named honda 
honda = Honda()
#parent class method
honda.acc()
honda.acc()
#child class method
honda.decelerate()
