import pyautogui
import time
import random

# Set the amount to scroll. Negative numbers scroll down, positive numbers scroll up.
scroll_amount = 1500
# Set the pause time in seconds between scrolls
pause_time = 1

try:
    while True:
        # Generate a random number between 1 and 10
        rand_num = random.randint(1, 10)
        
        if rand_num % 2 == 0:
            # If the number is even, scroll down
            pyautogui.scroll(-scroll_amount)
        else:
            # If the number is odd, scroll up
            pyautogui.scroll(scroll_amount)
            
        time.sleep(pause_time)
except KeyboardInterrupt:
    print("Program exited.")