# Programs purpose is to calculate the minimum number of days required for a zombie population to
#  exceed a given threshold from user input.

# User input for the zombie threshold (Zth).
Zth = int(input("Zombie threshold (Zth): "))

# While-loop goes as long as the input is greater than or equal to zero.
while (Zth <= 0):
    print("\nPlease enter a number greater than zero.")
    Zth = int(input("\nZombie threshold (Zth): "))

# User input for the initial number of zombies (Z0).
Z0 = int(input("Zombies on Day 0 (Z0): "))

# While-loop goes as long as the input is greater than zero and less than or equal to Zth
while (Z0 <= 0) or (Z0 > Zth):
    # If-else structure determines the response based on if the input is greater than zero.
    if (Z0 <= 0):
        print("\nPlease enter a number greater than zero.")
    else:
        print("\nPlease enter a number less than or equal to the zombie threshold.")
    Z0 = int(input("\nZombies on Day 0 (Z0): "))

# User input for the zombie turn rate (Ztr).
Ztr = int(input("Zombie turn rate (Ztr): "))

# While-loop goes as long as the input is greater than or equal to zero.
while (Ztr <= 0):
    print("\nPlease enter a number greater than zero.")
    Ztr = int(input("\nZombie turn rate (Ztr): "))

# Ztn keeps track of the total number of zombies.
Ztn = Z0
# Zdn represents the number of newly created zombies per day.
Zdn = 0    

# Day counter.
day = 0 

# Displays the values for Day 0.
print("\nDay 0")
print("\tZ0 =", Z0)
print("\tZtn =", Ztn)

# While-loop determines the days required to exceed the threshold and this repeats until the
#  total number of zombies surpasses Zth.
while (Ztn <= Zth):
    Zdn = Ztn * Ztr # Calculates the new zombies created.
    Ztn += Zdn # Updates the number of total zombies.
    day += 1 # Increments the day counter from above.     
    
    # Displays the day number, new zombies created, and total zombies.
    print("\nDay", day)
    print("\tZ" + str(day) + " =", Zdn)
    print("\tZtn =", Ztn)

# If-else statement determines the singular or plural form of "zombie" and "day".
if (Zth == 1):
    zombie_word = "zombie"
else:
    zombie_word = "zombies"

if (day == 1):
    day_word = "day"
else:
    day_word = "days"

# Final output for the minimum days required to exceed the threshold.
print("\nThe minimum number of days to create more than", Zth, zombie_word, "is", day, day_word, ".")
