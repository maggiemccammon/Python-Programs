#Program's purpose is to generate an itemized bill for a group of people at a restaurant, and determining the total amount of the bill with tax included based on the number of people in the group.
infile = open("U3.1-Data5.txt", "r")

dollar_amount = float(input("Enter the amount of the gift certificate: $"))
tax_rate = float(input("Enter the tax rate as a percentage (e.g., 7.75): "))

line_read = infile.readline()
number_people = int(line_read)

counter = 0
total_amount = 0
total_amount_everyone = 0

while counter < number_people:
    print("\nItems ordered for person", counter + 1)

    line_read = infile.readline()
    appetizer_amount = float(line_read)
    print(f'Appetizer: ${appetizer_amount:.2f}')
    
    line_read = infile.readline()
    entree_amount = float(line_read)
    print(f'Entree: ${entree_amount:.2f}')
    
    line_read = infile.readline()
    drinks_amount = float(line_read)
    print(f'Drinks: ${drinks_amount:.2f}')

    line_read = infile.readline()
    dessert_amount = float(line_read)
    print(f'Dessert: ${dessert_amount:.2f}')

    total_amount = appetizer_amount + entree_amount + drinks_amount + dessert_amount
    total_amount_everyone += total_amount

    counter += 1
#what originally had from stem lab: print(f'\nTotal cost of items ordered for person {counter}: ${total_amount:.2f}')
    print('\nTotal cost of items ordered for person', end=' ')
    print(counter, end='')
    print(f': ${total_amount:.2f}')

infile.close()

print(f'\nTotal cost of items ordered for the group: ${total_amount_everyone:.2f}')

calculated_tax_rate = total_amount_everyone * tax_rate / 100
total_tax_everyone = total_amount_everyone + calculated_tax_rate

print(f'Total cost of items ordered for the group including tax: ${total_tax_everyone:.2f}')

total_bill_giftcard = total_tax_everyone - dollar_amount

print(f'Total bill after applying the gift certificate: ${total_bill_giftcard:.2f}')

print("(negative amount indicates unused amount of gift certificate)")
                      
