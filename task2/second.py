def solution(matrix):
    # 1 - последовательность возрастает, 0 - убывает, -1 - первоначальное значение,
    # 2 - не убывает и не возрастает
    s = -1
    sign = -1
    currentRow = len(matrix) - 1
    for j in range(0, len(matrix[0])):
        for i in range(0, len(matrix)):
            if j == len(matrix[0]) - 1 and i == len(matrix) - 1:
                continue
            if s == -1:
                s = isSequence(matrix[currentRow][j], matrix[currentRow + sign][j])
            else:
                col = j
                row = currentRow + sign
                if i == len(matrix) - 1:
                    row = currentRow
                    col = j + 1

                if s != isSequence(matrix[currentRow][j], matrix[row][col]) \
                        and isSequence(matrix[currentRow][j], matrix[row][col]) != 2:
                    return False
            if i != len(matrix) - 1:
                currentRow += sign
        sign *= -1

    return True


def isSequence(firstValue, secondValue):
    if secondValue > firstValue:
        return 1
    elif firstValue > secondValue:
        return 0
    else:
        return 2


example1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]
example2 = [
    [1],
    [6],
    [11],
    [16],
    [21]]
example3 = [
    [1, 0],
    [6, -1],
    [11, -2],
    [16, -3],
    [21, -4]]
print(solution(example1))
print(solution(example2))
print(solution(example3))
