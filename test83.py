import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
CHANNELS = 2
RATE = 44100
CHUNK = 2048
FORMAT = pyaudio.paInt16

# Initialize PyAudio
p = pyaudio.PyAudio()

# Function to find and select the desired microphone
def select_microphone():
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels') > 0:
            print(f"Input Device id {i} - {p.get_device_info_by_host_api_device_index(0, i).get('name')}")
    device_index = int(input("Select device id: "))
    return device_index

# Get device index
device_index = 3

# Start stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=device_index,
                frames_per_buffer=CHUNK)

# Plotting setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
x = np.arange(0, CHUNK)
line1, = ax1.plot(x, np.random.rand(CHUNK), '-', lw=1)
line2, = ax2.plot(x, np.random.rand(CHUNK), '-', lw=1, color='red')
ax1.set_title('Left Channel Waveform')
ax2.set_title('Right Channel Waveform')
ax1.set_ylim(-2**15, 2**15)
ax2.set_ylim(-2**15, 2**15)
ax1.set_xlim(0, CHUNK - 1)
ax2.set_xlim(0, CHUNK - 1)

# Animation update function
def update(frame):
    data = stream.read(CHUNK, exception_on_overflow=False)
    data_np = np.frombuffer(data, dtype=np.int16)
    left_channel = data_np[0::2]
    right_channel = data_np[1::2]
    
    # Update waveform
    line1.set_ydata(left_channel)
    line2.set_ydata(right_channel)
    
    return line1, line2

# Animation
ani = FuncAnimation(fig, update, blit=True, interval=50)

plt.show()

# Cleanup
stream.stop_stream()
stream.close()
p.terminate()
