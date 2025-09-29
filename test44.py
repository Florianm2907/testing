import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import cv2
import collections
from scipy.signal import find_peaks
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time as t

history_length = 100
red_history = collections.deque(maxlen=history_length)
green_history = collections.deque(maxlen=history_length)
blue_history = collections.deque(maxlen=history_length)
pulse_lines = []
update_time = 50
times = collections.deque(maxlen=history_length)
time_differences = collections.deque(maxlen=history_length)
threshold = 1.1
min_distance = 3
bpm = 0
difference_average = collections.deque(maxlen=history_length)


def time_between_peaks(peaks):
    pulses = []
    for i in range(len(peaks)):
        if len(peaks) > i + 1:
            pulses.append(peaks[i+1] - peaks[i])
    return pulses

def get_average_rgb(camera):
    ret, frame = camera.read()
    if not ret:
        raise Exception("Failed to capture a frame from the camera.")
    average_color = np.mean(frame, axis=(0, 1))
    return average_color

def update_plot(frame, red_line, green_line, blue_line, camera, ax2):
    average_rgb = get_average_rgb(camera)
    red_history.append(average_rgb[0])
    green_history.append(average_rgb[1])
    blue_history.append(average_rgb[2])
    times.append(t.time())
    formatted_values = ["{:.2f}".format(value % 100) for value in times]
    red_line.set_ydata(np.pad(red_history, (history_length - len(red_history), 0)))
    green_line.set_ydata(np.pad(green_history, (history_length - len(green_history), 0)))
    blue_line.set_ydata(np.pad(blue_history, (history_length - len(blue_history), 0)))
    ymax = np.max([red_history,green_history,blue_history])
    ymin = np.min([red_history,green_history,blue_history])
    if ymin >= 2: ymin-=2
    ymax +=2
    ax2.set_ylim(ymin, ymax)
    brightness = (average_rgb[0] + average_rgb[1] + average_rgb[2])/3
    if brightness < 70:
        peaks = detect_pulse(blue_history, formatted_values)
        draw_pulse_lines(peaks, ax2, len(red_history))

def detect_pulse(red_history, history_with_time):
    peaks, _ = find_peaks(red_history, height=threshold, distance=min_distance)
    difference_average = []
    difference_average_average_time = []
    for x in peaks[-6:]:
        difference_average.append(float(history_with_time[x]))
    for i in range(1, len(difference_average)): difference_average_average_time.append(float(difference_average[i]) - float(difference_average[i - 1]))
    print("values to calculate with: ", str(difference_average_average_time))
    difference_average_average_time = np.average(difference_average_average_time)
    print("estimated pulse:", str(60 / float(difference_average_average_time)))
    return peaks

def draw_pulse_lines(peaks, ax, num_frames):
    global pulse_lines
    min_frame_index = num_frames - history_length
    pulse_lines = [line for line in pulse_lines if line.get_xdata()[0] >= min_frame_index]
    for line in pulse_lines:
        line.remove()
    pulse_lines = []
    x_coords = [peak for peak in peaks if peak >= min_frame_index]
    for x_coord in x_coords:
        line = ax.axvline(x=x_coord, color='gray', linestyle='--', linewidth=1, alpha=0.5)
        pulse_lines.append(line)
    excess_lines = len(pulse_lines) - history_length
    if excess_lines > 0:
        pulse_lines[:excess_lines] = []

def main():
    camera = cv2.VideoCapture(0)
    try:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        num_channels = history_length
        x = np.arange(num_channels)
        red_history = np.zeros(history_length)
        green_history = np.zeros(history_length)
        blue_history = np.zeros(history_length)
        red_line, = ax2.plot(x, red_history, 'r-', label='Red')
        green_line, = ax2.plot(x, green_history, 'g-', label='Green')
        blue_line, = ax2.plot(x, blue_history, 'b-', label='Blue')
        ax2.set_title("Average RGB Values Over Time")
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Average Value")
        ax2.legend()
        camera_frame = ax1.imshow(np.zeros((480, 640, 3), dtype=np.uint8))
        def update_frame(i):
            ret, frame = camera.read()
            if ret:
                camera_frame.set_data(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        anim = FuncAnimation(fig, update_frame, interval=update_time)
        anim2 = FuncAnimation(fig, update_plot, fargs=(blue_line, green_line, red_line, camera, ax2), interval=update_time, save_count=history_length)
        plt.show()
    except Exception as e:
        print("Error:", e)
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()