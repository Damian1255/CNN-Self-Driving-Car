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
    steering = joystick.get_axis(0)
    throttle = joystick.get_axis(1)
    brake = joystick.get_axis(2)

    # Normalize the axes
    steering = round(steering, 2)
    throttle = round(throttle, 2)
    brake = round(brake, 2)

    # Do something with the input data
    print(f"Steering: {steering}, throttle: {throttle}, brake: {brake}", end="\r")
