import pyautogui
pyautogui.FAILSAFE = True

# (100, 100)に移動
pyautogui.moveTo(100, 100)

# ゆっくり(150, 150)分移動
pyautogui.moveRel(150, 150, duration=5)
