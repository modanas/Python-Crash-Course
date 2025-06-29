
# Step 1: Click at (1294, 1049)
pyautogui.click(1210, 926)
time.sleep(0.5)

# Step 2: Drag from (658, 177) to (1893, 929)
pyautogui.moveTo(658, 177)
pyautogui.mouseDown()
pyautogui.moveTo(1893, 929, duration=1)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Press Ctrl+C to copy
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Store copied text into a variable
copied_text = pyperclip.paste()

print("Copied Text:\n", copied_text)
