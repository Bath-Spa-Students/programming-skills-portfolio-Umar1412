# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# * Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.

# * Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, 

# or print the word on one line and then print its meaning indented on a second line. 

# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.


# Storing the information of the five programming words in a dictionary.

glossary = {
    'comment': 'Comments in Python are the lines in the code that are ignored by the interpreter during the execution of the program.',
    'string': 'A string is a data type in Python, composed of a collection of characters.',
    'integer': 'A whole number, positive or negative, without decimals, of unlimited length.',
    'variable': 'A reserved memory location to store values.',
    'list': 'An ordered and changeable collection of data objects.',
}

# Printing each word with its meaning, and using newline character to insert a blank line between them.

program_word = 'comment'
print(f"\n{program_word.title()}: {glossary[program_word]}")

program_word = 'string'
print(f"\n{program_word.title()}: {glossary[program_word]}")

program_word = 'integer'
print(f"\n{program_word.title()}: {glossary[program_word]}")

program_word = 'variable'
print(f"\n{program_word.title()}: {glossary[program_word]}")

program_word = 'list'
print(f"\n{program_word.title()}: {glossary[program_word]}")