import numpy as np
import matplotlib.mlab as mlab

class STFT:
    def __init__(self, default_fs=44100, default_window_size=4096,
                 default_overlap_ratio=0.5):
        ######################################################################
        # Sampling rate, related to the Nyquist conditions, which affects
        # the range frequencies we can detect.
        self.DEFAULT_FS = default_fs

        ######################################################################
        # Size of the FFT window, affects frequency granularity
        self.DEFAULT_WINDOW_SIZE = default_window_size

        ######################################################################
        # Ratio by which each sequential window overlaps the last and the
        # next window. Higher overlap will allow a higher granularity of offset
        # matching, but potentially more fingerprints.
        self.DEFAULT_OVERLAP_RATIO = default_overlap_ratio

    def get_2D_spectrum(self, channel_samples):
        """
        FFT the channel, log transform output
        """
        # FFT the signal and extract frequency components
        arr2D = mlab.specgram(
            channel_samples,
            NFFT=self.DEFAULT_WINDOW_SIZE,
            Fs=self.DEFAULT_FS,
            window=mlab.window_hanning,
            noverlap=int(self.DEFAULT_WINDOW_SIZE * self.DEFAULT_OVERLAP_RATIO))[0]

        # apply log transform since specgram() returns linear array
        arr2D = 10 * np.log10(arr2D)
        arr2D[arr2D == -np.inf] = 0  # replace infs with zeros
        return arr2D