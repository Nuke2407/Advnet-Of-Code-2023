from pathlib import Path 

path = Path("Engine_Schematic.txt").read_text().splitlines()

grid = [list(line) for line in path]
total = 0 


for row_index, row in enumerate(grid):
    for column_index, value in enumerate(row):
        if value == '*':  
            num_1 = 0 
            num_2 = 0
            for row_finder in [-1,0,1]:
                for column_finder in [-1,0,1]:
                    local_row = row_index + row_finder
                    local_column = column_index + column_finder
                    if 0 <= local_row < len(grid) and 0 <= local_column < len(row):
                        if grid[local_row][local_column].isnumeric():

                            while local_column + 1 < len(row) and grid[local_row][local_column + 1].isnumeric():
                                local_column += 1
                            
                            numbers = []
                            numbers.append(grid[local_row][local_column])
                            grid[local_row][local_column] = '.'
                        
                            while local_column - 1 >= 0 and grid[local_row][local_column - 1].isnumeric():
                                local_column -= 1
                                numbers.append(grid[local_row][local_column])
                                grid[local_row][local_column] = '.'

                            numbers.reverse() 

                            final_number = ""
                            for num in numbers:
                                final_number += num

                            if num_1 == 0:
                                num_1 = int(final_number)
                            elif num_1 != 0:
                                num_2 = int(final_number)
                            else:
                                num_1 = 0
                                num_2 = 0

            final = num_1 * num_2
            total += final

print(total)
