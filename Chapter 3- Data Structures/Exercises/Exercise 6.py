# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

# •Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

# •Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

# •Print a message to each of the two people still on your list, letting them know they’re still invited.

# •Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guest_list = ['Faisal', 'Wathila', 'Saeed']

print(f"{guest_list[0].title()}, you are invited to attend my dinner.")

print(f"{guest_list[1].title()}, you are invited to attend my dinner.")

print(f"{guest_list[2].title()}, you are invited to attend my dinner.")

print(f"\nSorry, {guest_list[2].title()} can't attend the dinner. ")

del(guest_list[2])
guest_list.insert(2, 'Ali')

print(f"\n{guest_list[0].title()}, you are invited to attend my dinner.")

print(f"{guest_list[1].title()}, you are invited to attend my dinner.")

print(f"{guest_list[2].title()}, you are invited to attend my dinner.")

print("\nSorry, We are only able to invite two people to dinner") 
print("due to our new dinner table not arriving in time.")

print(f"\nSorry, {guest_list.pop().title()} there's no place at the dining table.")

print(f"\n{guest_list[0].title()}, you are still invited to attend my dinner.")

print(f"{guest_list[1].title()}, you are still invited to attend my dinner.")

del(guest_list[0])
del(guest_list[0])

print(guest_list)

