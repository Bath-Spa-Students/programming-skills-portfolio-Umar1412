# A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

# You will to use the arithmetic operators to complete this exercise.


# Adding a variable with the cost of the usb.
usb_stick = 6

# Total budget
total_budget = 50

# Calculate how many usbs she can buy
number_usbsticks = total_budget // usb_stick

# Calculate the remaining money she will have left.
remaining = total_budget % usb_stick

# Print the results
print(f"With £{total_budget}, she can purchase {number_usbsticks} usb sticks.")
print(f"She will have £{remaining} left.")

