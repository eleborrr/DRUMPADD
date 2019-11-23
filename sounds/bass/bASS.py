import player
import sys
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('bass.ui', self)
        self.load_mp3('/Users/esrev/PycharmProjects/MIDI_instr/bass/01.wav')
        self.load_mp3_2('/Users/esrev/PycharmProjects/MIDI_instr/bass/02.wav')
        self.load_mp3_3('/Users/esrev/PycharmProjects/MIDI_instr/bass/03.wav')
        self.load_mp3_4('/Users/esrev/PycharmProjects/MIDI_instr/bass/04.wav')

    def nothing(self):
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            # self.pushButton_1.click()
            self.player.stop()
            self.player.play()
        elif event.key() == Qt.Key_W:
            # self.pushButton_2.clicked.connect(self.nothing)
            self.player_2.stop()
            self.player_2.play()
        elif event.key() == Qt.Key_E:
            # self.pushButton_3.click()
            self.player_3.stop()
            self.player_3.play()
        elif event.key() == Qt.Key_R:
            # self.pushButton_4.click()
            self.player_4.stop()
            self.player_4.play()


    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def load_mp3_2(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_2 = QtMultimedia.QMediaPlayer()
        self.player_2.setMedia(content)

    def load_mp3_3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_3 = QtMultimedia.QMediaPlayer()
        self.player_3.setMedia(content)

    def load_mp3_4(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_4 = QtMultimedia.QMediaPlayer()
        self.player_4.setMedia(content)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())