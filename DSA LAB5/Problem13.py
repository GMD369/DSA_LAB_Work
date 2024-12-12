def display_grid(grid):
    for row in grid:
        print(row)

def Add_row(grid,row):
    if len(grid)==0 or len(row)==len(grid[0]):
        grid.append(row)
    else:
        print("Invalid row")

def Add_col(grid,col):
    if len(grid)==0 or len(col)==len(grid): 
        for i in range(len(grid)):
            grid[i].append(col[i])
    else:
        print("Error: New column length must match the current grid height.")      

def Sum_Grid(grid):
    total = 0
    for row in grid:
        total += sum(row)
    return total


grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row=[1,45,66]
Add_row(grid,row)
print("After added row:")
display_grid(grid)  


col = [13, 14, 15, 16] 
Add_col(grid,col)
print("After added column:")
display_grid(grid)

print("Sum of Grid:")
print(Sum_Grid(grid))