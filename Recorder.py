import pyaudio
import wave
from threading import Thread


class RecordingFile(object):
    def __init__(self, fname):
        self.fname = fname
        self.mode = 'wb'
        self.channels = 1
        self.rate = 44100
        self.frames_per_buffer = 1024
        self._pa = pyaudio.PyAudio()
        self.wavefile = self._prepare_file(self.fname, self.mode)
        self._stream = None

    # открытие потока и его подготовка, запись

    def record(self, duration):
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.frames_per_buffer)
        for _ in range(int(self.rate / self.frames_per_buffer * duration)):
            audio = self._stream.read(self.frames_per_buffer)
            self.wavefile.writeframes(audio)
        return None

    # подготовка файла к сохранению

    def _prepare_file(self, fname, mode='wb'):
        wavefile = wave.open(fname, mode)
        wavefile.setnchannels(self.channels)
        wavefile.setsampwidth(self._pa.get_sample_size(pyaudio.paInt16))
        wavefile.setframerate(self.rate)
        return wavefile


class Record:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        Thread(target=self.recording).start()
        Thread(target=self.nothing).start()

    def recording(self):
        file = RecordingFile(f'{self.name}.wav')
        file.record(self.time)

    def nothing(self):
        pass
