from typing import Tuple
#from braitenberg_agent.agent import preprocess
import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[100:150, 100:150] = 1
    res[300:, 200:] = 1
    #res[:, :shape[1] // 2] = preprocess[:, :shape[1] // 2] / 255
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[100:150, 100:300] = -1
    #res[:, shape[1] // 2:] = preprocess[:, shape[1] // 2:] / 255
    # ---
    return res
