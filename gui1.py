import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Application")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowIcon(QIcon("../images/logo.jpg"))
        label = QLabel("Father_Looks always represents", self)
        label.setFont(QFont("Arial", 16))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet(
            "color: blue;"
            "background-color: lightgray;"
            "border: 2px solid black;"
            "font-weight: bold;"
            "font-style: italic;"
            "padding: 10px;"
            "text-decoration: underline;"
        )
        label.setAlignment(Qt.AlignCenter)
        self.show()


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    return 0


if __name__ == "__main__":
    sys.exit(main())
