from pathlib import Path 

path = Path("record-of-games.txt").read_text().splitlines()
maxValues = {"red": 12, "green": 13, "blue": 14}

answer = 0

for line in path: 
    game_ID, data = line.split(":")

    min_cubes = {"red": 0, "green": 0, "blue": 0}
    game_value = 1

    for sets in data.split(";"):
        for hand in sets.split(","):
            hand = hand.strip()
            value, color = hand.split(" ")
            value = int(value)

            if min_cubes[color] < value:
                min_cubes[color] = value 

    for key in min_cubes:
        game_value *= min_cubes[key]

    answer += game_value

print(answer)