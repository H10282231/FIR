import sounddevice as sd
import scipy.io.wavfile as wav

# 录制参数
duration = 5  # 录制时长 秒
samplerate = 44100  # 采样率 Hz

# 录制音频
print("开始录制...")
audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')  # 单声道录音
sd.wait()  # 等待录制完成
print("录制完成!")

output_filename = 'record/my_recording.wav'
wav.write(output_filename, samplerate, audio_data)
print("音频文件已保存为 {}".format(output_filename))
