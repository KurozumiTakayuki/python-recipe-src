import pyautogui
pyautogui.FAILSAFE = True

# shift + 右カーソル3回
pyautogui.keyDown("shift")
pyautogui.typewrite(["right"] * 3, interval=1)
pyautogui.keyUp("shift")

# ctrl + c
pyautogui.hotkey("ctrl", "c")
