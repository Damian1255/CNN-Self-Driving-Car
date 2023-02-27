import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

def throttle(value):
    gamepad.right_trigger_float(value_float=value)
    gamepad.update()

def steering(value):
    gamepad.left_joystick_float(x_value_float=value, y_value_float=0.0)
    gamepad.update()

def brake(value):
    gamepad.left_trigger_float(value_float=value)
    gamepad.update()

def reset():
    gamepad.reset()

def update():
    gamepad.update()

x = 0.0
y = 0.0
z = 0.0

while True:
    if x > 1.0:
        x = 0.0
        y = 0.0
    if z > 2.0:
        z = -2.0

    gamepad.left_trigger_float(value_float=x)
    gamepad.right_trigger_float(value_float=y)
    gamepad.left_joystick_float(x_value_float=z, y_value_float=0.0)
    gamepad.update()

    x += 0.01
    y += 0.01
    z += 0.01
    time.sleep(0.05)
    print(f"Steering: {z}, throttle: {y}, brake: {x}", end="\r")