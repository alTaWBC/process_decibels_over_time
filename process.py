#%%%

import numpy as np
import scipy.io.wavfile
import scipy.io
import os
import matplotlib.pyplot as plt


# #%%%
# files_folder = r"C:\Users\WilliamCosta\Desktop\tese_repositories\process_decibels_over_time"

# files = [os.path.join(files_folder, f) for f in os.listdir(files_folder) if '.txt' in f]

# for f in files:
#     with open(f, 'r') as decibels_file:
#         lines = decibels_file.readlines()
#         x, y = [], []
#         for line in lines[1:]:
#             parts = line.split(',')
#             if 'Infinity' in parts[3]:
#                 continue

#             x.append(float(parts[1]))
#             y.append(float(parts[3]))

#         plt.plot(x, y)
#         plt.plot([-1000, 1000], [30, 30])
#         plt.xlim([0, x[-1]+1])


#%%%
audio_location = r"C:\Users\WilliamCosta\Desktop\tese_repositories\process_decibels_over_time\audios\161.WAV"

sampleRate, audioBuffer = scipy.io.wavfile.read(audio_location)

duration = len(audioBuffer)/sampleRate

time = np.arange(0, duration, 1/sampleRate)  # time vector

print(audioBuffer.shape, time.shape)
audio = audioBuffer[:, 0] if len(audioBuffer.shape) == 2 else audioBuffer


decibels = 20 * np.log10(audio/ 0.000001, where=audio != 0) - 60

plt.scatter(time, decibels)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.ylim(0, 300)
plt.title(audio_location)
plt.plot([-1000, 1000], [30, 30])
plt.xlim([0, time[-1]])
plt.show()

# %%
#%%%
files_folder = r"C:\Users\WilliamCosta\Desktop\tese_repositories\process_decibels_over_time"

files = [os.path.join(files_folder, f)
         for f in os.listdir(files_folder) if '.txt' in f]

for f in files:
    with open(f, 'r') as decibels_file:
        lines = decibels_file.readlines()
        x, y = [], []
        for line in lines[1:]:
            parts = line.split(',')
            if 'Infinity' in parts[3]:
                continue

            x.append(float(parts[1]))
            y.append(float(parts[3]))

        plt.plot(x, y)
        plt.plot([-1000, 1000], [30, 30])
        plt.xlim([0, x[-1]+1])
        plt.show()
