import sys
import pandas as pd
import requests
from io import StringIO
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QTableWidget, QTableWidgetItem, QLineEdit, QLabel
)
from PyQt5.QtGui import QColor

class TitanicSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поиск на Титанике")
        self.setGeometry(200, 200, 800, 600)

        # Загрузка данных
        self.data = self.load_data()
        self.filtered_data = self.data.copy()

        # Основной виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной layout
        layout = QVBoxLayout()

        # Поле поиска
        self.search_label = QLabel("Подстрока для поиска:")
        layout.addWidget(self.search_label)
        self.search_field = QLineEdit()
        self.search_field.textChanged.connect(self.update_table)
        layout.addWidget(self.search_field)

        # Таблица
        self.table = QTableWidget()
        layout.addWidget(self.table)

        central_widget.setLayout(layout)

        # Инициализация таблицы
        self.update_table()

    def load_data(self):
        """
        Загрузка данных из удаленного файла.
        """
        url = "https://yastatic.net/s3/lyceum/content/problems/qt6/titanic.csv"
        response = requests.get(url)
        response.raise_for_status()  # Проверка успешности запроса
        csv_data = StringIO(response.text)
        return pd.read_csv(csv_data)

    def update_table(self):
        # Получение текста из поля поиска
        search_text = self.search_field.text()

        # Фильтрация данных
        if len(search_text) >= 3:
            self.filtered_data = self.data[self.data['Name'].str.contains(search_text, case=False, na=False)]
        else:
            self.filtered_data = self.data

        # Обновление таблицы
        self.table.setRowCount(len(self.filtered_data))
        self.table.setColumnCount(len(self.filtered_data.columns))
        self.table.setHorizontalHeaderLabels(self.filtered_data.columns)

        for row_idx, row in self.filtered_data.iterrows():
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                # Установка цвета строки
                if row['Survived'] == 1:  # Если выжил
                    item.setBackground(QColor(200, 255, 200))  # Зеленый цвет
                else:  # Если погиб
                    item.setBackground(QColor(255, 200, 200))  # Красный цвет
                self.table.setItem(row_idx, col_idx, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TitanicSearchApp()
    window.show()
    sys.exit(app.exec_())