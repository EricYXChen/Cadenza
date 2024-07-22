import essentia.standard as es

# Load the audio file
audio_file = 'output.wav'
audio = es.MonoLoader(filename=audio_file)()

# Apply high-pass filter
cutoff_frequency = 10000  # Set your cutoff frequency here
high_pass_filter = es.HighPass(cutoffFrequency=cutoff_frequency)
filtered_audio = high_pass_filter(audio)

# Save the filtered audio
output_file = 'filtered_audio_high_pass.wav'
es.MonoWriter(filename=output_file)(filtered_audio)

print(f"Filtered audio saved to {output_file}")

