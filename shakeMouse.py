import random
import time
import pyautogui

pyautogui.PAUSE = 0.3
w, h = pyautogui.size()

while True:
    # 获取当前鼠标位置，只小范围偏移，不乱跑
    x, y = pyautogui.position()
    offset_x = random.randint(-8, 8)
    offset_y = random.randint(-8, 8)

    # 小幅度移动，最自然
    pyautogui.moveRel(offset_x, offset_y, duration=0.2)

    # 每一轮模拟按一下Shift（系统最强唤醒）
    pyautogui.keyDown("shift")
    pyautogui.keyUp("shift")

    print("防休眠运行中...")
    time.sleep(25)