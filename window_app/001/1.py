import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Фокус со словами")
        self.resize(250, 150)

        self.line1 = QLineEdit(self)
        self.line2 = QLineEdit(self)

        self.button = QPushButton('→', self)
        self.button.clicked.connect(self.switch_button)

        self.left_to_right = True

        layout = QHBoxLayout()
        layout.addWidget(self.line1)
        layout.addWidget(self.button)
        layout.addWidget(self.line2)
        layout.setSpacing(9)

        self.setLayout(layout)

    def switch_button(self):
        if self.left_to_right:
            self.line2.setText(self.line1.text())
            self.line1.clear()
            self.button.setText('←')
        else:
            self.line1.setText(self.line2.text())
            self.line2.clear()
            self.button.setText('→')

        self.left_to_right = not self.left_to_right


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())