###############################################################################
# Advent of Code - 2023: Day 1: Trebuchet?!
# https://adventofcode.com/2023/day/1
# Author: AndiFuerst -- https://github.com/AndiFuerst
###############################################################################

DIGITS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_line_integers_as_strings(line):
    """
    This function takes a string and returns a tuple with the first and last
    digits within the string, whether they are numbers (0, 1, 2) or not 
    (zero, one, two)

    Parameters:
    line (string): The string to be parsed

    Returns:
    a list: A list of the first and last digits within the string
    """
    min_digits_list = []
    max_digits_list = []
    for digit_index in range(len(DIGITS)):
        min_digits_list.append(line.find(DIGITS[digit_index]))
        max_digits_list.append(line.rfind(DIGITS[digit_index]))
    return_integers = []
    for char_index in range(len(line)):
        try:
            int(line[char_index])
        except:
            try:
                result = min_digits_list.index(char_index)
                return_integers.append(str(result))
                break
            except:
                pass
        else:
            return_integers.append(line[char_index])
            break
    for char_index in list(reversed(range(len(line)))):
        try:
            int(line[char_index])
        except:
            try:
                result = max_digits_list.index(char_index)
                return_integers.append(str(result))
                break
            except:
                pass
        else:
            return_integers.append(line[char_index])
            break
    return return_integers

def get_line_value(line):
    """
    This function takes a string and returns the concatenated value of the 
    first and last integers within the string. Even if those integers are
    written out.

    Parameters:
    line (string): The string to be parsed

    Returns:
    int: The concatenated value of the first and last integer within the string.
    """
    values = get_line_integers_as_strings(line)
    return int(values[0] + values[-1])



if __name__ == "__main__":
    file = open("Day1-Trebuchet/input.txt", "r+")
    total_value = 0
    for line in file:
        total_value += get_line_value(line)
    print(total_value)
    file.close()

