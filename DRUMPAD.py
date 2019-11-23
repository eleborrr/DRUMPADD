import player
import sys
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('drumpad.ui', self)
        self.lst_sounds = []
        self.load_mp3('/Users/esrev/PycharmProjects/MIDI_instr/bass/01.wav')
        self.load_mp3_2('/Users/esrev/PycharmProjects/MIDI_instr/bass/02.wav')
        self.load_mp3_3('/Users/esrev/PycharmProjects/MIDI_instr/bass/03.wav')
        self.load_mp3_4('/Users/esrev/PycharmProjects/MIDI_instr/bass/04.wav')

    def nothing(self):
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.player.stop()
            self.player.play()
        elif event.key() == Qt.Key_W:
            self.player_2.stop()
            self.player_2.play()
        elif event.key() == Qt.Key_E:
            self.player_3.stop()
            self.player_3.play()
        elif event.key() == Qt.Key_R:
            self.player_4.stop()
            self.player_4.play()

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        self.lst_sounds.append(player)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())