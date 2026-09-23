# DICTIONARIES:
# QUESTION #1:
# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# Your code goes here:
phonebook.pop("Jill")
phonebook["Jake"] = 938273443
print(phonebook)




# QUESTION #2: Create a dictionary called aboutMe that contains the following keys and values: 
# name (which contains the value of your name)
# age (which contains the value of your age)
# favFood (which contains a list as its value of your favourite foods)
# hairColor (which contains the value of your hair color)
# favSubject (which contains your favourite subject)
# favSweet (which contains your favourite sweet to eat)
# favHobbies (which contains a list as its value of your favourite hobbies)
# likeCoding (which contains a bool, True if you like coding and False if you don’t like coding)
# Then, print aboutMe
Foods = [
    "Grilled cheese",
    "Pizza",
    "White rice",
    "Ground beef",
]
Hobbies = [
    "Drawing",
    "Coding",
    "Crafting",
]
aboutMe = {
    "name" : "Tylar",
    "age" : 15,
    "favFood" : Foods,
    "hairColor" : "brown",
    "favSubject" : "Programming",
    "favSweet" : "Chocolate",
    "favHobbies" : Hobbies,
    "likeCoding" : True
}
print(aboutMe)




# QUESTION #3: Create a dictionary called myPet that contains information about a pet that you want to adopt! 
# These are the keys:
# 1. name (which contains the value of your pets name)
# 2. breed (which contains the value of your pets breed)
# 3. age (which contains the value of your pets age)
# 4. noise (which contains the value of what noise your pet makes ex: woof or meow)
# 5. favActivity (which contains the value of your pets favourite activity)
# 5. favFood (which contains the value of your pets favourite food)

myPet = {
    "name" : "Gigi",
    "breed" : "Toy poddle",
    "age" : "6 years",
    "noise" : "woof",
    "favActivity" : "Playing",
    "favFood" : "Chicken",
}

# Then do the following:
# A. Print the dictionary
# B. Print the value of breed using the breed key
# C. Remove favFood and its value then print the dictionary
# D. Add one new key-value pair then print the dictionary
# E. Print the length of your dictionary
# F. Change the value of one existing value then print the dictionary
print(myPet)
print(myPet["breed"])
myPet.pop("favFood")
print(myPet)
myPet["size"] = "small"
print(len(myPet))
myPet["favActivity"] = "walking"
print(myPet)





# QUESTION #4: Create a dictionary called heights that 5 student names (keys) and their heights (values). 
# A. Print the dictionary
# B. Print the second value
# C. Remove the last key-value pair then print the dictionary
# D. Add one new key-value pair then print the dictionary
# E. Print the length of your dictionary
# F. Change the value of one existing value then print the dictionary
heights = {
    "Tylar" : "5ft 3in",
    "Adiel" : "5ft 3in",
    "Momina" : "5ft 3in",
    "Aniya" : "5ft 5in",
    "Leomar" : "5ft 9in"
}
print(heights)
print(heights["Adiel"])
heights.pop("Leomar")
print(heights)
heights["Terance"] = "5ft 9in"
print(heights)
print(len(heights))
heights["Terance"] = "5ft 11in"
print(heights)
