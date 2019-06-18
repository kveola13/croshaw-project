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
    if len(kept_dice_list) is 0:
        return list_of_dice
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
        print("You get: " + str(sum_of_dice) + " points!\n")
        return sum_of_dice, int(sum_of_dice / amount_of_paris)
    else:
        print("Your roll did not get " + str(amount_of_paris) + " equal dice\n")
        return 0, 0


def find_yahtzee(list_of_dice: list):
    score, placeholder = find_pair(6, 0, list_of_dice)
    if score > 0:
        return score, True
    else:
        return score, False


def find_house(list_of_dice: list, amount_of_dice: int):
    try:
        sum_of_dice, number_to_exclude = find_pair(3, 0, list_of_dice)
        print("Number to exclude: " + str(number_to_exclude))
        second_list_of_dice = roll_dice_with_exchange(throw_dice(amount_of_dice))
        second_sum, number_to_exclude = find_pair(2, number_to_exclude, second_list_of_dice)
        print("You scored: " + str(sum_of_dice + second_sum))
        return sum_of_dice + second_sum, True
    except TypeError:
        print("You did not get the required pairs!\n")
        return 0, False


def chance_play(list_of_dice: list):
    total = 0
    for value in list_of_dice:
        total += value
    print("You get: " + str(total) + " points!")
    return total, True


def check_straight(list_of_dice: list):
    dice_set = set()
    for dice_number in list_of_dice:
        if dice_number not in dice_set:
            dice_set.add(dice_number)
    for value in range(0, len(dice_set) - 1, 1):
        if list(dice_set)[value] + 1 != list(dice_set)[value + 1]:
            print("Sorry, you did not get a straight!\n")
            return 0, False
    if len(dice_set) >= 5:
        return 40, True
    if len(dice_set) == 4:
        return 30, True


def play_strict_order(amount_of_dice: int):
    score = 0
    for index in range(2, 6, 1):
        print("Now playing for: " + str(index) + " amount of pairs!")
        score += find_pair(index, 0, roll_dice_with_exchange(throw_dice(amount_of_dice)))
    print("Now playing for house:")
    house_score, house_boolean = find_house(roll_dice_with_exchange(throw_dice(6)), 6)
    print("Now playing for small straight:")
    small_straight_score, small_straight_boolean = check_straight(roll_dice_with_exchange(throw_dice(6)))
    print("Now playing for big straight:")
    big_straight_score, big_straight_boolean = check_straight(roll_dice_with_exchange(throw_dice(6)))
    test_list = [5, 5, 5, 5, 5, 5]
    print("Now playing for Yahtzee: ")
    yahtzee_score, yahtzee_boolean = find_yahtzee(test_list)
    print("Now playing for chance play!")
    chance_score, chance_boolean = chance_play(roll_dice_with_exchange(throw_dice(6)))
    score = score + house_score + small_straight_score + big_straight_score + yahtzee_score + chance_score
    print("Thanks for playing! Your score is: " + str(score))


def play_loose_order():
    # TODO: Implement this
    return None


if __name__ == '__main__':
    numbers = [5, 5, 5, 5, 5, 4]
    # play_strict_order(6)

    exit()
