import random

def roll_die(sides):
    "Rolls a dice with a specified number of sides"
    return random.randint(1,sides)

def d4():
    return roll_die(4)

def d6():
    return roll_die(6)

def d8():
    return roll_die(8)

def d10():
    return roll_die(10)

def d12():
    return roll_die(12)

def d20():
    return roll_die(20)

def roll_dice(number, sides):
    "rolls mutilple dice and returns indvidual rolls and total"
    rolls = []

    for _ in range(number):
        rolls.append(roll_die(sides))

    total = sum(rolls)

    return rolls, total

def roll_with_modifier(number, sides, modifier):
    "Rolls dice and applies modifier"
    rolls, total = roll_dice(number,sides)
    modified_total = total + modifier
    return rolls, total, modified_total

def ability_modifier(score):
    "Use DND modifier formula"
    return (score-10) // 2

def ability_check(ability_score):
    modifier = ability_modifier(ability_score)
    roll = d20()
    total = roll + modifier
    return roll, modifier, total

def check_success(total, dc):
    return total >= dc
