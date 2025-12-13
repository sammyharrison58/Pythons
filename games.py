import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Father_Looks")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("logo.jpg"))
        Label = QLabel("Its Father_Looks", self)
        Label.setFont(QFont("Arial", 20))
        Label.setGeometry(0, 0, 500, 100)
        Label.setStyleSheet(
            "color:white;"
            "background-color:grey;"
            "font-weight:bold;"
            "font-style:italic;"
            "text-decoration:underline;"
        )
        Label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)


def main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
