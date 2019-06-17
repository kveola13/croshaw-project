import random


def roll_dice_with_exchange(list_of_dice: list):
    kept_dice_list = []
    print("Your roll: " + str(list_of_dice))
    try:
        for dice in map(int, input("Input the die you want to keep, separated by a space: ").split(" ")):
            if dice is not "" and dice in list_of_dice:
                kept_dice_list.append(dice)
            else:
                print("Could not find " + str(dice) + " in your roll\n")
            list_of_dice.remove(dice)
    except ValueError:
        print("There was an error, most likely a misplaced space..")
    if len(kept_dice_list) is not 0:
        print("You kept: " + str(kept_dice_list))
    if len(list_of_dice) is not 0:
        new_dice_throw = throw_dice(len(list_of_dice))
        for value in new_dice_throw:
            kept_dice_list.append(value)
        print("Your new die: " + str(kept_dice_list))
    return kept_dice_list


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
        print("You got " + str(amount_of_paris) + " " + str(int(sum_of_dice / amount_of_paris)) + "\'s")
        print("Your score: " + str(sum_of_dice) + "\n")
        return sum_of_dice
    else:
        print("Your roll did not get " + str(amount_of_paris) + " equal dice\n")
        return 0


def find_yahtzee(list_of_dice: list):
    return find_pair(6, 0, list_of_dice)


def find_house():
    try:
        sum_of_dice, number_to_exclude = find_pair(3, 0, throw_dice(6))
        print("Number to exclude: " + str(number_to_exclude))
        print(find_pair(2, number_to_exclude, throw_dice(6)))
        return sum_of_dice
    except TypeError:
        print("Sorry! You did not get house!\n")
        return 0


def chance_play(list_of_dice: list):
    total = 0
    for value in list_of_dice:
        total += value
    return total


def check_straight(list_of_dice: list):
    dice_set = set()
    for dice_number in list_of_dice:
        if dice_number not in dice_set:
            dice_set.add(dice_number)
    for value in range(0, len(dice_set) - 1, 1):
        if list(dice_set)[value] + 1 != list(dice_set)[value + 1]:
            print("Sorry, you did not get a straight!\n")
            return 0
    if len(dice_set) >= 5:
        return 40
    if len(dice_set) == 4:
        return 30


def play_strict_order(amount_of_dice: int):
    score = 0
    for index in range(2, 6, 1):
        print("Now playing for: " + str(index) + " amount of pairs!")
        score += find_pair(index, 0, roll_dice_with_exchange(throw_dice(amount_of_dice)))
    print("Now playing for house:")
    score += find_house()
    print("Now playing for small straight:")
    score += check_straight(roll_dice_with_exchange(throw_dice(amount_of_dice)))
    print("Now playing for big straight:")
    score += check_straight(roll_dice_with_exchange(throw_dice(amount_of_dice)))
    yahtzee_test_list = [5, 5, 5, 5, 5, 5]
    print("Now playing for Yahtzee: ")
    score += find_yahtzee(yahtzee_test_list)
    print("Now playing for chance play!")
    score += chance_play(roll_dice_with_exchange(throw_dice(amount_of_dice)))
    print("Thanks for playing! Your score is: " + str(score))


def play_loose_order():
    # TODO: Implement this
    return None


if __name__ == '__main__':
    # numbers = [2, 3, 6, 4, 5, 5]
    play_strict_order(6)
    exit()
