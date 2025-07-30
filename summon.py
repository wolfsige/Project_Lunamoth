import json
from random import randint
import random


def main():
    continue_on = ""
    while continue_on.upper() != "N":
        continue_on = input("Hit 'Enter' to summon"
                            
                            "Enter 'N' stop ")
        if continue_on.upper() != "N":
            summon_logic()
            print(

            )

def summon_logic():
    with open("unit_database.json", "r") as summons:
        data = json.load(summons)

    ssr_units = []
    for unit in data:
        if unit["rarity"] == "SSR":
            ssr_units.append(unit)

    sr_units = []
    for unit in data:
        if unit["rarity"] == "SR":
            sr_units.append(unit)

    r_units = []
    for unit in data:
        if unit["rarity"] == "R":
            r_units.append(unit)

    for _ in range(10):
        roll = randint(1, 100)

        if roll <= 5:
            chosen_unit = random.choice(ssr_units)
        elif 5 < roll <= 30:
            chosen_unit = random.choice(sr_units)
        else:
            chosen_unit = random.choice(r_units)

        print(f"You summoned {chosen_unit['name']}, "
              f"they are {chosen_unit["rarity"]} rarity!")

main()