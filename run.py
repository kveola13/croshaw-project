import random


def throw_dice(amount_of_die: int):
    return [random.randint(1, 6) for _ in range(0, amount_of_die, 1)]


def find_pair(amount_of_paris: int, list_of_dice: list):
    sum_of_dice = 0
    for value in range(6, 0, -1):
        counter = 0
        for dice_number in list_of_dice:
            if dice_number == value:
                counter += 1
                if counter >= amount_of_paris:
                    sum_of_dice = max(dice_number * amount_of_paris, sum_of_dice)
    if sum_of_dice is not 0:
        return sum_of_dice
    else:
        print("Your roll did not get " + str(amount_of_paris) + " equal dice")


def play_strict_order():
    return None


def play_loose_order():
    # TODO: Implement this
    return None


if __name__ == '__main__':
    numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 5, 5]
    print(find_pair(2, throw_dice(6)))
    exit()
