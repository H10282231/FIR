import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体支持
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

# 假设采样频率（Hz）和截止频率（Hz）
sr = 4410  # 采样频率
fc = 50   # 截止频率
filter_order = 301  # 滤波器阶数（脉冲响应长度）

# 载入音频信号
file_path = 'record/noisy_audio.wav'  # 替换为你的音频文件路径
noisy_signal, sr1 = librosa.load(file_path, sr=None)


# 频率采样法设计低通FIR滤波器
def fir_filter_frequency_sampling(signal, Sr, cutoff_freq, Filter_order):
    # frequencies = np.linspace(0, Sr / 2, Filter_order // 2 + 1)
    frequency_response = np.zeros(Filter_order)
    frequency_response[:Filter_order // 2 + 1] = 1  # 低通滤波器通带为1
    frequency_response[Filter_order // 2 + 1:] = 0  # 高频部分为0
    cutoff_index = int(np.round(cutoff_freq / (Sr / 2) * (filter_order // 2)))
    frequency_response[cutoff_index:] = 0  # 截止频率以上的部分为0
    fir_filter = np.fft.ifft(frequency_response)
    fir_filter = np.real(fir_filter)
    filtered_signal = np.convolve(signal, fir_filter, mode='same')
    return filtered_signal, fir_filter


# 对噪声信号进行频率采样法FIR滤波
filtered_signal_freq_sampling, fir_filter_freq_sampling = fir_filter_frequency_sampling(noisy_signal, sr,
                                                                                        fc, filter_order)

sf.write('record/filtered_audio_2.wav', filtered_signal_freq_sampling, sr1)

# 可视化频率采样法滤波器系数和滤波后的信号
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(fir_filter_freq_sampling)
plt.title("FIR滤波器系数（频率采样法）")

plt.subplot(2, 1, 2)
# plt.plot(filtered_signal_freq_sampling[:1000])
plt.plot(filtered_signal_freq_sampling)
plt.title("滤波后信号（频率采样法）")

plt.tight_layout()
plt.savefig('image/Filtered_Frequency.png', dpi=300)

plt.show()

def fir_filter_frequency_sampling(signal, Sr, cutoff_freq, Filter_order):
    frequency_response = np.zeros(Filter_order)
    frequency_response[:Filter_order // 2 + 1] = 1
    frequency_response[Filter_order // 2 + 1:] = 0
    cutoff_index = int(np.round(cutoff_freq / (Sr / 2) * (filter_order // 2)))
    frequency_response[cutoff_index:] = 0
    fir_filter = np.fft.ifft(frequency_response)
    fir_filter = np.real(fir_filter)
    filtered_signal = np.convolve(signal, fir_filter, mode='same')
    return filtered_signal, fir_filter
