TAB_SPACING = 3

BOX_SIZE = 4
GRID_SIZE = BOX_SIZE ** 2
GAPS_PER_BOX = 5

UPPER_LEFT_CORNER_BRACKET = "\u250C"
UPPER_RIGHT_CORNER_BRACKET = "\u2510"
LOWER_LEFT_CORNER_BRACKET = "\u2514"
LOWER_RIGHT_CORNER_BRACKET = "\u2518"

HORIZONAL_BAR = "\u2500"
VERTICAL_BAR = "\u2502"

VERTICAL_BAR_RIGHT_CONNECTOR = "\u251C"
VERTICAL_BAR_LEFT_CONNECTOR = "\u2524"
HORIZONAL_BAR_BOTTOM_CONNECTOR = "\u252C"
HORIZONAL_BAR_TOP_CONNECTOR = "\u2534"

CROSS_CONNECTOR = "\u253C"


def check_grid(grid):
    is_valid = True
    
    if (len(grid) != GRID_SIZE):
        is_valid = False
        
    else:
        grid_length = len(grid)
        done = False
        row = 0
        
        while not done:
            if (len(grid[row]) != GRID_SIZE):
                done = True
                is_valid = False
                
            elif (row < GRID_SIZE - 1):
                row += 1
                
            else:
                done = True

        if (is_valid):
            row = 0
            done = False
            
            while not done and row < GRID_SIZE:
                col = 0
                
                while not done and col < GRID_SIZE:
                    cell = grid[row][col]

                    if (len(cell) != 1):
                        done = True
                        is_valid = False
                        
                    elif (not cell.isalnum() or (cell.isdigit() and cell == "0")
                            or (cell.isalpha() and (cell.islower() or cell.upper() > "G"))):
                        done = True
                        is_valid = False

                    else:
                        col += 1

                row += 1
                
                
    return is_valid


def print_grid(grid):
    grid_or_message = UPPER_LEFT_CORNER_BRACKET
    
    for i in range(BOX_SIZE):
        for j in range(GAPS_PER_BOX * TAB_SPACING + BOX_SIZE):
            grid_or_message += HORIZONAL_BAR

        if (i != BOX_SIZE - 1):
            grid_or_message += HORIZONAL_BAR_BOTTOM_CONNECTOR
            
    grid_or_message += UPPER_RIGHT_CORNER_BRACKET + "\n"
    
    for i in range(GRID_SIZE):
        grid_or_message += VERTICAL_BAR + "\t".expandtabs(TAB_SPACING)
        
        for j in range(GRID_SIZE):
            grid_or_message += grid[i][j] + "\t".expandtabs(TAB_SPACING)
            
            if (j % BOX_SIZE == BOX_SIZE - 1):
                grid_or_message += VERTICAL_BAR + "\t".expandtabs(TAB_SPACING)
                
        grid_or_message += "\n"
        
        if (i % BOX_SIZE == BOX_SIZE - 1 and i != GRID_SIZE - 1):
            grid_or_message += VERTICAL_BAR_RIGHT_CONNECTOR
            
            for k in range(BOX_SIZE):
                for l in range(GAPS_PER_BOX * TAB_SPACING + BOX_SIZE):
                    grid_or_message += HORIZONAL_BAR
                    
                if (k != BOX_SIZE - 1):
                    grid_or_message += CROSS_CONNECTOR
                       
            grid_or_message += VERTICAL_BAR_LEFT_CONNECTOR + "\n"
            
    grid_or_message += LOWER_LEFT_CORNER_BRACKET
    
    for i in range(BOX_SIZE):
        for j in range(GAPS_PER_BOX * TAB_SPACING + BOX_SIZE):
            grid_or_message += HORIZONAL_BAR
            
        if (i != BOX_SIZE - 1):
            grid_or_message += HORIZONAL_BAR_TOP_CONNECTOR
            
    grid_or_message += LOWER_RIGHT_CORNER_BRACKET
    
    
    return grid_or_message
