import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen

class SmileWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.scale = 1.0  

    def set_scale(self, value):
        self.scale = value / 10  
        self.update() 

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(Qt.red, 2)
        painter.setPen(pen)

        center_x, center_y = self.width() // 2, self.height() // 2

        radius = int(100 * self.scale)

        painter.drawEllipse(center_x - radius, center_y - radius, 2 * radius, 2 * radius)

        eye_radius = int(20 * self.scale)
        eye_offset_x = int(40 * self.scale)
        eye_offset_y = int(30 * self.scale)
        painter.drawEllipse(center_x - eye_offset_x - eye_radius, center_y - eye_offset_y, 2 * eye_radius, 2 * eye_radius)
        painter.drawEllipse(center_x + eye_offset_x - eye_radius, center_y - eye_offset_y, 2 * eye_radius, 2 * eye_radius)

        mouth_width = int(80 * self.scale)
        mouth_height = int(30 * self.scale)
        painter.drawArc(center_x - mouth_width // 2, center_y + 10, mouth_width, mouth_height, 0, -180 * 16)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рост хорошего настроения")

        self.smile_widget = SmileWidget()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(5)  # минимальный масштаб (0.5x)
        self.slider.setMaximum(30)  # максимальный масштаб (3.0x)
        self.slider.setValue(10)  # начальное значение (1.0x)
        self.slider.valueChanged.connect(self.update_scale)

        layout = QVBoxLayout()
        layout.addWidget(self.smile_widget)
        layout.addWidget(self.slider)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_scale(self, value):
        self.smile_widget.set_scale(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 400)
    window.show()
    sys.exit(app.exec_())