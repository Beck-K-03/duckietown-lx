from typing import Tuple
#from braitenberg_agent.agent import preprocess
import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    if (res[300:, 0:200]):
        res=1
    elif (res[300:, 400:600]):
        res=0
    else:
        res=1

    #res[:, :shape[1] // 2] = preprocess[:, :shape[1] // 2] / 255
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    if (res[300:, 400:600]):
        res=1
    elif (res[300:, 0:200]):
        res=0
    else:
        res=1
    #res[:, shape[1] // 2:] = preprocess[:, shape[1] // 2:] / 255
    # ---
    return res
