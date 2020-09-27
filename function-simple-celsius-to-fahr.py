def say_hello(person):
    print("Hello! " + person + ", how are you?")

def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius

print( "Celsius: ", round (fahr2celsius(100),2)) 
print( "Kelvin: ", round (fahr2celsius(100) + 273.5 ,2))


