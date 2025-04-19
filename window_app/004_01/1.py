import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QSlider, QPushButton, QFileDialog, QWidget, QMessageBox
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from PIL import Image

class TransparencyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Регулировка прозрачности изображения")
        self.setGeometry(100, 100, 600, 600)

        self.original_image = None
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.setValue(255)  
        self.slider.valueChanged.connect(self.update_transparency)
        self.slider.setEnabled(False) 

        self.open_button = QPushButton("Открыть изображение", self)
        self.open_button.clicked.connect(self.open_image)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.slider)
        layout.addWidget(self.open_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_image(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Открыть изображение", "", "Image Files (*.png *.jpg *.bmp)")
            if file_path:
                self.original_image = Image.open(file_path).convert("RGBA")  # Открытие изображения с поддержкой альфа-канала
                self.slider.setEnabled(True)  # Включаем слайдер после загрузки изображения
                self.update_transparency()  # Обновляем изображение с текущим уровнем прозрачности
        except Exception as e:
            
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть изображение: {e}")

    def update_transparency(self):
        try:
            if self.original_image is None:
                return

            alpha_value = self.slider.value()

            image = self.original_image.copy()
            alpha = Image.new("L", image.size, alpha_value) 
            image.putalpha(alpha)  

            data = image.tobytes("raw", "BGRA")
            qt_image = QImage(data, image.width, image.height, QImage.Format.Format_ARGB32)

            self.image_label.setPixmap(QPixmap.fromImage(qt_image))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось обновить изображение: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransparencyApp()
    window.show()
    sys.exit(app.exec())