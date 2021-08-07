def getIndexFirstMaxElement(lst):
    index = 0
    value = lst[index]

    for i in range(1, len(lst)):
        if lst[i] > value:
            index = i
            value = lst[i]

    return index


def getIndexLastMinElement(lst):
    index = 0
    value = lst[index]

    for i in range(1, len(lst)):
        if lst[i] <= value:
            index = i
            value = lst[i]

    return index


def turnList(lst, firstIndex, lastIndex):
    scope = (lastIndex - firstIndex) // 2 + 1

    for i in range(0, scope):
        lst[i + firstIndex], lst[lastIndex - i] = lst[lastIndex - i], lst[i + firstIndex]


def solution(lst):
    minIndex = getIndexFirstMaxElement(lst)
    maxIndex = getIndexLastMinElement(lst)

    if minIndex > maxIndex:
        minIndex, maxIndex = maxIndex, minIndex

    turnList(lst, minIndex + 1, maxIndex - 1)

    return lst


print("Пример из задания:", end=" ")
example1 = [2, 1, 0, 3, 3]
print(example1)
print("Результат:", end=" ")
print(solution(example1))

# length = int(input("Введите размер списка "))
# print("Введите элементы списка")
# example2 = []
# for i in range(0, length):
#     example2.append(int(input()))
# print("Результат:", end=" ")
# print(solution(example2))
