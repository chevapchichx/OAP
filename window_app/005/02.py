import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QMainWindow)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class SquareLens(QWidget):
    def __init__(self):
        super().__init__()
        self.k = 0.9  # Начальный коэффициент масштабирования
        self.n = 10   # Начальное количество итераций
        self.points = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Квадрат-объектив")

        # Основной вертикальный макет
        vbox = QVBoxLayout()

        # Горизонтальный макет для элементов управления
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("k = "))
        self.k_input = QLineEdit(str(self.k))
        hbox.addWidget(self.k_input)
        hbox.addWidget(QLabel("n = "))
        self.n_input = QLineEdit(str(self.n))
        hbox.addWidget(self.n_input)
        self.draw_button = QPushButton("Рисовать")
        self.draw_button.clicked.connect(self.draw_spiral)
        hbox.addWidget(self.draw_button)
        vbox.addLayout(hbox)

        # Добавление холста для рисования
        self.canvas = QWidget()
        vbox.addWidget(self.canvas)

        self.setLayout(vbox)

    def draw_spiral(self):
        try:
            self.k = float(self.k_input.text())
            if not 0 < self.k < 1:
                raise ValueError("Коэффициент k должен быть в диапазоне (0, 1)")
            self.n = int(self.n_input.text())
            if self.n <= 0:
                raise ValueError("Количество итераций n должно быть положительным числом")
            self.points = self.generate_points()
            self.update()  # Запуск перерисовки
        except ValueError as e:
            print(f"Error: {e}")

    def generate_points(self):
        size = min(self.width(), self.height())
        center_x = self.width() / 2
        center_y = self.height() / 2
        side = size * 0.8  # Размер квадрата

        points = [[center_x - side / 2, center_y - side / 2],
                  [center_x + side / 2, center_y - side / 2],
                  [center_x + side / 2, center_y + side / 2],
                  [center_x - side / 2, center_y + side / 2]]

        all_points = [points]

        for _ in range(self.n):
            new_points = []
            for i in range(4):
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % 4]
                new_x = x1 + (x2 - x1) * self.k
                new_y = y1 + (y2 - y1) * self.k
                new_points.append([new_x, new_y])
            points = new_points
            all_points.append(points)

        return all_points

    def paintEvent(self, event):
        # Настройка QPainter для рисования на текущем виджете
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor("red"), 1, Qt.SolidLine)
        painter.setPen(pen)

        if self.points:
            for square in self.points:
                for i in range(4):
                    x1, y1 = square[i]
                    x2, y2 = square[(i + 1) % 4]
                    painter.drawLine(int(x1), int(y1), int(x2), int(y2))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = SquareLens()
        self.setCentralWidget(self.central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec_())