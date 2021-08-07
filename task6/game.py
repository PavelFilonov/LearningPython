import sys
from PyQt5.QtWidgets import QApplication

from task6.window import MyWindow

app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())