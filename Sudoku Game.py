# Purpose of program is to read a 16x16 Sudoku grid from a text file and verify whether
##  it is a valid Sudoku solution based on three constraints:

### 1) Each row contains 16 values which are not duplicated
### 2) Each column contains 16 values which are not duplicated
### 3) Each 4x4 boc contains 16 values which are not duplicated

import grid_util

BOX_SIZE = 4
GRID_SIZE = BOX_SIZE ** 2

# Defines the function that checks if grid follows the row, column, and box rules
def grid_valid(grid):

    # Assumes grid is true unless constraints are violated 
    is_valid = True

### Row check

    # Initial row index
    row_position = 0
    
    # While-loop is checking each row for duplicates
    while (row_position < GRID_SIZE):

        # Initial column index
        value_position = 0 

        # While_loop loops through each value in row
        while (value_position < GRID_SIZE):
            # Gets current value by indexing into the list
            value = grid[row_position][value_position] 

            # Initial new counter that checks rows from beginning
            check_position = 0

            # Initial count variable
            count = 0
            
            # While-loop counts how many times the value found appears in the current row
            while (check_position < GRID_SIZE):
                # If statement compares the current value with each value in row
                if grid[row_position][check_position] == value:
                    # If a match is found the count increases by one for that value
                    count = count + 1

                # Moves to the next position in row
                check_position = check_position + 1

            # If current value appears more than once in a row then it will be invalid
            if (count > 1):
                # Output saying if row is invalid
                print("Invalid row.")

                # Sets the grid to false
                is_valid = False

                # Exit for the current row value loop 
                value_position = GRID_SIZE
            else:
                # Otherwise moves to the next value in the row if there is no duplicate
                value_position = value_position + 1

        # Moves to the next row after checking the current row
        row_position = row_position + 1

### Column check

    # Initial column index 
    column_position = 0

    # While-loop goes through each column in the grid
    while (column_position < GRID_SIZE):

        # Start at the top of the column to check each value
        row_position = 0

        # While-loop goes down each row for a specific column
        while (row_position < GRID_SIZE):

            # Get the current value in the column by indexing
            value = grid[row_position][column_position]

            # Initialize counter for how many times this value appears in the column
            check_position = 0
            count = 0

            # Check every row in the column to count how many times the value appears
            while (check_position < GRID_SIZE):
                # Compare the value to each row element in the current column
                if grid[check_position][column_position] == value:
                    # If a match is found, increase the count
                    count = count + 1

                # Move to the next row in the column
                check_position = check_position + 1

            # If the value appears more than once in the column, it's invalid
            if (count > 1):
                # Output saying if column is invalid
                print("Invalid column.")

                # Set the grid to false
                is_valid = False

                # Exit column check early by setting row_position to max
                row_position = GRID_SIZE
            else:
                # Otherwise continue to the next row in the column
                row_position = row_position + 1

        # Move to the next column after checking the current one
        column_position = column_position + 1

### Box check

    # Sets the starting row index for the box (0, 4, 8, 12)
    box_row = 0

    # Loops through each horizontal layer of boxes (top to bottom)
    while (box_row < GRID_SIZE):

        # Sets the starting column index for the box (0, 4, 8, 12)
        box_column = 0

        # Loops through each vertical group of boxes (left to right)
        while (box_column < GRID_SIZE):

            # Create an empty list to teack values already seen in 4x4 box
            seen_values = []
            
            # Sets the row offset within the current 4x4 box (0 to 3)
            box_row_offset = 0

            # Loops through each row inside the current 4x4 box
            while (box_row_offset < BOX_SIZE):

                # Sets the column offset within the current 4x4 box (0 to 3)
                box_column_offset = 0

                # Loops through each column inside the current 4x4 box
                while (box_column_offset < BOX_SIZE):

                    # Gets the current value in the box using the row and column offsets
                    value = grid[box_row + box_row_offset][box_column + box_column_offset]

                    # Initializes an index to loop through the list of already seen values
                    check_index = 0

                    # Initializes a flag to track if a duplicate value is found in the current box
                    duplicate_found = False

                    # While-loop goes through each value already seen in this 4x4 box
                    while (check_index < len(seen_values)):

                        # If the current value is equal to one already in the seen list, it's a duplicate
                        if seen_values[check_index] == value:
                            # Sets the duplicate flag to True if match is found
                            duplicate_found = True

                        # Moves to the next index in the seen_values list
                        check_index = check_index + 1

                    # If a duplicate value was found in the box, it's an invalid box
                    if (duplicate_found):
                        # Prints message for invalid box
                        print("Invalid box.")

                        # Sets the overall grid validity to false
                        is_valid = False

                        # Exits both offset loops by setting them to their limits
                        box_row_offset = BOX_SIZE
                        box_column_offset = BOX_SIZE

                    else:
                        # If no duplicate found, add value to the seen list for this box
                        seen_values.append(value)
                        
                        # Moves to the next column offset in the box
                        box_column_offset = box_column_offset + 1

                # Moves to the next row offset only if not skipped
                if (box_column_offset == BOX_SIZE):
                    box_row_offset = box_row_offset + 1

            # Moves to the next 4x4 box horizontally
            box_column = box_column + BOX_SIZE

        # Moves to the next 4x4 box vertically
        box_row = box_row + BOX_SIZE
                   
    return is_valid
    
def main():

    # Opens the file containing the Sudoku grid data
    sudoku_file = open("Invalid_Sudoku_Grid__Boxes__INCORRECT2.txt", "r")

    # Creates an empty list to store the 2D Sudoku grid
    grid = []

    # Reads the first line from the file
    line = sudoku_file.readline()

    # While-loop reads each line from the file until no more lines remain
    while (line != ""):
        
        # Removes any newline character and splits the line into a list of values
        row = line.strip().split(",")

        # Adds the list of values (row) to the grid list
        grid.append(row)

        # Reads the next line in the file
        line = sudoku_file.readline()

    # Closes the file after all lines have been read
    sudoku_file.close()

    
    if (grid_util.check_grid(grid)):
        print(grid_util.print_grid(grid))

        if (grid_valid(grid)):
            print("\nThis is a valid Sudoku solution.")
        else:
            print("\nThis is an invalid Sudoku solution.")
    else:
        print("Invalid grid.")    


    return


main()
