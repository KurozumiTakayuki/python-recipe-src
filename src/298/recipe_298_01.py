import pyautogui

# マウスポインタの位置
mouse_pos = pyautogui.position()
print(mouse_pos.x, mouse_pos.y)

# 画面サイズ
disp_size = pyautogui.size()
print(disp_size.height, disp_size.width)
