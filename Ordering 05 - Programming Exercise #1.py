#Program's purpose is to take three integer values from the user input and display them in ascending order from least to greatest.
first_num = int(input(f'{"Please enter the first number:":<32}'))
second_num = int(input(f'{"Please enter the second number:":<32}'))
third_num = int(input(f'{"Please enter the third number:":<32}'))

#*#*# The if-elif-else structure checks the six different ways an integer can be listed from user input to display least to greatest

##If the first number is greater than the second number, first number is greater than the third number,
## and second number is greater than the third number.
if (first_num > second_num) and (first_num > third_num) and (second_num > third_num):

###Display the order to be third number, second number, and first number.
    print(f'\nThe ascending order is: {third_num}, {second_num}, {first_num}')

##Elif the first number is greater than the second number, first number is greater than the third number,
## and second number is less than the third number.
elif (first_num > second_num) and (first_num > third_num) and (second_num < third_num):

###Display the order to be second number, third number, and first number.
    print(f'\nThe ascending order is: {second_num}, {third_num}, {first_num}')

##Elif the first number is greater than the third number, first number is less than the second number,
## and second number is greater than the third number.
elif (first_num > third_num) and (first_num < second_num) and (second_num > third_num):

###Display the order to be third number, first number, and second number.
    print(f'\nThe ascending order is: {third_num}, {first_num}, {second_num}')

##Elif the first number is greater than the second number, first number is less than the third number,
## and second number is less than the third number.
elif (first_num > second_num) and (first_num < third_num) and (second_num < third_num):

###Display the order to be second number, first number, and third number.
    print(f'\nThe ascending order is: {second_num}, {first_num}, {third_num}')

##Elif the first number is less than the second number, first number is less than the third number,
## and second number is greater than the third number.
elif (first_num < second_num) and (first_num < third_num) and (second_num > third_num):

###Display the order to be first number, third number, and second number.
    print(f'\nThe ascending order is: {first_num}, {third_num}, {second_num}')

##Elif the first number is less than the second number, first number is less than the third number,
## and second number is less than the third number.
elif (first_num < second_num) and (first_num < third_num) and (second_num < third_num):

###Display the order to be first number, second number, and third number.
    print(f'\nThe ascending order is: {first_num}, {second_num}, {third_num}')

##Else if none of those conditions are met then display this message.
else:
    print('\nCannot display ascending order because the integers are the same or are not integers.')



    
    
