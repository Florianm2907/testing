import pyautogui
import keyboard
import time as t

def main():
    try:
        while True:
            # Check if spacebar is pressed to stop the program
            if keyboard.is_pressed('space'):
                print("Program stopped by user.")
                break
            
            # Simulate pressing the ^ key
            keyboard.press_and_release('^')
            # Type "comet"comet
            pyautogui.typewrite('comet')
            # Press Enter
            pyautogui.press('enter')
            
            # You can adjust the sleep time based on your system's responsiveness
            # If it's too fast, you might not be able to stop it in time with spacebar
            pyautogui.sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted.")

if __name__ == "__main__":
    t.sleep(5)
    main()
