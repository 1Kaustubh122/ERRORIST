# # recording via microphone

import pyaudio
import wave

Frame_Per_Buffer = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format= FORMAT,
    channels= CHANNELS,
    rate=RATE,
    input= True,
    frames_per_buffer=Frame_Per_Buffer
)

print("Start Recording")

seconds = 5
frames = []
for i in range(0, int(RATE/Frame_Per_Buffer*seconds)):
    print(f"Reading frame {i}")
    data = stream.read(Frame_Per_Buffer)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()


obj = wave.open("output2.wav", "wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()