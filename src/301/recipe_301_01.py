import pyautogui
pyautogui.FAILSAFE = True

# abc入力後にエンター
pyautogui.typewrite(["a", "b", "c", "return"], interval=1)
