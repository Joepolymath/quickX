from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,500,450)
        self.setWindowTitle("PyJosh")
        self.page()

    def page(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Welcome to PyJosh")
        self.label.move(200,200)

        #button
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.click)

    def click(self):
        filename = QFileDialog.getOpenFileName(self)
        print(filename)
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()