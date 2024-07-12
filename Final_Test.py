from pacman import PacManTest
from collections import deque

# Read input from file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Extract dimensions of the grid
values = lines[0].strip().split(',')
values = [int(val) for val in values]
rows, cols = values

values = lines[1].strip().split(',')
values = [int(val) for val in values]
agent_row, agent_col = values

grid = []

# Extract the grid layout
for line in lines[3:]:
    grid.append(list(line.strip()))

# Check the status of a cell (wall or empty)
def check_cell(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        if grid[row][col] != "*":
            return True  
    return False  

# Find the position of agent and food
start_position = (agent_row, agent_col)
food_position = None
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "f":
            food_position = (i, j)
            break


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Implement BFS algorithm 
def bfs(grid, start, end):
    queue = deque([(start, [start])])  
    visited = set([start])  

    while queue:
        current_position, path = queue.popleft()
        if current_position == end:
            return path  
        
        for direction in directions:
            new_row = current_position[0] + direction[0]
            new_col = current_position[1] + direction[1]
            new_position = (new_row, new_col)

            # Check if the new position is valid and not visited before
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != "*" and new_position not in visited:
                visited.add(new_position)
                queue.append((new_position, path + [new_position]))

    return None  

all_paths = bfs(grid, start_position, food_position)

# Prepare the output
output_one = start_position
output_two = food_position
output_three = len(all_paths) - 1 

# Print the outputs
print(output_one)
print(output_two)
print(output_three)

# Prepare the output in the desired format(1.up 2.right ,...)
output_new = []
for i in range(0, len(all_paths) - 1):
    current_position = all_paths[i]
    next_position = all_paths[i + 1]
    
    if next_position[0] == current_position[0] + 1:
        movement = 3  
    elif next_position[0] == current_position[0] - 1:
        movement = 1  
    elif next_position[1] == current_position[1] + 1:
        movement = 2  
    elif next_position[1] == current_position[1] - 1:
        movement = 4  
    
    output_new.extend([current_position, movement])
    
output_new.append(food_position)   
# Print the output
print(output_new)

packMan_test = PacManTest("mapfile.txt",(2,1) , (7,4), 14, output_new)
packMan_test.path()
packMan_test.compare_results()