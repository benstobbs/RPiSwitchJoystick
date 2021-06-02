import Adafruit_ADS1x15
import pyautogui

MOVE_DISTANCE = 5
SPEED_INCREASE = 1

UP = 0
DOWN = 2
LEFT = 3
RIGHT = 1

THRESHOLD = 800

adc = Adafruit_ADS1x15.ADS1015()

x_increase = 0
y_increase = 0

while True:
    direction_values = [adc.read_adc(i, gain=1, data_rate=128) for i in [UP, DOWN, LEFT, RIGHT]]

    print(direction_values)

    x_direction = 0
    y_direction = 0

    if direction_values[0] > THRESHOLD:
        y_increase += 1
        y_direction = y_increase
    elif direction_values[1] > THRESHOLD:
        y_increase -= 1
        y_direction = -1 * y_increase
    else:
        y_increase = 0

    if direction_values[2] > THRESHOLD:
        x_increase -= 1
        x_direction = -1 * y_increase
    elif direction_values[3] > THRESHOLD:
        x_increase += 1
        x_direction = x_increase
    else:
        x_increase = 0


    pyautogui.move(MOVE_DISTANCE * x_direction, MOVE_DISTANCE * y_direction, 0.05)