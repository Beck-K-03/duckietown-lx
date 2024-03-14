from typing import Tuple
#from braitenberg_agent.agent import preprocess
import numpy as np
import math
Decay=0.99056
YRange=355
Radius=300

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    for k in range (Radius):
        for i in range(640):
            num=(k**2)-((i-320)**2)
            if (num>=0):
                highpixel=-math.sqrt(num)+480
                highpixel=int(highpixel)
                if (i<320):
                    res[highpixel:480,i] += (1/Radius)*((1.001)**k)
                else:
                    res[highpixel:480,i] += (-1/Radius)*((1.001)**k)
    for i in range(YRange):
        res[(479-i),320:640] += -1*(Decay**i)
        res[(479-i),0:320] += 1*(Decay**i)

    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    for k in range (Radius):
        for i in range(640):
            num=(k**2)-((i-320)**2)
            if (num>=0):
                highpixel=-math.sqrt(num)+480
                highpixel=int(highpixel)
                if (i<320):
                    res[highpixel:480,i] += (-1/Radius)*((1.001)**k)
                else:
                    res[highpixel:480,i] += (1/Radius)*((1.001)**k)
    for i in range(YRange):
        res[(479-i),320:640] += 1*(Decay**i)
        res[(479-i),0:320] += -1*(Decay**i)
    return res
