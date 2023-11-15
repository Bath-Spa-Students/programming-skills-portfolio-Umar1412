# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

# * Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

# * Use a loop to print the name of each river included in the dictionary.

# * Use a loop to print the name of each country included in the dictionary.


# Dictionary containing three major rivers.

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'amazon': 'brazil',
    }

# Using a loop to print a sentence about each river running through the country.

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Using a loop to print the name of each river stored in dictionary.

print("\nThese rivers are included in this dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")

# Using a loop to print the name of each country stored in dictionary. 

print("\nThese countries are included in this dictionary:")
for country in rivers.values():
    print(f"- {country.title()}")

