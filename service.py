import pyautogui
from gpiozero import Button


MOVE_DISTANCE = 5
SPEED_INCREASE = 1

UP = 14
DOWN = 3
LEFT = 4
RIGHT = 2

x_increase = 0
y_increase = 0

buttons = [Button(x) for x in [UP, DOWN, LEFT, RIGHT]]

while True:
    direction_values = [i.is_pressed for i in buttons]

    print(direction_values)

    if direction_values[0]:
        y_increase += 1
    elif direction_values[1]:
        y_increase -= 1
    else:
        y_increase = 0

    if direction_values[2]:
        x_increase -= 1
    elif direction_values[3]:
        x_increase += 1
    else:
        x_increase = 0

    pyautogui.move(MOVE_DISTANCE * x_increase, MOVE_DISTANCE * y_increase, 0.05)