import pyautogui
import random
import threading
import time as t
# Function to move cursor randomly across the screen
def move_cursor():
    screen_width, screen_height = pyautogui.size()
    while not exit_event.is_set():
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.sleep(0.1)

# Function to stop cursor movement when left mouse button is clicked
def stop_movement():
    pyautogui.mouseDown()
    exit_event.set()

# Start cursor movement on right mouse button click
def on_right_click(x, y):
    move_thread.start()

# Initialize exit event to stop the cursor movement thread
exit_event = threading.Event()

# Register the right mouse button click event
pyautogui.rightClick = on_right_click

# Register the left mouse button click event
pyautogui.leftClick = stop_movement

# Create a thread for cursor movement
move_thread = threading.Thread(target=move_cursor)

try:
    t.sleep(5)
    # Start the cursor movement thread
    move_thread.start()
    
    # Keep the script running
    move_thread.join()
except KeyboardInterrupt:
    # Handle keyboard interrupt gracefully
    exit_event.set()
