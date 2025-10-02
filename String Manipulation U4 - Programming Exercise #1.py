#Program's purpose is to take a string of letter combinations ('UWXZ') from a file, transform the
#  letters to display a new message, and display the amount of each letter in that new message.
index = 0
new_message = ''

infile = open("U4.1-Data1.txt", "r")
line = str(infile.readline().strip())

print("Original message =", line)
#The while loop takes all characters from the string read from the file (line), finds the length, and continues until the string ends 
while index < len(line):
    all_char = line[index]
    #The if-elif-else structure transforms each letter based on information John noted from the gadget
    if all_char == 'U': #If one of the characters read from the string is 'U'
        new_message += 'W' #It changes the 'U' to 'W' for the new message
    elif all_char == 'W': #If one of the characters read from the string is 'W'
        new_message += 'WU' #It changes the 'W' to 'WU' for the new message
    elif all_char == 'X': #If one of the characters read from the string is 'X'
        new_message += 'Z' #It changes the 'X' to 'Z' for the new message
    elif all_char == 'Z': #If one of the characters read from the string is 'Z'
        new_message += 'ZX' #It changes the 'Z' to 'ZX' for the new message
    else: #Else it is not one of the letters used so
        new_message += all_char #The new message displays the original string 

    index += 1 

print("New message =", new_message)
#Takes each letter from the new_message string and counts using the .count from unit 4 in zyBooks, and assigns to a variable
char_u = new_message.count('U')
char_w = new_message.count('W')
char_x = new_message.count('X')
char_z = new_message.count('Z')
#Prints out the number of each letter according to assigned variable listed above
print("\nNumber of \'U\'s =", char_u)
print("Number of \'W\'s =", char_w)
print("Number of \'X\'s =", char_x)
print("Number of \'Z\'s =", char_z)

infile.close()
