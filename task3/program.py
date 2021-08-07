from task3 import point
from task3 import triangle


def proportionality(t1, t2):
    values = [t1.getAB(), t1.getBC(), t1.getAC(), t2.getAB(), t2.getBC(), t2.getAC()]
    return (
            values[0] / values[3] == values[1] / values[4] == values[2] / values[5] or
            values[0] / values[4] == values[1] / values[3] == values[2] / values[5] or
            values[0] / values[3] == values[1] / values[5] == values[2] / values[4] or
            values[0] / values[5] == values[1] / values[4] == values[2] / values[3] or
            values[0] / values[4] == values[1] / values[5] == values[2] / values[3] or
            values[0] / values[5] == values[1] / values[3] == values[2] / values[4]
    )


def solution(lst):
    resultList = []

    for i in range(0, len(lst)):
        notAdded = True
        for j in range(0, len(resultList)):
            if proportionality(lst[i], resultList[j][0]):
                resultList[j].append(lst[i])
                notAdded = False
        if notAdded:
            newGroup = [lst[i]]
            resultList.append(newGroup)

    return resultList


example = [
    triangle.Triangle(point.Point(1, 5), point.Point(2, 7), point.Point(4, 5)),
    triangle.Triangle(point.Point(2, 1), point.Point(-4, 6), point.Point(-2, 2)),
    triangle.Triangle(point.Point(2, -2), point.Point(2, -6), point.Point(4, -6)),
    triangle.Triangle(point.Point(-6, 1), point.Point(-9, 1), point.Point(-7, 3)),
    triangle.Triangle(point.Point(-7, -5), point.Point(-7, -4), point.Point(-9, -5))
]
s = solution(example)
for k in range(len(s)):
    print("Группа " + str(k + 1) + ":")
    for g in range(len(s[k])):
        print(s[k][g].get())
    print()
