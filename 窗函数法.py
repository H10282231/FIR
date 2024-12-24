import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体支持
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

# 载入音频信号
file_path = 'record/noisy_audio.wav'  # 替换为你的音频文件路径
noisy_signal, sr = librosa.load(file_path, sr=None)


# 窗函数法设计低通FIR滤波器
def fir_filter_window(signal, sr, cutoff_freq=300, filter_order=101):
    # 计算理想低通滤波器的脉冲响应
    ideal_response = np.sinc(2 * cutoff_freq / sr * (np.arange(filter_order) - (filter_order - 1) / 2))

    # 应用窗函数（汉明窗）
    window = np.hamming(filter_order)
    fir_filter = ideal_response * window

    # 归一化滤波器系数
    fir_filter /= np.sum(fir_filter)

    # 滤波
    filtered_signal = np.convolve(signal, fir_filter, mode='same')
    return filtered_signal, fir_filter


# 对噪声信号进行窗函数法FIR滤波
filtered_signal_window, fir_filter_window = fir_filter_window(noisy_signal, sr, cutoff_freq=300, filter_order=101)

sf.write('record/filtered_audio_1.wav', filtered_signal_window, sr)


# 可视化窗函数法滤波器系数和滤波后的信号
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(fir_filter_window)
plt.title("FIR滤波器系数（窗函数法）")

plt.subplot(2, 1, 2)
# plt.plot(filtered_signal_window[:1000])
plt.plot(filtered_signal_window)
plt.title("滤波后信号（窗函数法）")

plt.tight_layout()
plt.savefig('image/Filtered_window.png', dpi=300)

plt.show()
