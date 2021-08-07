def load(path):
    with open(path, 'r') as file:
        matrix = file.readlines()
        matrix = [[int(n) for n in x.split()] for x in matrix]
    return matrix
