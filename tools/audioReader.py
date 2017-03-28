import numpy as np
import audioread
import pygame


class AudioReader:
    def __init__(self, filename):
        self.channels = 1
        self.sampleRate = 0
        self.duration = 0
        self.audioData = self._read_audio(filename)

    def _read_audio(self, filename):
        data = ''
        with audioread.audio_open(filename) as f:
            self.channels = f.channels
            self.sampleRate = f.samplerate,
            self.duration = f.duration

            for buf in f:
                data += buf
            data_array = np.fromstring(data, dtype='int16')
            if self.channels == 2:
                data_array = data_array.reshape((len(data_array) / 2, 2))
        return data_array

    def play_audio(self, audio_array, sampleRate=44100, channels=2):
        pygame.init()
        # 44100 Hz, 16bit, 2 channels
        pygame.mixer.init(sampleRate, -16, channels)
        sound = pygame.sndarray.make_sound(audio_array)
        sound.play()

    def write_audio(self, filename):
        pass
