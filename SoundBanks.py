import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QInputDialog, QTableWidgetItem
from player_buttons import PlayerButtons
from PyQt5.QtGui import QIcon


class SoundBank(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("SoundBank.ui", self)
        self.change_sound = PlayerButtons()
        self.setWindowTitle("Банк звуков")
        self.setWindowIcon(QIcon("iconca.png"))
        self.con = sqlite3.connect('SoundsBank.db')
        self.cur = self.con.cursor()
        self.output()

    def on_add_sound_clicked(self):
        path, ok = QInputDialog.getText(self, 'Добавление звука',
                                        'Введите расположение файла:')
        if ok:
            name, ok_2 = QInputDialog.getText(self, 'Добавление звука',
                                              'Введите название звука:')
            if ok_2:
                inpt_string = f"INSERT INTO Sounds(name, PATHs_sounds) VALUES({str(name)},{str(path)})"
                self.cur.execute(inpt_string)
                self.con.commit()
                self.output()

    def on_del_sound_clicked(self):
        _id, ok = QInputDialog.getText(self, 'Удаление звука',
                                        'Введите id файла:')
        if ok:
            inpt_string = f"DELETE from Sounds WHERE ID == {int(_id)}"
            self.cur.execute(inpt_string)
            self.con.commit()
            self.output()

    def output(self):
        result = self.cur.execute("Select name, PATHs_sounds from Sounds").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
