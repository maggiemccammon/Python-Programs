# Program reads two files with registered participants, one containing who registered
# and the other containing who completed the race out of those registered.
# The program uses a dictionary to find how many times each name appears, 
# and then finds out who did not complete the race.

###

# Set up an empty dictionary which will store the registered names, and how many times they appear
registered_dict = {}

###

# First try block starts with trying to open the registered participants file and traps for IOError
try:
    # Open the registered names file for reading
    registered_file = open('U11.1-RegisteredParticipants1.txt', 'r')

    # Read one line at a time from the registered names file
    for line in registered_file:
        name_reg = line.strip() # Removes whitespace on each line

        # If the names read from the file are in the dictionary, increase the count by 1
        if name_reg in registered_dict:
            registered_dict[name_reg] += 1 # Increment count for this name
            
        # Else the name is not in the dictionary, add it with starting count of 1
        else:
            registered_dict[name_reg] = 1 # Name appears for first time

    # Closes the file assigned to registered_file
    registered_file.close()

# Except traps for IOError if file cannot open
except IOError as error:
    print(error) # Prints the error contents

###

# Second try block starts with trying to open the completed participants file and traps for IOError
try:
    # Open the completed names file for reading
    completed_file = open('U11.1-CompletedParticipants1.txt', 'r')

    # Read one line at a time from the completed names file
    for line in completed_file:
        name_com = line.strip() # Removes whitespace on each line

        # If the names read from the file are in the dictionary, subtract 1 from the count
        if name_com in registered_dict:
            registered_dict[name_com] -= 1 # Decrease count for this name

    # Closes the file assigned to completed_file
    completed_file.close()

# Except traps for IOError if file cannot open
except IOError as error:
    print(error) # Prints the error contents

###

# Loops through the dictionary to find the participant that did not complete the race
for name in registered_dict:
    # Check if the name count is one within the dictionary
    if registered_dict[name] == 1:
        print(name) # Prints the name of the participant who did not complete the race





    
