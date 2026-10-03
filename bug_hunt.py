count = 1
total = 0

# BUG: Added a colon after the while condition to fix the syntax error.
while count <= 5:
    # BUG: Fixed the indentation so the statements are inside the while loop.
    total = total + count
    count = count + 1

# BUG: Converted total to a string so it can be joined with the message.
print("Sum of 1 to 5 is: " + str(total))
