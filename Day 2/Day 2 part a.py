from pathlib import Path 

path = Path("record-of-games.txt").read_text().splitlines()
maxValues = {"red": 12, "green": 13, "blue": 14}

answer = 0

for line in path: 
    game_ID, data = line.split(":")
    game, game_value =  game_ID.split(" ")
    game_value = int(game_value)

    for sets in data.split(";"):
        for hand in sets.split(","):
            hand = hand.strip()
            value, color = hand.split(" ")
            value = int(value)

            if value > maxValues[color]:
                game_value = 0
                break

    answer += game_value

print(answer)