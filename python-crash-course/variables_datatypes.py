#Variables
message = "Hello Python Crash Course!"
print(message)

simple_message = "Store a message in a variable, and then print that message."
print(simple_message)
simple_messages = "Store a message in a variable, and print that message. Then Change the value of your variable to a new message."
print(simple_messages)
simple_messages = "New message"
print(simple_messages)

#Strings
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#Combining or Concatenating String
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")


#Adding whitespace to String with Tabs or Newlines
print("This is Python")
print("\tThis is Python")
print("Languages: \nPython\nJavaScript\nRust")

#Stripping Whitespace
favorite_language = " python "
print(favorite_language)
print(favorite_language.strip())

#You can also strip whitespace from the left side of a string using the lstrip()
# right side of a string using the rstrip()
favorite_language = " python"
print(favorite_language.lstrip())
favorite_language = "python "
print(favorite_language.rstrip())

famous_quote = "Albert Einstein once said, 'A person who never made a\nmistake never tried anything new.'"
print(famous_quote)

#Numbers
integer_1 = 2+3
integer_2 = 4+2*4/2
integer_3 = 3**2
print(integer_1)
print(integer_2)
print(integer_3)

#Floats
float_1 = 0.1 + 0.1
float_2 = 0.2 + 0.5
print(float_1)
print(float_2)




