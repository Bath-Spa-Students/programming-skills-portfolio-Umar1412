# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; 

# if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 

# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.


# Set up the initial prompt for the user to enter their age.
user_prompt = "What is your age?"
user_prompt += "\nEnter 'quit' when you are finished. "

# Start an infinite loop to continuously ask for the user's age.
while True:
    # Ask the user to enter their age.
    age_input = input(user_prompt)

    # Check if the user wants to quit.
    if age_input == 'quit':
        break

    # Convert the age input to an integer.
    age = int(age_input)

    # Calculate the price of the ticket according to the user's age.
    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")