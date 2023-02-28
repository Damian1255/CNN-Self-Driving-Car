import numpy as np
from grabscreen import grab_screen
import cv2


while True:
    screen = grab_screen(region=(0,40,1920,1080))
    # resize to something a bit more acceptable for a CNN
    screen = cv2.resize(screen, (480,270))
    # run a color convert:
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

    cv2.imshow('window',cv2.resize(screen,(640,360)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

