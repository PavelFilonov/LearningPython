from PyQt5.QtWidgets import *
from task6.logic import LightsOut


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ROWS_COUNT = 5
        self.COLS_COUNT = 5
        self.menuButtons = []
        self.gameButtons = []
        self.setWindowTitle('Выключить свет!')
        self.setGeometry(0, 0, 500, 500)
        self.location_on_the_screen()
        self.init_menu()
        self.init_chooser_level()
        self.show()

    def location_on_the_screen(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def init_menu(self):
        buttons = [QPushButton('Начать игру', self), QPushButton('Правила игры', self), QPushButton('Выйти', self)]
        buttons[0].setGeometry(100, 150, 300, 50)
        buttons[1].setGeometry(100, 210, 300, 50)
        buttons[2].setGeometry(100, 270, 300, 50)
        for i in range(len(buttons)):
            buttons[i].clicked.connect(self.clicked_in_menu)
        self.menuButtons.append(buttons)
        self.show_menu()

    def init_chooser_level(self):
        buttons = [QPushButton('1 уровень', self), QPushButton('2 уровень', self),
                   QPushButton('3 уровень', self), QPushButton('4 уровень', self),
                   QPushButton('5 уровень', self)]
        for i in range(len(buttons)):
            buttons[i].setVisible(False)
            buttons[i].move(200, 100 + i * 50)
            buttons[i].clicked.connect(self.choosed_level)
        self.menuButtons.append(buttons)

    def show_menu(self):
        for i in range(len(self.menuButtons[0])):
            self.menuButtons[0][i].setVisible(True)

    def init_buttons(self):
        self.gameButtons.clear()
        for i in range(self.ROWS_COUNT):
            b = []
            for j in range(self.COLS_COUNT):
                b.append(QPushButton('', self))
                b[j].setGeometry(j * 100, i * 100, 100, 100)
                b[j].setVisible(True)
            self.gameButtons.append(b)

        for i in range(self.ROWS_COUNT):
            for j in range(self.COLS_COUNT):
                self.gameButtons[i][j].clicked.connect(self.clicked_in_game)

    def updateView(self):
        for i in range(self.ROWS_COUNT):
            for j in range(self.COLS_COUNT):
                if self.game.field[i][j]:
                    self.gameButtons[i][j].setStyleSheet('background: rgb(0,0,255);')
                else:
                    self.gameButtons[i][j].setStyleSheet('background: rgb(255,255,0);')
        self.endOfGame()

    def clicked_in_menu(self):
        if self.sender().text() == 'Начать игру':
            self.closeMenu()
        elif self.sender().text() == 'Правила игры':
            QMessageBox.question(self, 'Правила игры', 'Игра "Выключить свет!" имеет следующие правила:\n'
                                                       ' - цель игры – выключить свет на всю доску\n'
                                                       ' - нажав на квадрат доски переключаете свет в соответствующем '
                                                       'квадрате\n'
                                                       ' - нажав на квадрат доски переключаете свет и в соседних '
                                                       'квадратах (в направлениях север, юг, восток и запад)',
                                 QMessageBox.Ok)
        elif self.sender().text() == 'Выйти':
            exit()

    def clicked_in_game(self):
        for i in range(self.ROWS_COUNT):
            for j in range(self.COLS_COUNT):
                if self.gameButtons[i][j] == self.sender():
                    row = i
                    col = j
                    self.game.changeArray(row, col)
                    self.updateView()

    def choosed_level(self):
        for j in range(len(self.menuButtons[1])):
            self.menuButtons[1][j].setVisible(False)
        self.init_buttons()
        self.game = LightsOut(int(self.sender().text().split(' ')[0]))
        self.updateView()

    def closeMenu(self):
        for j in range(len(self.menuButtons[0])):
            self.menuButtons[0][j].setVisible(False)
        self.showChooserLevel()

    def showChooserLevel(self):
        for j in range(len(self.menuButtons[1])):
            self.menuButtons[1][j].setVisible(True)

    def closeGameButtons(self):
        for i in range(len(self.gameButtons)):
            for j in range(len(self.gameButtons[i])):
                self.gameButtons[i][j].setVisible(False)

    def endOfGame(self):
        if self.game.checkWin():
            for i in range(self.ROWS_COUNT):
                for j in range(self.COLS_COUNT):
                    self.gameButtons[i][j].setStyleSheet('background: rgb(0,128,0);')
            if self.game.lvl == 5:
                messageBox = QMessageBox.question(self, '', 'You win!', QMessageBox.Ok)
                if messageBox == QMessageBox.Ok:
                    self.closeGameButtons()
                    self.show_menu()
            else:
                messageBox = QMessageBox.question(self, 'You win!', 'Перейти на следующий уровень?',
                                              QMessageBox.Yes | QMessageBox.No)
                if messageBox == QMessageBox.Yes:
                    self.game.loadLvl(self.game.lvl + 1)
                    self.updateView()
                if messageBox == QMessageBox.No:
                    self.closeGameButtons()
                    self.show_menu()
