import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 120, 104, 54))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 120, 104, 54))
        font.setPointSize(23)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 120, 104, 54))
        font.setPointSize(23)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.radioButton_blue_1 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_blue_1.setGeometry(QtCore.QRect(110, 200, 100, 20))
        self.radioButton_blue_1.setObjectName("radioButton_blue_1")

        self.radioButton_red_1 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_red_1.setGeometry(QtCore.QRect(110, 240, 100, 20))
        self.radioButton_red_1.setObjectName("radioButton_red_1")

        self.radioButton_green_1 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_green_1.setGeometry(QtCore.QRect(110, 280, 100, 20))
        self.radioButton_green_1.setObjectName("radioButton_green_1")

        self.buttonGroup1 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup1.addButton(self.radioButton_blue_1)
        self.buttonGroup1.addButton(self.radioButton_red_1)
        self.buttonGroup1.addButton(self.radioButton_green_1)

        self.radioButton_blue_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_blue_2.setGeometry(QtCore.QRect(330, 200, 100, 20))
        self.radioButton_blue_2.setObjectName("radioButton_blue_2")

        self.radioButton_red_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_red_2.setGeometry(QtCore.QRect(330, 240, 100, 20))
        self.radioButton_red_2.setObjectName("radioButton_red_2")

        self.radioButton_green_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_green_2.setGeometry(QtCore.QRect(330, 280, 100, 20))
        self.radioButton_green_2.setObjectName("radioButton_green_2")

        self.buttonGroup2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup2.addButton(self.radioButton_blue_2)
        self.buttonGroup2.addButton(self.radioButton_red_2)
        self.buttonGroup2.addButton(self.radioButton_green_2)

        self.radioButton_blue_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_blue_3.setGeometry(QtCore.QRect(550, 200, 100, 20))
        self.radioButton_blue_3.setObjectName("radioButton_blue_3")

        self.radioButton_red_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_red_3.setGeometry(QtCore.QRect(550, 240, 100, 20))
        self.radioButton_red_3.setObjectName("radioButton_red_3")

        self.radioButton_green_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_green_3.setGeometry(QtCore.QRect(550, 280, 100, 20))
        self.radioButton_green_3.setObjectName("radioButton_green_3")

        self.buttonGroup3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup3.addButton(self.radioButton_blue_3)
        self.buttonGroup3.addButton(self.radioButton_red_3)
        self.buttonGroup3.addButton(self.radioButton_green_3)

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 400, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.draw_flag)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Текстовый флаг"))
        self.label.setText(_translate("MainWindow", "Текст №1"))
        self.label_2.setText(_translate("MainWindow", "Текст №2"))
        self.label_3.setText(_translate("MainWindow", "Текст №3"))
        self.radioButton_blue_1.setText(_translate("MainWindow", "Синий"))
        self.radioButton_red_1.setText(_translate("MainWindow", "Красный"))
        self.radioButton_green_1.setText(_translate("MainWindow", "Зеленый"))
        self.radioButton_blue_2.setText(_translate("MainWindow", "Синий"))
        self.radioButton_red_2.setText(_translate("MainWindow", "Красный"))
        self.radioButton_green_2.setText(_translate("MainWindow", "Зеленый"))
        self.radioButton_blue_3.setText(_translate("MainWindow", "Синий"))
        self.radioButton_red_3.setText(_translate("MainWindow", "Красный"))
        self.radioButton_green_3.setText(_translate("MainWindow", "Зеленый"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать"))

    def draw_flag(self):
        color1 = self.get_selected_color(self.buttonGroup1)
        color2 = self.get_selected_color(self.buttonGroup2)
        color3 = self.get_selected_color(self.buttonGroup3)
        message = f"{color1}, {color2}, {color3}"
        QtWidgets.QMessageBox.information(None, "Цвета флага", message)

    def get_selected_color(self, button_group):
        for button in button_group.buttons():
            if button.isChecked():
                return button.text()
        return "Не выбран"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())