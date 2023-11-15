# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. 

# Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet.



# Creating an empty list to store information about pets.

pets = []

# Define and store information about a dog pet.

dog = {
    'animal': 'dog',
    'name': 'rocket',
    'owner': 'mark',
    'age': 3,
}
pets.append(dog)

# Define and store information about a cat pet.

cat = {
    'animal': 'cat',
    'name': 'luna',
    'owner': 'jake',
    'age': 2,
}
pets.append(cat)

# Define and store information about a horse pet.

horse = {
    'animal': 'horse',
    'name': 'ryan',
    'owner': 'john',
    'age': 5,
}
pets.append(horse)

# Printing the information about each pet.

for pet in pets:
    print(f"\nInformation about the pet {pet['animal'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
