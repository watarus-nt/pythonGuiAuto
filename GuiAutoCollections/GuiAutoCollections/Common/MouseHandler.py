import time
import pyautogui


class MouseHandler(object):
    def __init__(self):
        pass

    def draw_a_square(self, location_x, location_y):
        time.sleep(1)
        pyautogui.click(location_x, location_y)  # click to put drawing program in focus
        distance = 100
        pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
        pyautogui.dragRel(0, distance, duration=0.5)  # move down
        pyautogui.dragRel(distance, 0, duration=0.5)  # move right
        pyautogui.dragRel(0, -distance, duration=0.5)  # move up