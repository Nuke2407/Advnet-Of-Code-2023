from pathlib import Path 

path = Path("calibration_document.txt")
document = path.read_text()
lines = document.splitlines()

answer = 0
bucket =[]

for line in lines: 

    for char in line:
        if char.isnumeric():
            bucket.append(char)
    if len(bucket):
        value = bucket[0] + bucket[-1]
        answer += int(value)
    else:
        None
    bucket = [] 

print(answer)
