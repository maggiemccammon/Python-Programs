# Program reads two files with registered participants, one containing who registered
# and the other containing who completed the race out of those registered.
# The program uses two sets to find the one participant who registered but did not complete the race
# by adding names from each file to a set and then finding the difference. 

###

# Creates two empty sets where the names from the files will be assigned
registered_set = set()
completed_set = set()

###

# First try block starts with trying to open the registered participants file and traps for IOError
try:
    # Open the registered names file for reading
    registered_file = open('U11.2-RegisteredParticipants1.txt', 'r')

    # Read one line at a time from the registered names file
    for line in registered_file:
        name_reg = line.strip() # Removes whitespace on each line

        # Adds the names read from the file to the first set
        registered_set.add(name_reg)

    # Closes the file assigned to registered_file
    registered_file.close()

# Except traps for IOError if file cannot open
except IOError as error:
    print(error) # Prints the error contents

###

# Second try block starts with trying to open the completed participants file and traps for IOError
try:
    # Open the completed names file for reading
    completed_file = open('U11.2-CompletedParticipants1.txt', 'r')

    # Read one line at a time from the completed names file
    for line in completed_file:
        name_com = line.strip() # Removes whitespace on each line

        # Adds the names read from the file to the second set
        completed_set.add(name_com)

    # Closes the file assigned to completed_file
    completed_file.close()

# Except traps for IOError if file cannot open
except IOError as error:
    print(error) # Prints the error contents

###
    
# Finds the runner who did not complete the race
did_not_complete = registered_set - completed_set

# If statement checks if there is a runner who did not complete the race 
if did_not_complete:
    print(did_not_complete.pop()) # .pop() removes set and prints only the name

# Else statement prevents traceback error
else:
    print("Error") # Prints a message if a participant in not found
