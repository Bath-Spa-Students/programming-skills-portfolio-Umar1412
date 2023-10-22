# Think of at least five places in the world you’d like to visit.

# • Store the locations in a list. Make sure the list is not in alphabetical order.

# • Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

# • Use sorted() to print your list in alphabetical order without modifying the actual list.

# • Show that your list is still in its original order by printing it.

# • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

# • Show that your list is still in its original order by printing it again.

# • Use reverse() to change the order of your list. Print the list to show that its order has changed.

# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

# • Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

dream_locations = ['New York', 'London', 'Abu Dhabi', 'Manchester', 'Oslo']

# Printing my list in the original order

print("Original order:")
print(dream_locations)

# Printing my list in an Alphabetical order

print("\nAlphabetical order:")
print(sorted(dream_locations))

# Printing my list in the original order

print("\nOriginal order:")
print(dream_locations)

# Printing my list in reverse alphabetical order 

print("\nReverse alphabeticial order:")
print(sorted(dream_locations, reverse=True))

# Printing the list in the original order

print("\nOriginal order:")
print(dream_locations)

# Printing my list in a reversed order

print("\nReversed order:")
dream_locations.reverse()
print(dream_locations)

# Printing my list using reverse again to return it to the original order

print("\nOriginal order:")
dream_locations.reverse()
print(dream_locations)

# Printing my list and storing in Alphabetical order

print("\nAlphabetical order:")
dream_locations.sort()
print(dream_locations)

# Printing my list and storing it in Reverse alphabetical order

print("\nReverse Alphabetical order:")
dream_locations.sort(reverse=True)
print(dream_locations)
