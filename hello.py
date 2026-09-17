#ask user for their
name = input("what is your name? ")

#remove whitespace from str and capitalize the user's name
name = name.strip().title()

#split user's name into first and last name
first, last = name.split(" ")

#say hello to user
print(f"Hello, {first}")