from pathlib import Path

answer = 0

path = Path("calibration_document.txt").read_text().splitlines() 
initialtest = ['o', 't', 'f', 's', 'e', 'n']
values = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}

for line in path: 
    temp = []
    for i in range(len(line)):
        if line[i].isnumeric(): 
            temp.append(line[i])
        if line[i] in initialtest:
            if line[i:i+3] in values:
                temp.append(values[line[i:i+3]])
            elif line[i:i+4] in values:
                temp.append(values[line[i:i+4]])
            elif line[i:i+5] in values:
                temp.append(values[line[i:i+5]])
            else: 
                None
        else: 
            None
    answer += int(temp[0] + temp[-1])

print(answer)


