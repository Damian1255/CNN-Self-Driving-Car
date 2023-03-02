import pygame
import time
import pickle
from grabscreen import grab_screen
import cv2

training_data = []

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

for i in list(range(3))[::-1]:
        print(f'Starting in: {i+1}')
        time.sleep(1)
        
print('\nRecording Started')

while True:
    pygame.event.pump()
    
    # Grab the screen
    screen = grab_screen(region=(0,40,1920,1080))
    screen = cv2.resize(screen, (480,270))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    #grayscale
    # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    
    # Read the joystick axes and buttons
    steering = joystick.get_axis(0)
    throttle = (joystick.get_axis(5) + 1) / 2
    brake = (joystick.get_axis(4) + 1) / 2

    # Append the data to the training_data list
    training_data.append([screen, steering, throttle, brake])

    # print(f"Steering: {steering}, throttle: {throttle}, brake: {brake}, recording: {len(training_data)}", end="\r")
    # print(f"Recording: {len(training_data)}", end="\r")

    if len(training_data) == 2500:
        print('Recording Ended')
        with open('Data/test_data.pickle', 'wb') as f:
            pickle.dump(training_data, f)
        break