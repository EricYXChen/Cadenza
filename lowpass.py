import essentia.standard as es

# Load the audio file
audio_file = 'output.wav'
audio = es.MonoLoader(filename=audio_file)()

# Apply low-pass filter
cutoff_frequency = 200  # Set your cutoff frequency here
low_pass_filter = es.LowPass(cutoffFrequency=cutoff_frequency)
filtered_audio = low_pass_filter(audio)

# Save the filtered audio
output_file = 'filtered_audio_low_pass.wav'
es.MonoWriter(filename=output_file)(filtered_audio)

print(f"Filtered audio saved to {output_file}")
