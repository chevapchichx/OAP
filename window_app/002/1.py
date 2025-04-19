import sys
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import math


class Ui_Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            '/Users/svetatugay/PythonProjects/OAP/window_app/002/1.ui', self)
        self.UI_num_table()
        self.current_expression = ""
        self.last_was_operator = False

    def UI_num_table(self):
        self.btn0.clicked.connect(self.append_num)
        self.btn1.clicked.connect(self.append_num)
        self.btn2.clicked.connect(self.append_num)
        self.btn3.clicked.connect(self.append_num)
        self.btn4.clicked.connect(self.append_num)
        self.btn5.clicked.connect(self.append_num)
        self.btn6.clicked.connect(self.append_num)
        self.btn7.clicked.connect(self.append_num)
        self.btn8.clicked.connect(self.append_num)
        self.btn9.clicked.connect(self.append_num)
        self.btn_plus.clicked.connect(self.append_operator)
        self.btn_minus.clicked.connect(self.append_operator)
        self.btn_mult.clicked.connect(self.append_operator)
        self.btn_div.clicked.connect(self.append_operator)
        self.btn_eq.clicked.connect(self.calculate_result)
        self.btn_clear.clicked.connect(self.clear_display)
        self.btn_dot.clicked.connect(self.append_num)
        self.btn_sqrt.clicked.connect(self.calculate_sqrt)
        self.btn_pow.clicked.connect(self.append_operator)

    def append_num(self):
        self.current_expression += self.sender().text()
        self.last_was_operator = False
        self.update_display()

    def append_operator(self):
        if not self.last_was_operator and self.current_expression:
            self.current_expression += self.sender().text()
            self.last_was_operator = True
            self.update_display()

    def update_display(self):
        if len(self.current_expression) > 12:
            display_text = self.current_expression[-12:]
        else:
            display_text = self.current_expression
        self.table.display(display_text)

    def calculate_result(self):
        try:
            result = eval(self.current_expression.replace('^', '**'))
            if isinstance(result, float):
                result = round(result, 8)
            self.current_expression = str(result)
            self.update_display()
        except Exception as e:
            self.table.display("Error")
            self.current_expression = ""

    def clear_display(self):
        self.current_expression = ""
        self.table.display(0)

    def calculate_sqrt(self):
        try:
            result = math.sqrt(float(self.current_expression))
            self.table.display(result)
            self.current_expression = str(result)
        except Exception as e:
            self.table.display("Error")
            self.current_expression = ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec())
