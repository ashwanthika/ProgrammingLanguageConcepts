# Ashwanthika Umasankar
# UTA ID - 1001854976
# Python version used - Python 3.9.13
# OS -  Windows

import random

def create_maze_route(path, current_x, current_y):
    """
    Recursive function to generate the maze path.
    """
    path[current_x][current_y] = 1
    possible_directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(possible_directions)

    for x_direction, y_direction in possible_directions:
        new_x, new_y = current_x + x_direction, current_y + y_direction
        if 0 <= new_x < len(path) and 0 <= new_y < len(path[0]) and path[new_x][new_y] == 0:
            path[current_x + x_direction // 2][current_y + y_direction // 2] = 1
            create_maze_route(path, new_x, new_y)

def draw_maze(width, length):
    """
    Function to generate the maze with specified dimensions.
    """
    try:
        horizontal = width* 2 + 1
        vertical = length* 2 + 1

        path = [[0] * horizontal for val in range(vertical)]
        create_maze_route(path, 1, 1)

        start = random.randint(1, width) * 2
        path[1][start] = 1
        quit = random.randint(1, width) * 2
        path[vertical - 2][quit] = 1
        path[0][random.randint(0, width)] = ' '
        path[-1][random.randint(0, width)] = ' '
        return path

    except ValueError:
        print("This input is not accepted, please try again")

def print_maze(path):
    """
    Function to print the maze.
    """
    out = ""
    for var_i in range(len(path)):
        if var_i % 2 == 0:
            for var_j in range(len(path[0])):
                if var_i == 1 and var_j == 0:
                    out += "   "
                elif var_i == len(path) - 2 and var_j == len(path[0]) - 1:
                    out += "   "
                elif path[var_i][var_j] == 0:
                    out += ":--"
                else:
                    out += ":  "
            out += ":\n"
        else:
            for var_j in range(len(path[0])):
                out += "|  " if path[var_i][var_j] == 0 else "   "

            out += "|\n"

    print(out)

width = 0
length = 0

try:
    inputs = input("Enter the width and length (comma-separated ): ")
    width, length = map(int, inputs.split(","))
except ValueError:
    print("This input is not accepted, please try again ")

maze_path = draw_maze(width, length)
print('\t AMAZING PROGRAM\n')
print('CREATIVE COMPUTING MORRISTOW, NEW JERSEY\n')
print_maze(maze_path)