import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('/Users/svetatugay/Library/CloudStorage/OneDrive-РАНХиГС/ОАиП/OAP_050.ui', self) # Загружаем дизайн
        self.pushButton_main_window_1.clicked.connect(self.run)

    def run(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())