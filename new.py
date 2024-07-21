import scipy.signal as signal
import scipy.io.wavfile as wavfile
import numpy as np

# Load the audio file
sample_rate, data = wavfile.read('output.wav')

print(sample_rate)

# High pass filter parameters
filter_order = 4
cutoff_frequency = 4000  # Adjust cutoff frequency as needed

# Nyquist frequency
nyquist = 0.5 * sample_rate

# High pass filter
b, a = signal.butter(filter_order, cutoff_frequency / nyquist, btype='low')

# Apply the filter to the audio data
filtered_data = signal.lfilter(b, a, data).astype(np.int16)

# Save the filtered audio
wavfile.write('output_highpass.wav', sample_rate, filtered_data)
