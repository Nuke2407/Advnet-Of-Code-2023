from pathlib import Path 

lines = Path("scratchcards.txt").read_text().splitlines()

line_start = 1 
line_end = len(lines)
total_points = 0 

def original_iteration(line_start, line_end):
    
    global total_points

    for line_number, line in enumerate(lines, 1):
        if line_start <= line_number <= line_end:
            print(line_number)
            card, both_numbers = line.split(":")
            
            card_name, card_number = card.split()
            card_number = int(card_number.strip())
            total_points += 1

            winning_numbers, numbers_elf_has = both_numbers.split("|")
            winning_numbers = winning_numbers.strip()
            numbers_elf_has = numbers_elf_has.strip()

            list_of_winning_numbers = [int(w_number.strip()) for w_number in winning_numbers.split(" ") if w_number.isnumeric()]
            list_of_elf_numbers = [int(elf_number.strip()) for elf_number in numbers_elf_has.split(" ") if elf_number.isnumeric()]

            count = 0 
            for winning_num in list_of_winning_numbers:
                if winning_num in list_of_elf_numbers:
                    count += 1
            #print(card_number + 1)
            original_iteration(card_number + 1, card_number + count)

    return total_points
    

answer = original_iteration(line_start, line_end)
print(answer)
    


