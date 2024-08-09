###############################################################################
# Advent of Code - 2023: Day 2: Cube Conundrum Pt 2
# https://adventofcode.com/2023/day/2#part2
# Author: AndiFuerst -- https://github.com/AndiFuerst
###############################################################################

import math

GAME_CONFIGURATION = {'red': 12, 'green': 13, 'blue': 14}
CUBE_COLORS =  {'red', 'green', 'blue'}

def get_min_num_of_cubes(game):
    """
    This function takes a string representing a game and returns a list of the
    minimum number of cubes per color.

    Parameters:
    line (string): The string to be parsed

    Returns:
    list: A list containing integer values representing the minimum number of
        cubes of each color
    """
    total_cube_data = {'red': 0, 'green': 0, 'blue': 0}
    game_data = game.split(":")[-1]
    match_data = game_data.split(";")
    for match in match_data:
        for cube_data in match.split(","):
            for color in CUBE_COLORS:
                if color in cube_data:
                    cube_count = int(cube_data.split(" ")[1])
                    if total_cube_data[color] < cube_count:
                        total_cube_data[color] = cube_count
                        break
    return [total_cube_data['red'], total_cube_data['blue'], total_cube_data['green']]


def get_power_of_game(game):
    """
    This function takes a string representing a game and the minimum number
    of each color of cube multiplied together.

    Parameters:
    line (string): The string to be parsed

    Returns:
    int: the power of the game
    """
    min_num_cubes = get_min_num_of_cubes(game)
    return math.prod(min_num_cubes)


if __name__ == "__main__":
    file = open("Day2-CubeConundrum/input.txt", "r+")
    total_sum = 0
    for game in file:
        total_sum += get_power_of_game(game)
    print(total_sum)
