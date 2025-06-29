import pyautogui
import time
import pyperclip

# Small delay to switch to target window
time.sleep(2)

# Step 1: Click at (1294, 1049)
pyautogui.click(1210, 926) #co-ordinates of chrome
time.sleep(0.5)

# Step 2: Drag from (658, 177) to (1893, 929)
pyautogui.moveTo(665, 196) # starting co-ordinates
pyautogui.mouseDown()
pyautogui.moveTo(1894, 927, duration=1) # ending co-ordinates
time.sleep(1) # Wait for 1 second to ensure the copy command is completed
pyautogui.click(693, 277)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Press Ctrl+C to copy
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Store copied text into a variable
copied_text = pyperclip.paste()

print("Copied Text:\n", copied_text)
