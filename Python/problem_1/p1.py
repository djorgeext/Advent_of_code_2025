with open("Inputs/input", "r") as f:
    lines = f.read().splitlines()

rotations = [x[0] for x in lines]
degrees = [int(x[1:]) for x in lines]
print(degrees)