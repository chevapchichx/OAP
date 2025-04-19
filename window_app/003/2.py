import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Псевдоним. Возвращение"))
        self.label.setText(_translate("MainWindow", "Задать количество камней"))
        self.pushButton.setText(_translate("MainWindow", "Начать игру"))
        self.label_2.setText(_translate("MainWindow", "Сколько камней взять?"))
        self.pushButton_2.setText(_translate("MainWindow", "Взять"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_game)
        self.pushButton_2.clicked.connect(self.player_turn)
        self.remaining_stones = 0

    def start_game(self):
        self.remaining_stones = self.spinBox.value()
        self.lcdNumber.display(self.remaining_stones)
        self.lineEdit.clear()

    def player_turn(self):
        try:
            stones_taken = int(self.lineEdit.text())
            if stones_taken < 1 or stones_taken > 3:
                raise ValueError("Недопустимое количество камней")
            self.remaining_stones -= stones_taken
            if self.remaining_stones <= 0:
                self.lcdNumber.display(0)
                QtWidgets.QMessageBox.information(self, "Игра окончена", "Вы выиграли!")
                return
            self.lcdNumber.display(self.remaining_stones)
            self.computer_turn()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите допустимое количество камней (1-3)")

    def computer_turn(self):
        stones_taken = min(3, self.remaining_stones)
        self.remaining_stones -= stones_taken
        if self.remaining_stones <= 0:
            self.lcdNumber.display(0)
            QtWidgets.QMessageBox.information(self, "Игра окончена", "Компьютер выиграл!")
            return
        self.lcdNumber.display(self.remaining_stones)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())