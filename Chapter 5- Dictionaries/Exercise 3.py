# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

# calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

# to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.


# Replacing series of print with loop and adding five more programming words.

glossary = {
    'comment': 'Comments in Python are the lines in the code that are ignored by the interpreter during the execution of the program.',
    'string': 'A string is a data type in Python, composed of a collection of characters.',
    'integer': 'A whole number, positive or negative, without decimals, of unlimited length.',
    'variable': 'A reserved memory location to store values.',
    'list': 'An ordered and changeable collection of data objects.',
    'dictionary': 'A collection of key-value pairs.',
    'float': 'A function or reusable code in the Python programming language that converts values into floating point numbers.',
    'input': 'The input function converts whatever you enter as an input into a string.',
    'print': 'Prints the specified message to the screen, or other standard output device.',
    'loop': 'Repeating something over and over until a particular condition is satisfied.',
}

# Replaced the print series with a loop before adding the five more words.

for program_word, definition in glossary.items():
    print(f"\n{program_word.title()}: {definition}")