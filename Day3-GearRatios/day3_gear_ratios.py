###############################################################################
# Advent of Code - 2023: Day 3: Gear Ratios
# https://adventofcode.com/2023/day/3
# Author: AndiFuerst -- https://github.com/AndiFuerst
# Reference Material: https://www.reddit.com/r/adventofcode/comments/189m3qw/comment/kbs9g3g/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
###############################################################################

import re
import math

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_numbers(line_list, locations):
    """
    This function takes a string and returns the list of all the part numbers
    within the string. 

    Parameters:
    line_list (list): The list of strings to be parsed

    Returns:
    list: A list containing all of the part numbers
    """
    part_numbers = {}
    for i, line in enumerate(line_list):
        for num in re.finditer(r"\d+", line):
            edges = {(i, char) for i in (i-1, i, i+1)
                               for char in range(num.start()-1, num.end()+1)}
            for elem in edges & set(locations):
                if elem not in part_numbers:
                    part_numbers[elem] = []
                part_numbers[elem].append(int(num.group()))
    return part_numbers

def get_symbol_locations(lines):
    locations = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char not in '0123456789.':
                locations[(i, j)] = []
    return locations


if __name__ == "__main__":
    file = open("Day3-GearRatios/input.txt", "r+")
    lines = file.read().splitlines()
    symbol_locations = get_symbol_locations(lines)
    numbers = get_numbers(lines, symbol_locations)
    print(f"Part 1: {sum(sum(num) for num in numbers.values())}")
    total = 0

    print(f"Part 2: {sum(math.prod(num) for num in numbers.values() if len(num)==2)}")
    file.close()

