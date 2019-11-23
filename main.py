import sys
import pyautogui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QWidget
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from Instruction import Instruction
from player_buttons import PlayerButtons
from Recorder import Record
from SoundBanks import SoundBank


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('drumpad.ui', self)
        self.setWindowTitle("DRUMPAD")

        # инициализация объектов других классов
        self.instruction = Instruction()
        self.error = RecordDialog()
        self.show_SoundBank = SoundBank()
        self.PlayerButtons_obj = PlayerButtons()

        # получение словаря, где кодам букв соответствует звук, а также словаря, где хранятся коды на каждую букву
        self.dict_sounds, self.dict_sounds_indx = self.PlayerButtons_obj.return_sounds()

        # Словарь с координатами перетаскивания мыши во время нажатий по клавиатуре
        self.mouse_click_indx = {81: (112, 226), 87: (215, 226),
                                 69: (319, 226), 82: (422, 226), 65: (111, 304),
                                 83: (215, 304), 68: (319, 304), 70: (422, 304),
                                 90: (111, 362), 88: (215, 362), 67: (319, 362),
                                 86: (422, 362)}

        # Обработка нажатий по кнопкам

        self.change_sound_button.clicked.connect(self.change_sound)
        self.record_button.clicked.connect(self.record)
        self.move_mouse_button.clicked.connect(self.move_mouse)

        self.mouse_move = True

        # инициализация нажатий клавишой мышки по играбельным кнопкам:

    def on_pushButton_clicked(self):
        self.dict_sounds[81].stop()
        self.dict_sounds[81].play()

    def on_pushButton_2_clicked(self):
        self.dict_sounds[87].stop()
        self.dict_sounds[87].play()

    def on_pushButton_7_clicked(self):
        self.dict_sounds[69].stop()
        self.dict_sounds[69].play()

    def on_pushButton_16_clicked(self):
        self.dict_sounds[82].stop()
        self.dict_sounds[82].play()

    def on_pushButton_12_clicked(self):
        self.dict_sounds[65].stop()
        self.dict_sounds[65].play()

    def on_pushButton_11_clicked(self):
        self.dict_sounds[83].stop()
        self.dict_sounds[83].play()

    def on_pushButton_10_clicked(self):
        self.dict_sounds[68].stop()
        self.dict_sounds[68].play()

    def on_pushButton_15_clicked(self):
        self.dict_sounds[70].stop()
        self.dict_sounds[70].play()

    def on_pushButton_5_clicked(self):
        self.dict_sounds[90].stop()
        self.dict_sounds[90].play()

    def on_pushButton_3_clicked(self):
        self.dict_sounds[88].stop()
        self.dict_sounds[88].play()

    def on_pushButton_6_clicked(self):
        self.dict_sounds[67].stop()
        self.dict_sounds[67].play()

    def on_pushButton_14_clicked(self):
        self.dict_sounds[86].stop()
        self.dict_sounds[86].play()

    def move_mouse(self):
        if self.mouse_move:
            self.mouse_move = False
            self.move_mouse_button.setText("Перемещать мышку")
        else:
            self.mouse_move = True
            self.move_mouse_button.setText("Не перемещать мышку")

    # Инициализация нажатий по кликабельным клавишам на клавиатуре

    def keyPressEvent(self, event):
        if event.key() in self.dict_sounds_indx.values():
            self.dict_sounds[event.key()].stop()
            self.dict_sounds[event.key()].play()
            pos = self.frameGeometry()
            # print(pos.top())
            if self.mouse_move:
                pyautogui.moveTo(self.mouse_click_indx[event.key()][0] + pos.left(),
                                 self.mouse_click_indx[event.key()][1] + pos.top())

    def change_sound(self):
        i, okBtnPressed = QInputDialog.getItem(self, "Выберите кнопку", "",
                                               ("Q", "W", "E", "R", "A", "S", "D", "F", "Z", "X", "C", "V"),
                                               1, False)
        if okBtnPressed:
            fname = QFileDialog.getOpenFileName(self, "Выбрать Аудио")
            self.dict_sounds = self.PlayerButtons_obj.change_sound(i, fname)

    def record(self):
        name, okBtnPressed = QInputDialog.getText(self, 'Введите название файла',
                                                  'Название:')
        if okBtnPressed:
            time_, okBtnPressed2 = QInputDialog.getText(self, 'Введите длительность файла',
                                                        'Длительность:')
            if okBtnPressed2:
                flag = True
                digits = '0123456789'
                for i in time_:
                    if i not in digits:
                        flag = False
                        break
                if flag:
                    self.is_recording.setText("Идет запись!")
                    Record(name, int(time_))
                else:
                    self.error.show()

    def on_toolButton_2_clicked(self):
        self.instruction.show()

    def on_toolButton_clicked(self):
        self.show_SoundBank.show()


class RecordDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 280)
        self.setWindowIcon(QIcon("iconca.png"))
        uic.loadUi("error.ui", self)
        self.setWindowTitle("Неправильно введено время!")


app = QApplication(sys.argv)
ex = Main()
ex.setFixedSize(540, 500)
ex.move(0, 0)
ex.show()
ex.setWindowIcon(QIcon("iconca.png"))
sys.exit(app.exec_())
