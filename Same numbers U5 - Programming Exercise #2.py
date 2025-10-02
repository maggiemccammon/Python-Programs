#Program's purpose is to take five integer values from user input and determine if there are at least three that are the same.
first_num = int(input(f'{"Please enter the first number:":<32}'))
second_num = int(input(f'{"Please enter the second number:":<32}'))
third_num = int(input(f'{"Please enter the third number:":<32}'))
fourth_num = int(input(f'{"Please enter the fourth number:":<32}'))
fifth_num = int(input(f'{"Please enter the fifth number:":<32}'))

#If there are at least three integers that are the same, a message will be displayed confirming the statement.
##The if-elif-else structure checks each condition that determines if the statement above is true.

###If the first number is equal to the second number and equal to the third number
#display at least three integers are the same

###elif the first number is equal to the second number and equal to the fourth number
#display at least three integers are the same

###elif the first number is equal to the second number and equal to the fifth number
#display at least three integers are the same

###elif the first number is equal to the third number and equal to the fourth number
#display at least three integers are the same

###elif the first number is equal to the third number and equal to the fifth number
#display at least three integers are the same

###elif the first number is equal to the fourth number and equal to the fifth number
#display at least three integers are the same

###elif the second number is equal to the third number and equal to the fourth number
#display at least three integers are the same

###elif the second number is equal to the third number and equal to the fifth number
#display at least three integers are the same

###elif the second number is equal to the fourth number and equal to the fifth number
#display at least three integers are the same

###elif the third number is equal to the fourth number and equal to the fifth number
#display at least three integers are the same

##Otherwise(else), the statement that prints determines there are NOT at least three integers that are the same.

if (first_num == second_num) and (first_num == third_num):
    print('\nThere are at least three numbers that are the same.')

elif (first_num == second_num) and (first_num == fourth_num):
    print('\nThere are at least three numbers that are the same.')

elif (first_num == second_num) and (first_num == fifth_num):
    print('\nThere are at least three numbers that are the same.')

elif (first_num == third_num) and (first_num == fourth_num):
    print('\nThere are at least three numbers that are the same.')

elif (first_num == third_num) and (first_num == fifth_num):
    print('\nThere are at least three numbers that are the same.')

elif (first_num == fourth_num) and (first_num == fifth_num):
    print('\nThere are at least three numbers that are the same.')

elif (second_num == third_num) and (second_num == fourth_num):
    print('\nThere are at least three numbers that are the same.')

elif (second_num == third_num) and (second_num == fifth_num):
    print('\nThere are at least three numbers that are the same.')

elif (second_num == fourth_num) and (second_num == fifth_num):
    print('\nThere are at least three numbers that are the same.')

elif (third_num == fourth_num) and (third_num == fifth_num):
    print('\nThere are at least three numbers that are the same.')

else:
    print('\nThere are NOT at least three numbers that are the same.')

    
    

    

    
