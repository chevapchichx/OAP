from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageQt
import sys

class ImageEditorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image = None
        self.original_image = None
        self.load_image()
        
    def initUI(self):
        self.setWindowTitle("PIL 2.0")
        self.setGeometry(100, 100, 600, 500)
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 113, 221))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        
        self.red_button = QtWidgets.QPushButton("R", self.verticalLayoutWidget)
        self.red_button.clicked.connect(lambda: self.apply_color_filter("R"))
        self.verticalLayout.addWidget(self.red_button)
        
        self.green_button = QtWidgets.QPushButton("G", self.verticalLayoutWidget)
        self.green_button.clicked.connect(lambda: self.apply_color_filter("G"))
        self.verticalLayout.addWidget(self.green_button)
        
        self.blue_button = QtWidgets.QPushButton("B", self.verticalLayoutWidget)
        self.blue_button.clicked.connect(lambda: self.apply_color_filter("B"))
        self.verticalLayout.addWidget(self.blue_button)
        
        self.all_button = QtWidgets.QPushButton("ALL", self.verticalLayoutWidget)
        self.all_button.clicked.connect(lambda: self.apply_color_filter("ALL"))
        self.verticalLayout.addWidget(self.all_button)
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 330, 481, 80))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        
        self.rotate_left_button = QtWidgets.QPushButton("Против часовой стрелки", self.horizontalLayoutWidget)
        self.rotate_left_button.clicked.connect(lambda: self.rotate_image(-90))
        self.horizontalLayout.addWidget(self.rotate_left_button)
        
        self.rotate_right_button = QtWidgets.QPushButton("По часовой стрелке", self.horizontalLayoutWidget)
        self.rotate_right_button.clicked.connect(lambda: self.rotate_image(90))
        self.horizontalLayout.addWidget(self.rotate_right_button)
        
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(QtCore.QRect(160, 40, 300, 300))
        self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
    def load_image(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать изображение", "", "Images (*.png *.xpm *.jpg *.jpeg)")
        if file_name:
            self.image = Image.open(file_name)
            self.image = self.image.convert("RGB")
            self.original_image = self.image.copy()
            self.display_image()
            
    def display_image(self):
        if self.image:
            qt_image = ImageQt.ImageQt(self.image)
            pixmap = QtGui.QPixmap.fromImage(qt_image)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio))
            
    def apply_color_filter(self, color):
        if not self.image:
            return
        
        self.image = self.original_image.copy()
        r, g, b = self.image.split()
        
        if color == "R":
            self.image = Image.merge("RGB", (r, Image.new("L", r.size), Image.new("L", r.size)))
        elif color == "G":
            self.image = Image.merge("RGB", (Image.new("L", g.size), g, Image.new("L", g.size)))
        elif color == "B":
            self.image = Image.merge("RGB", (Image.new("L", b.size), Image.new("L", b.size), b))
        elif color == "ALL":
            self.image = self.original_image.copy()
            
        self.display_image()
    
    def rotate_image(self, angle):
        if not self.image:
            return
            
        self.image = self.image.rotate(angle, expand=True)
        self.display_image()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = ImageEditorApp()
    mainWindow.show()
    sys.exit(app.exec())