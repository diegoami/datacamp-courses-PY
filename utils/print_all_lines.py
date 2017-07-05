file = 'digits_header.txt'

with open(file) as f:
    lines = f.readlines()
    for line in lines:
        if line:
            print(line.rstrip("\n"))