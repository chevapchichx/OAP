import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Третья программа")

        self.btn = QPushButton("Кнопка", self)
        self.btn.resize(100, 100)
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.hello)

    def hello(self):
        self.btn.setText("Привет")

if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())