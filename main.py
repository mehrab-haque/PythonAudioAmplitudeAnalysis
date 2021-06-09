import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd

file = "ignition-start-3.mp3"
audio,sr = librosa.load(file)

sample_duration = 1 / sr
print(f"One sample lasts for {sample_duration:6f} seconds")
tot_samples = len(audio)
duration = 1 / sr * tot_samples
print(f"The audio lasts for {duration} seconds")

plt.figure(figsize=(12, 8))

librosa.display.waveplot(audio, alpha=0.5)
plt.ylim((-1, 1))
plt.title("file")

plt.show()
