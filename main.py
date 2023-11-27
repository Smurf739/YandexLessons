import random

from UI import *
from PyQt5 import QtWidgets
import sys


class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()
        self.check_db = None
        self.base_line_edit = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ellipse)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphics_view = QtWidgets.QGraphicsView(self.ui.centralwidget)
        self.graphics_view.setScene(self.scene)
        self.graphics_view.setGeometry(290, 100, 200, 200)
        self.graphics_view.setAlignment(Qt.AlignCenter)

    def ellipse(self):
        self.scene.clear()

        diametr = random.randint(50, 187)
        rect = QtCore.QRectF(0, 0, diametr, diametr)
        color = Qt.GlobalColor(random.randint(1, 18))
        self.scene.addEllipse(rect, QtGui.QPen(color), QtGui.QBrush(color))
        if color == 3:
            self.scene.clear()
            self.scene.addText("Белый круг")



app = QtWidgets.QApplication(sys.argv)
mywin = Interface()
mywin.show()
sys.exit(app.exec_())
