import numpy as np
import matplotlib.pyplot as plt
# from audioFingerprint import fingerprint
from tools.audioReader import AudioReader
from tools.STFT import STFT

filename = '/home/zyyf/audioFingerprint/mp3/Brad-Sucks--Total-Breakdown.mp3'

## Read audio
#############################################
print 'Read audio......'
print ''
audioReader = AudioReader(filename=filename)
audioData = audioReader.audioData
audioData_1_ch = np.mean(audioData, axis=1)

## test fingerprint
#############################################
# print 'Calulate fingerprint......'
# print ''
# fingerprint = fingerprint(audioData_1_ch)
# fingerprint_list = list(fingerprint)


## test audio 2D spectrum
##############################################
print 'Calulate audio 2D apectrum.......'
print ''
stft = STFT()
spectrum = stft.get_2D_spectrum(audioData_1_ch)
plt.imshow(spectrum)
plt.show()

print ''