def say_hello(person1, person2):
    print("Hello! " + person1 +  ", how are you? " + person2 + " is waiting for you.")
 
def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius
say_hello("Jane" , "Tim")

################

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


