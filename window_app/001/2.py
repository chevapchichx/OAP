import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Вычисление выражений")
        self.resize(300, 100)

        self.text1 = QLabel(self)
        self.text1.setText("Выражение:")
        self.line1 = QLineEdit(self)

        self.text2 = QLabel(self)
        self.text2.setText("Результат:")
        self.line2 = QLineEdit(self)

        self.button = QPushButton('→', self)
        self.button.clicked.connect(self.calc_res)

        layout = QGridLayout()
        layout.addWidget(self.text1, 0, 0)
        layout.addWidget(self.line1, 1, 0)
        layout.addWidget(self.button, 1, 1)
        layout.addWidget(self.text2, 0, 2)
        layout.addWidget(self.line2, 1, 2)
        layout.setSpacing(8)

        self.setLayout(layout)


    def calc_res(self):
        self.line2.setText(str(eval(self.line1.text())))
        self.line1.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())