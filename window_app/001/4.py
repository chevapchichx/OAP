import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QLineEdit, QLabel


class HideWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Прятки для виджетов')
        self.setGeometry(100, 100, 400, 200)

        self.checkbox1 = QCheckBox('edit1', self)
        self.checkbox2 = QCheckBox('edit2', self)
        self.checkbox3 = QCheckBox('edit3', self)
        self.checkbox4 = QCheckBox('edit4', self)

        self.edit1 = QLineEdit('Поле edit1', self)
        self.edit2 = QLineEdit('Поле edit2', self)
        self.edit3 = QLineEdit('Поле edit3', self)
        self.edit4 = QLineEdit('Поле edit4', self)

        self.checkbox1.setChecked(True)
        self.checkbox2.setChecked(True)
        self.checkbox3.setChecked(True)
        self.checkbox4.setChecked(True)

        self.checkbox1.stateChanged.connect(self.widget_visibility)
        self.checkbox2.stateChanged.connect(self.widget_visibility)
        self.checkbox3.stateChanged.connect(self.widget_visibility)
        self.checkbox4.stateChanged.connect(self.widget_visibility)

        layout = QVBoxLayout()

        row1 = QHBoxLayout()
        row1.addWidget(self.checkbox1)
        row1.addWidget(self.edit1)
        layout.addLayout(row1)

        row2 = QHBoxLayout()
        row2.addWidget(self.checkbox2)
        row2.addWidget(self.edit2)
        layout.addLayout(row2)

        row3 = QHBoxLayout()
        row3.addWidget(self.checkbox3)
        row3.addWidget(self.edit3)
        layout.addLayout(row3)

        row4 = QHBoxLayout()
        row4.addWidget(self.checkbox4)
        row4.addWidget(self.edit4)
        layout.addLayout(row4)

        self.setLayout(layout)

    def widget_visibility(self):
        self.edit1.setVisible(self.checkbox1.isChecked())
        self.edit2.setVisible(self.checkbox2.isChecked())
        self.edit3.setVisible(self.checkbox3.isChecked())
        self.edit4.setVisible(self.checkbox4.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HideWidgets()
    window.show()
    sys.exit(app.exec_())