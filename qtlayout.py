import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTLayOut ")
        self.setGeometry(700, 300, 500, 500)
        self.InitUI()

    def InitUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        label1 = QLabel("Label 1", self)
        label2 = QLabel("Label 2", self)
        label3 = QLabel("Label 3", self)
        label4 = QLabel("Label 4", self)
        label5 = QLabel("Label 5", self)

        label1.setStyleSheet("background-color: lightblue; border: 1px solid black;")
        label2.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
        label3.setStyleSheet("background-color: lightcoral; border: 1px solid black;")
        label4.setStyleSheet("background-color: lightyellow; border: 1px solid black;")
        label5.setStyleSheet("background-color: lightgray; border: 1px solid black;")

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        central_widget.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    return 0


if __name__ == "__main__":
    sys.exit(main())
