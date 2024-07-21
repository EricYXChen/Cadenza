#https://www.youtube.com/watch?v=Aht4letBAmA

from scipy import signal
from scipy.io.wavfile import read
import numpy as np
import sounddevice as sd

sampling_rate = 44100
duration_in_seconds = 5
highpass = True
amplitude = 0.05

duration_in_samples = int(duration_in_seconds*sampling_rate)
a = read("output.wav")
white_noise = np.array(a[1], dtype=float)
input_signal = white_noise

print(input_signal)

cutoff_frequency = np.geomspace(20000, 20, input_signal.shape[0])
print(cutoff_frequency)
allpass_output = np.zeros_like(input_signal)

print(allpass_output)

dn_1 = 0

for n in range(input_signal.shape[0]):
    break_frequency = cutoff_frequency[n]
    tan = np.tan(np.pi*break_frequency/sampling_rate)
    a1 = (tan - 1)/ (tan + 1)
    allpass_output[n] = a1 * input_signal[n] + dn_1
    dn_1 = input_signal[n] - a1 * allpass_output[n]

if highpass:
    allpass_output *= -1

filter_output = input_signal + allpass_output

filter_output *=0.5

filter_output *= amplitude

sd.play(filter_output, sampling_rate)
sd.wait()



