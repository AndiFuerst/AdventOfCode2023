###############################################################################
# Advent of Code - 2023: Day 4: Scratchcards
# https://adventofcode.com/2023/day/4
# Author: AndiFuerst -- https://github.com/AndiFuerst
###############################################################################


def get_matches(list_a, list_b):
    """
    This function takes two lists and returns the number of values that match.

    Parameters:
    list_a (list): the first list to compare
    list_b (list): the second list to compare

    Returns:
    int: the number of matching values
    """
    matches = []
    for a in list_a:
        for b in list_b:
            if a == b and a not in matches:
                matches.append(a)
    return len(matches)

def get_cards(lines):
    """
    This function takes a list of scratchcards and returns a parsed dictionary

    Parameters:
    lines (list): the list of lines to parse

    Returns:
    dict: a dictionary with the card number as the key and the data as the value
    """
    cards = {}
    for line in lines:
        card_number, card_data_str = line.split(":")
        winning_nums_str, my_nums_str = card_data_str.split("|")
        my_nums_str = my_nums_str.split("\n")[0]
        win_nums = []
        my_nums = []
        for num in winning_nums_str.split(" "):
            try:
                win_nums.append(int(num))
            except:
                pass
        for num in my_nums_str.split(" "):
            try:
                my_nums.append(int(num))
            except:
                pass
        card_num =int(card_number.split(" ")[-1])
        cards[card_num] = []
        cards[card_num].append(win_nums)
        cards[card_num].append(my_nums)
    return cards

if __name__ == "__main__":
    file = open("Day4-Scratchcards\input.txt", "r+")
    base_cards = get_cards(file)
    card_matches = {}
    for card in base_cards:
        card_matches[card] = get_matches(base_cards[card][0], base_cards[card][1])
    card_counts = {}
    for card in base_cards:
        card_counts[card] = 1
    for card in card_counts:
        for card_inst in range(card_counts[card]):
            for match in range(card_matches[card]):
                card_counts[card + 1 + match] += 1
    print(sum(list(card_counts.values())))
    file.close()

