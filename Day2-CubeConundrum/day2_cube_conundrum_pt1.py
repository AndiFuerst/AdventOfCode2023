###############################################################################
# Advent of Code - 2023: Day 2: Cube Conundrum Pt 1
# https://adventofcode.com/2023/day/2
# Author: AndiFuerst -- https://github.com/AndiFuerst
###############################################################################

import os

GAME_CONFIGURATION = {'red': 12, 'green': 13, 'blue': 14}
CUBE_COLORS =  {'red', 'green', 'blue'}



def is_game_possible(game):
    """
    This function takes a string representing a game and returns whether 
    the game is possible based on the current configuration.

    Parameters:
    line (string): The string to be parsed

    Returns:
    Bool: True if the game is possible, false otherwise
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
    for color in CUBE_COLORS:
        if GAME_CONFIGURATION[color] < total_cube_data[color]:
            return False
    return True


def get_game_id(game):
    """
    This function takes a string representing a game and returns the game's id

    Parameters:
    line (string): The string to be parsed

    Returns:
    int: The Id of the given game
    """
    game_full_name = game.split(":")[0]
    return int(game_full_name.split("Game ")[-1])


if __name__ == "__main__":
    file = open("Day2-CubeConundrum/input.txt", "r+")
    possible_games = []
    for game in file:
        if is_game_possible(game):
            possible_games.append(get_game_id(game))
    print(sum(possible_games))
    file.close()
