import pyautogui
from gpiozero import Button

pyautogui.FAILSAFE = False

MOVE_DISTANCE = 5
SPEED_INCREASE = 1

UP = 3
DOWN = 14
LEFT = 4
RIGHT = 2

x_increase = 0
y_increase = 0

buttons = [Button(x) for x in [UP, DOWN, LEFT, RIGHT]]

while True:
    direction_values = [i.is_pressed for i in buttons]

    print(direction_values)

    if direction_values[0]:
        y_increase += SPEED_INCREASE
    elif direction_values[1]:
        y_increase -= SPEED_INCREASE
    else:
        y_increase = 0

    if direction_values[2]:
        x_increase -= SPEED_INCREASE
    elif direction_values[3]:
        x_increase += SPEED_INCREASE
    else:
        x_increase = 0

    pyautogui.move(MOVE_DISTANCE * x_increase, MOVE_DISTANCE * y_increase, 0.05)
