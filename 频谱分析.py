import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 载入音频信号
file_path = 'record/filtered_audio_2.wav'
noisy_signal, sr = librosa.load(file_path, sr=None)

# 设置中文字体支持
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 6))
D = np.abs(librosa.stft(noisy_signal))
librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), sr=sr, x_axis='time', y_axis='log')
plt.title('Noisy Signal Spectrum')
plt.colorbar(format='%+2.0f dB')
plt.show()
