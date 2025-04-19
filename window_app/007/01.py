import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QComboBox, QPushButton, QWidget, QHeaderView
)
from PyQt5.QtGui import QColor


class OlympicsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Результаты олимпиады")
        self.resize(800, 600)

        # Основной виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Выпадающие списки для фильтров
        self.school_filter = QComboBox()
        self.class_filter = QComboBox()
        self.school_filter.addItem("Все школы")
        self.class_filter.addItem("Все классы")
        self.layout.addWidget(self.school_filter)
        self.layout.addWidget(self.class_filter)

        # Кнопка применения фильтров
        self.filter_button = QPushButton("Показать результаты")
        self.layout.addWidget(self.filter_button)

        # Таблица для отображения данных
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # События
        self.filter_button.clicked.connect(self.apply_filters)

        # Загрузка данных
        self.data = []
        self.schools = set()
        self.classes = set()
        self.load_data("rez.csv")
        self.populate_filters()
        self.display_data(self.data)

    def load_data(self, file_path):
        # Загрузка данных из CSV
        file_path = "/Users/svetatugay/PythonProjects/OAP/window_app/007/rez.csv"
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.data = list(reader)

        # Извлечение уникальных школ и классов
        for row in self.data:
            login = row["login"]
            school, class_ = login.split("-")[2:4]
            self.schools.add(school)
            self.classes.add(class_)

    def populate_filters(self):
        # Заполнение фильтров уникальными значениями
        self.school_filter.addItems(sorted(self.schools))
        self.class_filter.addItems(sorted(self.classes))

    def apply_filters(self):
        # Применение фильтров к данным
        school = self.school_filter.currentText()
        class_ = self.class_filter.currentText()

        filtered_data = self.data
        if school != "Все школы":
            filtered_data = [row for row in filtered_data if row["login"].split("-")[2] == school]
        if class_ != "Все классы":
            filtered_data = [row for row in filtered_data if row["login"].split("-")[3] == class_]

        self.display_data(filtered_data)

    def display_data(self, data):
        # Отображение данных в таблице
        self.table.clear()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Логин", "ФИО", "Сумма баллов"])
        self.table.setRowCount(len(data))

        # Заполнение таблицы
        for row_index, row in enumerate(data):
            self.table.setItem(row_index, 0, QTableWidgetItem(row["login"]))
            self.table.setItem(row_index, 1, QTableWidgetItem(row["user_name"]))
            self.table.setItem(row_index, 2, QTableWidgetItem(row["Score"]))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Подсветка призёров
        self.highlight_winners(data)

    def highlight_winners(self, data):
        # Подсветка первых трёх мест
        # Сортировка по сумме баллов
        sorted_data = sorted(data, key=lambda x: int(x["Score"]), reverse=True)

        # Определение мест
        places = {}
        current_place = 1
        previous_score = None

        for row in sorted_data:
            score = int(row["Score"])
            if score != previous_score:
                current_place = len(places) + 1
            places[row["login"]] = current_place
            previous_score = score
# Подсветка строк
        for row_index in range(self.table.rowCount()):
            login = self.table.item(row_index, 0).text()
            place = places.get(login, 0)

            if place == 1:
                self.color_row(row_index, QColor(255, 215, 0))  # Золото
            elif place == 2:
                self.color_row(row_index, QColor(192, 192, 192))  # Серебро
            elif place == 3:
                self.color_row(row_index, QColor(205, 127, 50))  # Бронза

    def color_row(self, row_index, color):
        # Окрашивание строки таблицы
        for col_index in range(self.table.columnCount()):
            self.table.item(row_index, col_index).setBackground(color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OlympicsApp()
    window.show()
    sys.exit(app.exec_())
