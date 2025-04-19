import sys
from PyQt6 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 587)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 20, 341, 471))
        self.calendarWidget.setObjectName("calendarWidget")

        self.timeEdit = QtWidgets.QTimeEdit(parent=self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(0, 0, 341, 21))
        self.timeEdit.setObjectName("timeEdit")

        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(340, 0, 371, 541))
        self.listWidget.setObjectName("listWidget")

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 493, 341, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Enter event name")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 510, 341, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Добавить событие")
        self.pushButton.clicked.connect(self.add_event)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Минипланировщик"))

    def add_event(self):
        date = self.calendarWidget.selectedDate()
        time = self.timeEdit.time()
        event_name = self.lineEdit.text()

        if event_name:
            event_datetime = QtCore.QDateTime(date, time)
            event_text = f"{event_datetime.toString('yyyy-MM-dd HH:mm')} - {event_name}"
            self.listWidget.addItem(event_text)
            self.sort_events()

    def sort_events(self):
        events = []
        for index in range(self.listWidget.count()):
            events.append(self.listWidget.item(index).text())
        events.sort()
        self.listWidget.clear()
        self.listWidget.addItems(events)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())