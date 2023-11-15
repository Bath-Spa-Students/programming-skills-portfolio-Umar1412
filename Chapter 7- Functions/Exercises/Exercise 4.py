# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 

# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


# Modify the function by adding a custom size and message so that they are set by default.
def make_shirt(size='large', message ='I love Python'):
    """Summarizing the information of the shirt being made."""

# Printing the size and message on the shirt.
    print(f"\nI will make a {size} t-shirt.")
    print(f'The message printed on the shirt will be, "{message}"')

# Making a large and medium shirt with the default message and then changing it to a new custom message.
make_shirt()

make_shirt(size='medium')

make_shirt('small','boogie') 