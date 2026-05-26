with open("Inputs/input", "r") as f:
    lines = f.read().splitlines()

rotations = [x[0] for x in lines]
degrees = [int(x[1:]) for x in lines]

count = 0
position = 50

for i in range(len(rotations)):
    if rotations[i] == "R":
        temp = position + degrees[i]
        if temp >= 100:
            temp -= 100
        position = temp

    else:
