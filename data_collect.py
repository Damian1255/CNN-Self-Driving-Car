import pygame

# Initialize the pygame & joystick modules
pygame.init()
pygame.joystick.init()

# Check for available joysticks
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Joystick not found")
    exit()

# Select the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Capture input from the joystick
while True:
    pygame.event.pump()

    # Read the joystick axes and buttons
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)
    z_axis = joystick.get_axis(2)
    button_1 = joystick.get_button(0)
    button_2 = joystick.get_button(1)

    # Normalize the axes
    x_axis = round(x_axis, 2)
    y_axis = round(y_axis, 2)
    z_axis = round(z_axis, 2)

    # Do something with the input data
    print(f"Steering: {x_axis}, throttle: {y_axis}, brake: {z_axis}, button 1: {button_1}, button 2: {button_2}", end="\r")
