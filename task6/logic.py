from task6 import loader


class LightsOut:

    def __init__(self, lvl):
        self.lvl = lvl
        self.field = []
        self.loadLvl(lvl)

    def changeArray(self, row, col):
        self.field[row][col] = not self.field[row][col]

        if row > 0:
            self.field[row - 1][col] = not self.field[row - 1][col]

        if row < len(self.field) - 1:
            self.field[row + 1][col] = not self.field[row + 1][col]

        if col > 0:
            self.field[row][col - 1] = not self.field[row][col - 1]

        if col < len(self.field[0]) - 1:
            self.field[row][col + 1] = not self.field[row][col + 1]

    def readArrayOfLvl(self, matrix):
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    row.append(True)
                else:
                    row.append(False)
            self.field.append(row)

    def loadLvl(self, lvl):
        self.field = []
        self.lvl = lvl
        self.readArrayOfLvl(loader.load('levels/level_0' + str(lvl) + '.txt'))

    def checkWin(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if not self.field[i][j]:
                    return False
        return True
