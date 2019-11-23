from PyQt5 import QtCore, QtMultimedia


class PlayerButtons():
    def __init__(self):
        super().__init__()
        self.lst_sounds = {}
        self.index_buttons = {"Q": 81, "W": 87, "E": 69, "R": 82, "A": 65, "S": 83, "D": 68, "F": 70,
                              "Z": 90, "X": 88, "C": 67, "V": 86}
        self.load_mp3('01.wav', 81)
        self.load_mp3('02.wav', 87)
        self.load_mp3('03.wav', 69)
        self.load_mp3('04.wav', 82)
        self.load_mp3('bochka.wav', 65)
        self.load_mp3('hi-hat.wav', 83)
        self.load_mp3('Crash Cymbal.mp3', 68)
        self.load_mp3('midtom.wav', 70)
        self.load_mp3('do.mp3', 90)
        self.load_mp3('mi.mp3', 88)
        self.load_mp3('sol.mp3', 67)
        self.load_mp3('si.mp3', 86)

    # создание плеера и добавление проигрывателя звука в словарь

    def load_mp3(self, filename, indx):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        self.lst_sounds[indx] = player

    # замена звука

    def change_sound(self, button, file):
        media = QtCore.QUrl.fromLocalFile(file[0][2:])
        content = QtMultimedia.QMediaContent(media)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        self.lst_sounds[self.index_buttons[button]] = player
        player.play()
        return self.lst_sounds

    def return_sounds(self):
        return self.lst_sounds, self.index_buttons
