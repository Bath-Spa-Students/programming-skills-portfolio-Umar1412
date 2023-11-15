# Tidy up the code to make it easier to understand

# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

# Print the name once, so the whitespace around the name is displayed. 

# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

# Using a variable to represent a name.
name = ("\t Umar Asif \n")

# Printing the name with no changes.
print("Name with no changes:")
print(name)

#Printing the name with lstrip.
print ("\nlstrip():")
print(name.lstrip())

# Printing the name with rstrip.
print ("\nrstrip():")
print(name.rstrip())

#Printing the name with nstrip.
print ("\nstrip():")
print(name.strip())
