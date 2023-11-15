# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

# print a message saying you’ll add that topping to their pizza.


# Set up the initial prompt for the user to choose pizza toppings.

user_prompt = "\nPlease choose a topping for your pizza."
user_prompt += "\nEnter 'quit' when you have made your selection: "

# Start an infinite loop to continuously ask for pizza toppings.

while True:

    # Ask the user to enter a topping.

    user_input = input(user_prompt)

    # Check if the user wants to quit.

    if user_input != 'quit':

        # Print a message confirming the selected topping.

        print(f"  Adding {user_input} to your pizza.")

    else:

        # Exit the loop if the user enters 'quit'.

        break