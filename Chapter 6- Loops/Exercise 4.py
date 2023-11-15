# Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 

# move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.


# Creating a list which stores the names of various sandwiches.
sandwich_orders = ['Nutella Sandwich', 'Egg Sandwich', 'Ham Sandwich', 'Grilled Chicken Sandwich']

# Creating an empty list.
finished_sandwiches = []

# Handle each order for a sandwich and pop the last sandwich from the list.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    # Print a message telling the customer that the sandwich is being made.
    print(f"I am making your {current_sandwich} ")

    # Adding the finished sandwich to the finished_sandwiches list.
    finished_sandwiches.append(current_sandwich)

# Print a message for each completed sandwich.
print("\n")
for sandwich in finished_sandwiches:
    print(f"I made your {sandwich} ")