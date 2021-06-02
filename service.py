import time
import Adafruit_ADS1x15
import pyautogui

MOVE_DISTANCE = 5

UP = 0
DOWN = 2
LEFT = 3
RIGHT = 1

THRESHOLD = 800

adc = Adafruit_ADS1x15.ADS1015()

while True:
    direction_values = [adc.read_adc(i, gain=1, data_rate=128) for i in [UP, DOWN, LEFT, RIGHT]]

    print(direction_values)

    x_direction = 0
    y_direction = 0

    if direction_values[0] > THRESHOLD:
        y_direction = 1
    elif direction_values[1] > THRESHOLD:
        y_direction = -1

    if direction_values[2] > THRESHOLD:
        x_direction = -1
    elif direction_values[3] > THRESHOLD:
        x_direction = 1


    pyautogui.drag(MOVE_DISTANCE * x_direction, MOVE_DISTANCE * y_direction, 0.05)

    time.sleep(0.05)