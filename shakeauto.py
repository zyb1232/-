import random
import time
import pyautogui

# 获取屏幕宽高
screen_w, screen_h = pyautogui.size()

def random_move_mouse():
    while True:
        # 生成屏幕内随机坐标
        x = random.randint(0, screen_w)
        y = random.randint(0, screen_h)
        # 移动鼠标，速度0.3秒
        pyautogui.moveTo(x, y, duration=0.3)
        print(f"移动到: {x}, {y}")
        # 间隔几秒动一次
        time.sleep(2)

if __name__ == "__main__":
    try:
        random_move_mouse()
    except KeyboardInterrupt:
        print("\n程序停止")