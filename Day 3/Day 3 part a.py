from pathlib import Path 

path = Path("Engine_Schematic.txt").read_text().splitlines()

grid = [list(line) for line in path]
total = 0 


for row_index, row in enumerate(grid):
    for column_index, value in enumerate(row):

        if value != '.' and not value.isnumeric():  
            for row_finder in [-1,0,1]:
                for column_finder in [-1,0,1]:
                    local_row = row_index + row_finder
                    local_column = column_index + column_finder
                    if 0 <= local_row < len(grid) and 0 <= local_column < len(row):
                        if grid[local_row][local_column].isnumeric():

                            while local_column + 1 < len(row) and grid[local_row][local_column + 1].isnumeric():
                                local_column += 1
                            
                            number = []
                            number.append(grid[local_row][local_column])
                            grid[local_row][local_column] = '.'
                        
                            while local_column - 1 >= 0 and grid[local_row][local_column - 1].isnumeric():
                                local_column -= 1
                                number.append(grid[local_row][local_column])
                                grid[local_row][local_column] = '.'

                            number.reverse() 

                            final_number = ""
                            for num in number:
                                final_number += num

                            total += int(final_number)


print(total)
