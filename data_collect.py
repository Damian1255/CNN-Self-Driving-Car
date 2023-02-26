import pygame

# Initialize the pygame library
pygame.init()

# Initialize the joystick module
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

    # Do something with the input data
    print(f"x-axis: {x_axis}, y-axis: {y_axis}, z-axis: {z_axis}, button 1: {button_1}, button 2: {button_2}")
