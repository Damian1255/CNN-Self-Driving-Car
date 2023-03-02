import vgamepad as vg
import time
import cv2
from grabscreen import grab_screen
from tensorflow import keras

gamepad = vg.VX360Gamepad()

# Load the trained model
model = keras.models.load_model('Models/model.h5')

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

while True:
    # Preprocess the input screen
    screen = grab_screen(region=(0,40,1920,1080))
    screen = cv2.resize(screen, (480,270))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    screen = screen.reshape(-1, 270, 480, 3)

    preds = model.predict(screen)
    preds = str(preds).replace("[", "").replace("]", "")
    preds = [float(i) for i in preds.split()]

    steering_pred, throttle_pred, brake_pred = preds[0], preds[1], preds[2]

    # Update the controls
    controls(throttle=throttle_pred, steering=steering_pred, brake=brake_pred)
    time.sleep(0.01)