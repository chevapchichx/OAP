import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QInputDialog
from PyQt6.QtGui import QPixmap, QImage, QPainter, QColor
from PyQt6.QtCore import Qt

class FlagApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор флагов")
        self.setGeometry(100, 100, 800, 600)

        self.flag_label = QLabel(self)
        self.flag_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.generate_button = QPushButton("Сгенерировать флаг", self)
        self.generate_button.clicked.connect(self.generate_flag)

        layout = QVBoxLayout()
        layout.addWidget(self.flag_label)
        layout.addWidget(self.generate_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def generate_flag(self):
        num_colors, ok = QInputDialog.getInt(self, "Количество полос", "Введите количество полос:", min=1, max=20)
        if not ok:
            return

        width = 800
        height = 600

        flag_image = QImage(width, height, QImage.Format.Format_RGB32)

        stripe_height = height // num_colors

        painter = QPainter(flag_image)
        for i in range(num_colors):
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.fillRect(0, i * stripe_height, width, stripe_height, color)
        painter.end()

        pixmap = QPixmap.fromImage(flag_image)
        self.flag_label.setPixmap(pixmap.scaled(self.flag_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlagApp()
    window.show()
    sys.exit(app.exec())