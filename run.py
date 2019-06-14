import random


def throw_dice(amount_of_die: int):
    return [random.randint(1, 6) for _ in range(0, amount_of_die, 1)]


def find_pair(amount_of_paris: int, number_to_exclude: int, list_of_dice: list):
    sum_of_dice = 0
    for value in range(6, 0, -1):
        counter = 0
        for dice_number in list_of_dice:
            if dice_number == value and dice_number != number_to_exclude:
                counter += 1
                if counter >= amount_of_paris:
                    sum_of_dice = max(dice_number * amount_of_paris, sum_of_dice)
    if sum_of_dice is not 0:
        print(list_of_dice)
        return sum_of_dice, int(sum_of_dice / amount_of_paris)
    else:
        print("Your roll did not get " + str(amount_of_paris) + " equal dice")


def find_yahtzee(list_of_dice: list):
    print(find_pair(6, 0, list_of_dice))


def find_house():
    try:
        sum_of_dice, number_to_exclude = find_pair(3, 0, throw_dice(6))
        print("Number to exclude: " + str(number_to_exclude))
        print(find_pair(2, number_to_exclude, throw_dice(6)))
    except TypeError:
        print("You did not get 3 of the same")


def chance_play(list_of_dice: list):
    total = 0
    for value in list_of_dice:
        total += value
    return total


def check_straight(list_of_dice: list):
    sorted_list = list(range(min(list_of_dice), max(list_of_dice) + 1))
    return sum(sorted_list * 2)


def play_strict_order():
    for index in range(1, 7, 1):
        print(find_pair(index, 0, throw_dice(6)))
    find_house()
    check_straight(throw_dice(6))
    check_straight(throw_dice(6))
    yahtzee_test_list = [5, 5, 5, 5, 5, 5]
    find_yahtzee(yahtzee_test_list)
    print(chance_play(throw_dice(6)))


def play_loose_order():
    # TODO: Implement this
    return None


if __name__ == '__main__':
    numbers = [2, 3, 6, 4, 5]
    # print(find_pair(2, throw_dice(6)))
    play_strict_order()
    exit()
