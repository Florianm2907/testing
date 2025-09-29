def is_solution(cell_data):
    for row in cell_data:
        if 'cell empty' in row:
            return False
    return True

def move_up(posx, posy, cell_data):
    if posy > 0 and not 'cell blocked' in cell_data[posy-1][posx]:
        cell_data[posy][posx] = 'cell blocked'
        posy -= 1
    return posx, posy, cell_data

def move_down(posx, posy, cell_data):
    if posy < len(cell_data) - 1 and not 'cell blocked' in cell_data[posy+1][posx]:
        cell_data[posy][posx] = 'cell blocked'
        posy += 1
    return posx, posy, cell_data

def move_right(posx, posy, cell_data):
    if posx < len(cell_data[0]) - 1 and not 'cell blocked' in cell_data[posy][posx+1]:
        cell_data[posy][posx] = 'cell blocked'
        posx += 1
    return posx, posy, cell_data

def move_left(posx, posy, cell_data):
    if posx > 0 and not 'cell blocked' in cell_data[posy][posx-1]:
        cell_data[posy][posx] = 'cell blocked'
        posx -= 1
    return posx, posy, cell_data

def start(x, y, cell_data):
    if not 'cell blocked' in cell_data[y][x]: 
        posx = x
        posy = y
        cell_data[y][x] = 'cell blocked'
    return posx, posy, cell_data

def dfs(posx, posy, cell_data):
    if is_solution(cell_data):
        return True

    for move_func in [move_up, move_down, move_left, move_right]:
        new_posx, new_posy, new_cell_data = move_func(posx, posy, [row[:] for row in cell_data])  # Make a copy of cell_data
        if new_cell_data != cell_data:  # Check if the move is valid
            if dfs(new_posx, new_posy, new_cell_data):
                return True
    return False
def is_goal_state(cell_data):
    # Check if all cells are blocked
    for row in cell_data:
        if 'cell empty' in row:
            return False
    return True
def bruteforce(posx, posy, cell_data):
    # Base case: Check if goal state is reached
    if is_goal_state(cell_data):
        return True
    
    # Try moving up
    if posy > 0 and not 'cell blocked' in cell_data[posy-1][posx]:
        cell_data[posy][posx] = 'cell blocked'
        if bruteforce(posx, posy - 1, cell_data):
            return True
        cell_data[posy][posx] = 'cell empty'
    
    # Try moving down
    if posy < len(cell_data) - 1 and not 'cell blocked' in cell_data[posy+1][posx]:
        cell_data[posy][posx] = 'cell blocked'
        if bruteforce(posx, posy + 1, cell_data):
            return True
        cell_data[posy][posx] = 'cell empty'
    
    # Try moving right
    if posx < len(cell_data[0]) - 1 and not 'cell blocked' in cell_data[posy][posx+1]:
        cell_data[posy][posx] = 'cell blocked'
        if bruteforce(posx + 1, posy, cell_data):
            return True
        cell_data[posy][posx] = 'cell empty'
    
    # Try moving left
    if posx > 0 and not 'cell blocked' in cell_data[posy][posx-1]:
        cell_data[posy][posx] = 'cell blocked'
        if bruteforce(posx - 1, posy, cell_data):
            return True
        cell_data[posy][posx] = 'cell empty'
    print(posx, posy)
    return False

# Example usage:
cell_data = [
    ['cell blocked', 'cell blocked', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty'],
    ['cell empty', 'cell empty', 'cell empty', 'cell blocked', 'cell blocked', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty'],
    ['cell empty', 'cell empty', 'cell empty', 'cell blocked', 'cell empty', 'cell empty', 'cell blocked', 'cell empty', 'cell empty', 'cell empty', 'cell empty'],
    ['cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell blocked', 'cell blocked', 'cell empty', 'cell empty', 'cell empty', 'cell empty'],
    ['cell empty', 'cell empty', 'cell blocked', 'cell blocked', 'cell blocked', 'cell blocked', 'cell blocked', 'cell empty', 'cell empty', 'cell empty', 'cell empty'],
    ['cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty'],
    ['cell empty', 'cell empty', 'cell empty', 'cell blocked', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty'],
    ['cell empty', 'cell blocked', 'cell empty', 'cell empty', 'cell empty', 'cell blocked', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty'],
    ['cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell empty', 'cell blocked', 'cell empty', 'cell empty', 'cell empty']
]

# # Start DFS from each cell
# for y in range(len(cell_data)):
#     for x in range(len(cell_data[0])):
#         if cell_data[y][x] == 'cell blocked':
#             print(x,y)
#             continue
#         if dfs(x, y, cell_data):
#             print("Solution found!")
#             for row in cell_data:
#                 print(row)
#             exit()

# print("No solution found.")

posx, posy = 2, 0  # Example start position at (2, 0)

# Run bruteforce search
if bruteforce(posx, posy, cell_data):
    print("Solution found:")
    for row in cell_data:
        print(row)
else:
    print("No solution found.")