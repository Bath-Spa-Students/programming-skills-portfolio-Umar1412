# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 

# should print a sentence summarizing the size of the shirt and the message printed on it. 

# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.


# Adding a function called make_shirt() accepting two texts.
def make_shirt(size, message):
    """Summarizing the information of the shirt being made."""

# Printing the size and message on the shirt.
    print(f"\nI will make a {size} t-shirt.")
    print(f'The message printed on the shirt will be, "{message}"')
    
# Calling the function using positional arguments.
make_shirt('medium', 'Itachi Uchiha!')

# Calling the function using keyword arguments.
make_shirt(message="Winter Szn.", size='small')