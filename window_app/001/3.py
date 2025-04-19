import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Миникалькулятор')
        self.resize(400, 400)

        self.num1 = QLineEdit(self)
        self.num1.setPlaceholderText('Первое число(целое)')

        self.num2 = QLineEdit(self)
        self.num2.setPlaceholderText('Первое число(целое)')

        self.calc_button = QPushButton('→', self)
        self.calc_button.clicked.connect(self.calc_res)

        self.sum_l = QLabel('Сумма:', self)
        self.diff_l = QLabel('Разность:', self)
        self.prod_l = QLabel('Произведение:', self)
        self.div_l = QLabel('Частное:', self)

        self.sum_res = QLCDNumber(self)
        self.diff_res = QLCDNumber(self)
        self.prod_res = QLCDNumber(self)
        self.div_res = QLCDNumber(self)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.num1)
        input_layout.addWidget(self.num2)
        input_layout.addWidget(self.calc_button)

        result_layout = QVBoxLayout()
        result_layout.addWidget(self.sum_l)
        result_layout.addWidget(self.sum_res)
        result_layout.addWidget(self.diff_l)
        result_layout.addWidget(self.diff_res)
        result_layout.addWidget(self.prod_l)
        result_layout.addWidget(self.prod_res)
        result_layout.addWidget(self.div_l)
        result_layout.addWidget(self.div_res)

        main_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(result_layout)

        self.setLayout(main_layout)

    def calc_res(self):
            first_num = int(self.num1.text())
            second_num = int(self.num2.text())

            sum_res = first_num + second_num
            diff_res = first_num - second_num
            prod_res = first_num * second_num

            if second_num != 0:
                div_res = first_num / second_num
            else:
                div_res = 'Ошибка'

            self.sum_res.display(sum_res)
            self.diff_res.display(diff_res)
            self.prod_res.display(prod_res)

            if div_res == 'Ошибка':
                self.div_res.display('Err')
            else:
                self.div_res.display(div_res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())