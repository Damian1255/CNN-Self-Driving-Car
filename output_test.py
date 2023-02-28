import vgamepad as vg
import time
import pickle
import cv2

gamepad = vg.VX360Gamepad()

def controls(throttle, steering, brake):
    gamepad.left_trigger_float(value_float=brake)
    gamepad.right_trigger_float(value_float=throttle)
    gamepad.left_joystick_float(x_value_float=steering, y_value_float=0.0)
    gamepad.update()

for i in list(range(5))[::-1]:
        print(f'Starting in: {i+1}')
        time.sleep(1)
        
print('Playback Started')

# read data from file
with open('Data/test_data.pickle', 'rb') as f:
    training_data = pickle.load(f)

for data in training_data:
    screen = data[0]
    throttle = data[2]
    steering = data[1]
    brake = data[3]

    # show the screen
    # cv2.imshow('screen', screen)
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    #     break

    controls(throttle=throttle, steering=steering, brake=brake)
    # print(f"Steering: {steering}, throttle: {throttle}, brake: {brake}", end="\r")

    time.sleep(0.01)

print('Playback Ended')