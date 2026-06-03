with open("Inputs/input", "r") as f:
    lines = f.read().splitlines()

rotations = [x[0] for x in lines]
degrees = [int(x[1:]) for x in lines]

count = 0
position = 50

# function to determine the new position of the ship after a rotation
def rotate(position, rotation, degree):
    temp = position + degree if rotation == "R" else position - degree
    return temp % 100

for i in range(len(rotations)):
    position = rotate(position, rotations[i], degrees[i])
    if position == 0:
        count += 1

print(count)
