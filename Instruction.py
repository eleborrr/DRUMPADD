from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui, QtCore
from PyQt5 import uic
from PyQt5.QtGui import QIcon


class Instruction(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("instruction.ui", self)
        self.setWindowTitle("Инструкция")
        self.setWindowIcon(QIcon("iconca.png"))
        self.setFixedSize(550, 550)
        pixmap_1 = QtGui.QPixmap("Instruction_01.png")
        pixmap_2 = QtGui.QPixmap("Instruction_02.png")
        pixmap_3 = QtGui.QPixmap("Instruction_03.png")
        pixmap_4 = QtGui.QPixmap("Instruction_04.png")
        pixmap_5 = QtGui.QPixmap("Instruction_05.png")
        self.label.setPixmap(pixmap_1.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.label_2.setPixmap(pixmap_2.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.label_3.setPixmap(pixmap_3.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.label_4.setPixmap(pixmap_4.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.label_5.setPixmap(pixmap_5.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))
