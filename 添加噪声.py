import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体支持
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

# 载入语音信号
file_path = 'record/my_recording.wav'  # 替换为你的音频文件路径
signal, sr = librosa.load(file_path, sr=None)


# 生成白噪声（宽带噪声）
def add_broadband_noise(in_signal, noise_level=0.01):
    noise = np.random.normal(0, noise_level, in_signal.shape)  # 高斯分布的白噪声
    Noisy_signal = in_signal + noise
    return Noisy_signal


# 给语音信号添加宽带噪声
noisy_signal = add_broadband_noise(signal)

# 保存添加噪声后的音频信号
sf.write('record/noisy_audio.wav', noisy_signal, sr)

# 可视化原始信号和噪声信号
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
# plt.plot(signal[:1000])  # 仅绘制前1000个样本点
plt.plot(signal)  # 仅绘制前1000个样本点
plt.title("原始信号")
plt.subplot(2, 1, 2)
# plt.plot(noisy_signal[:1000])  # 仅绘制前1000个样本点
plt.plot(noisy_signal)  # 仅绘制前1000个样本点
plt.title("噪声信号")
plt.tight_layout()
plt.savefig('image/origin_noisy.png', dpi=300)

plt.show()
