import pyaudio
import wave

# Define the parameters for recording
FORMAT = pyaudio.paInt32  # 32-bit resolution
CHANNELS = 1             # 1 channel (mono)
RATE = 44100              # 44.1kHz sampling rate
CHUNK = 1024              # 2^10 samples for buffer
RECORD_SECONDS = 5        # Duration of recording
DEVICE_INDEX = 0
OUTPUT_FILENAME = "output.wav"  # Output filename

# Create an interface to PortAudio
audio = pyaudio.PyAudio()
print("----------------------record device list---------------------")
info = audio.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name'))

print("-------------------------------------------------------------")
# Open a new stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK, input_device_index= DEVICE_INDEX)

print("Recording...")

# Initialize array to store frames
frames = []

# Store data in chunks for the specified duration
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# Stop and close the stream
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
audio.terminate()

# Save the recorded data as a .wav file
waveFile = wave.open(OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

print(f"Audio saved to {OUTPUT_FILENAME}")
