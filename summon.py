from random import randint


def main():
    num = input("How many summons do you have? ")
    summons = summon_logic(int(num))

    print(summons)


def summon_logic(x):
    out_come = []
    for y in range(1, x+1):
        rolled = randint(1, 10)
        summon = summon_list(rolled)
        out_come.append(summon)
    return out_come


def summon_list(num):
    dict = {"SSR": ["SSR 1", "SSR 2"],
            "SR": ["SR 1", "SR 2", "SR 3", "SR 4"],
            "R": ["R1", "R2", "R3", "R4", "R5", "R6"]}
    if num == 1:
        what_one = randint(1, 2)
        match what_one:
            case 1:
                return dict["SSR"][0]
            case _:
                return dict["SSR"][1]
    elif 2 <= num <= 4:
        what_one = randint(1, 4)
        match what_one:
            case 1:
                return dict["SR"][0]
            case 2:
                return dict["SR"][1]
            case 3:
                return dict["SR"][2]
            case _:
                return dict["SR"][3]
    else:
        what_one = randint(1, 6)
        match what_one:
            case 1:
                return dict["R"][0]
            case 2:
                return dict["R"][1]
            case 3:
                return dict["R"][2]
            case 4:
                return dict["R"][3]
            case 5:
                return dict["R"][4]
            case _:
                return dict["R"][5]



main()