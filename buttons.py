import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
)


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Gui")
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click Me", self)
        self.label = QLabel("Hello", self)
        self.InitUI()

    def InitUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet(
            "background-color: lightblue; border: 1px solid black;font-size: 30px;"
        )
        self.button.clicked.connect(self.on_button_click)
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 20px;")

    def on_button_click(self):
        self.label.setText("Button Clicked!")


def main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())
    return 0


if __name__ == "__main__":
    sys.exit(main())
