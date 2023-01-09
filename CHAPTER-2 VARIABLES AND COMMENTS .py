##1.Assign a message to a variable, and print that message.
# msg = "Hi My name is Lateef and i am new to python language."
# print(msg)

##1.1.Then change the value of the variable to a new message, and print the new
# msg = "I love studying python language because it is user friendly and easy to learn and understand"
# print(msg)

##2.Find a quote from a famous person you admire. Print the quote and the name of its author.
# Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.
# msg = input("Don't get high temprature, keep it room temprature - Aiman")
# print(msg) # prints the message

##3.Tidy up the code to make it easier to understand
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, “\t” and “\n”, at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

# n = "\t Lateef \n" # using \t to give a tab space and \n to print the name in a newline
# print(n) # printing the name 
# print(n.lstrip()) # prints n in lstrip
# print(n.rstrip()) # prints n in rstrip
# print(n.strip()) #prints n in strip

##4.Use a variable to represent your favorite number. Then,using that variable, create a message that reveals your favorite number. Print that message.
# favorite_number = 69  # This is my favorite number
# # Create a message using the favorite_number variable
# message = f"My favorite number is {favorite_number}."
# # Print the message
# print(message)

##5.A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
# You will to use the arithmetic operators to complete this exercise.
# price_per_usb_stick = 6  # price of each USB stick in pounds
# budget = 50  # amount of money the girl has in pounds

# # Calculate how many USB sticks the girl can buy
# num_usb_sticks = budget // price_per_usb_stick

# # Calculate how much money the girl has left
# remaining_budget = budget % price_per_usb_stick

# # Print the results
# print(f"The girl can buy {num_usb_sticks} USB sticks.")
# print(f"She will have {remaining_budget} pounds left.")