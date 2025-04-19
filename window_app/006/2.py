import sys
import csv
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QSpinBox, QLabel, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Осторожно: дорого!")
        self.setGeometry(100, 100, 600, 400)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Название", "Цена", "Количество"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
 
        self.total_label = QLabel("Итого: 0.00")
        self.total_label.setAlignment(Qt.AlignRight)

        self.update_button = QPushButton("Обновить")
        self.update_button.setFixedSize(90, 30)
        self.update_button.clicked.connect(self.update_total)

        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.update_button)
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(self.total_label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(table_layout)
        main_layout.addLayout(bottom_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.load_data()

    def load_data(self):
        with open('/Users/svetatugay/PythonProjects/OAP/window_app/006/price.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader) 
            for row in reader:
                if row:
                    self.add_row(row[0], float(row[1]))

        self.sort_table_by_price()

        self.highlight_top_5()

    def add_row(self, name, price):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        self.table.setItem(row_position, 0, QTableWidgetItem(name))
        self.table.setItem(row_position, 1, QTableWidgetItem(f"{price:.2f}"))

        spin_box = QSpinBox()
        spin_box.setValue(0)
        self.table.setCellWidget(row_position, 2, spin_box)

    def sort_table_by_price(self):
        self.table.sortItems(1, Qt.DescendingOrder)

    def highlight_top_5(self):
        colors = [QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(5)]
        for row in range(min(5, self.table.rowCount())):
            color = colors[row]
            for col in range(3): 
                item = self.table.item(row, col)
                if item is not None:
                    item.setBackground(color)
            spin_box = self.table.cellWidget(row, 2)
            if spin_box is not None:
                spin_box.setStyleSheet(f"background-color: {color.name()};")

    def update_total(self):
        total = 0
        for row in range(self.table.rowCount()):
            price_item = self.table.item(row, 1)
            price = float(price_item.text())
            quantity = self.table.cellWidget(row, 2).value()
            total += price * quantity
        self.total_label.setText(f"Итого: {total:.2f}")

        self.highlight_top_5()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())