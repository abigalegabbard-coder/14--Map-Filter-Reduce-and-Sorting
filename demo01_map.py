"""
The map() function is used to apply a given function to every item in a collection
(collections: list, tuple, set, dictionary)
"""

celsius_temps = [0,10,20,30,40]

# Convert these all to a list of Fehrenheit
# (c * 9/5) + 32

def c_to_f(temp):
    return (temp*9/5)+32

fahrenheit_temps = map(c_to_f, celsius_temps) #runs c_to_f on each thing in celsius_temps
print(fahrenheit_temps) #map object
#convert map object to a list
print(list(fahrenheit_temps))

# Do the same thing but with a Lambda:
fahrenheit_temps2 = map(lambda temp: (temp* 9/5) + 32, celsius_temps)
print(fahrenheit_temps2) #map object
fahrenheit_temps2 = list(fahrenheit_temps2)

"""
Why would we use map?
- save time, no need for long for loops
- cleaner code
- works great with lambda
- efficient
"""

names = [
    {"fname": "frank", "lname": "williams", "age": 52},
    {"fname": "david", "lname": "smith", "age": 15},
    {"fname": "jace", "lname": "larkin", "age": 16},
    {"fname": "k", "lname": ",uh", "age": 103},
    {"fname": "duane", "lname": "olesnanik", "age": 31}
]

# Without list comprehension: Map these names to be lastnameFirstInitial, zero padded age (52 052), if age were 7, 007
#eg. williamsf052
codes = list(map(lambda dict: f"{dict["lname"]}{dict["fname"][0]}{str(dict["age"]).rjust(3,"0")}",names))
print(f"Duanes: {codes}")

def func(ell):
    return ell.get("lname")+ell.get("fname")[0]+(str(ell.get("age")).rjust(3,"0"))
aaaa = map(func,names )
print(f"Mykyta's: {list(aaaa)}")

print("Map object looped through: ")
for item in aaaa:
    print(item)