# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

# near the beginning of your program to print a message saying the deli has run out of pastrami, 

# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.



# Adding Pastrami in the same list from the previous exercise

sandwich_orders = ['Pastrami Sandwich', 'Nutella Sandwich', 'Pastrami Sandwich', 'Egg Sandwich', 'Ham Sandwich', 'Pastrami Sandwich', 'Grilled Chicken Sandwich']

finished_sandwiches = []

# Printing the message saying the deli has run out of pastrami
print("Sorry, the deli has run out of Pastrami.")

# Removing all instances of 'Pastrami Sandwich' from the list
while 'Pastrami Sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami Sandwich')

print("\n")

# Making sandwiches from the remaining orders
while sandwich_orders:

    # Pop the last sandwich order from the list
    current_sandwich = sandwich_orders.pop()

    # Print a message showing that the current sandwich is being made
    print(f"I am making your {current_sandwich}")

    # Add the current sandwich to the finished_sandwiches list
    finished_sandwiches.append(current_sandwich)

print("\n")

# Print a message for each finished sandwich
for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}")