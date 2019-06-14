import random


def throw_dice(amount_of_die: int):
    return [random.randint(1, 6) for _ in range(0, amount_of_die, 1)]


def find_pair(amount_of_paris: int, list_of_dice: list):
    sum_of_dice = 0
    print(list_of_dice)
    # TODO: Implement in the future
    return sum_of_dice


def play_strict_order():
    return None


def play_loose_order():
    # TODO: Implement this
    return None


if __name__ == '__main__':
    find_pair(2, throw_dice(6))
    exit()
