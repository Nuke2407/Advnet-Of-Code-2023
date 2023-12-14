from pathlib import Path 

lines = Path("scratchcards.txt").read_text().splitlines()
total_points = 0

print(len(lines))

for line in lines:
    card, both_numbers = line.split(":")
    winning_numbers, numbers_elf_has = both_numbers.split("|")
    winning_numbers = winning_numbers.strip()
    numbers_elf_has = numbers_elf_has.strip()

    list_of_winning_numbers = [int(w_number.strip()) for w_number in winning_numbers.split(" ") if w_number.isnumeric()]
    list_of_elf_numbers = [int(elf_number.strip()) for elf_number in numbers_elf_has.split(" ") if elf_number.isnumeric()]

    points = 0
    for winning_num in list_of_winning_numbers:
        if winning_num in list_of_elf_numbers and points == 0:
            points += 1
        elif winning_num in list_of_elf_numbers and points >= 1:
            points *= 2

    total_points += points

print(total_points)
    


