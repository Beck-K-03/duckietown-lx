from typing import Tuple

import numpy as np
import cv2


def get_steer_matrix_left_lane_markings(shape: Tuple[int, int]) -> np.ndarray:
    """
    Args:
        shape:              The shape of the steer matrix.

    Return:
        steer_matrix_left:  The steering (angular rate) matrix for Braitenberg-like control
                            using the masked left lane markings (numpy.ndarray)
    """
    height, width = shape
    steer_matrix_left = np.zeros(shape)
    
    for i in range(width):
        # Gradually change value from -1 to 0 across the width
        value = -1 + (i / (width - 1))
        steer_matrix_left[:, i] = value
    # TODO: implement your own solution here
    #steer_matrix_left = np.random.rand(*shape)
    # ---
    return steer_matrix_left


def get_steer_matrix_right_lane_markings(shape: Tuple[int, int]) -> np.ndarray:
    """
    Args:
        shape:               The shape of the steer matrix.

    Return:
        steer_matrix_right:  The steering (angular rate) matrix for Braitenberg-like control
                             using the masked right lane markings (numpy.ndarray)
    """
    height, width = shape
    steer_matrix_right = np.zeros(shape)
    
    for i in range(width):
        # Gradually change value from 0 to -1 across the width
        value = 0 - (i / (width - 1))
        steer_matrix_right[:, i] = value
    # TODO: implement your own solution here
    #steer_matrix_right = np.random.rand(*shape)
    # ---
    return steer_matrix_right


def detect_lane_markings(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Args:
        image: An image from the robot's camera in the BGR color space (numpy.ndarray)
    Return:
        mask_left_edge:   Masked image for the dashed-yellow line (numpy.ndarray)
        mask_right_edge:  Masked image for the solid-white line (numpy.ndarray)
    """
    h, w, _ = image.shape
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Yellow color range for left lane markings
    yellow_lower = np.array([20, 100, 100], dtype="uint8")
    yellow_upper = np.array([30, 255, 255], dtype="uint8")
    mask_left_edge = cv2.inRange(hsv, yellow_lower, yellow_upper)
    
    # White color range for right lane markings
    white_lower = np.array([55, 0, 100], dtype="uint8")
    white_upper = np.array([200, 255, 255], dtype="uint8")
    mask_right_edge = cv2.inRange(hsv, white_lower, white_upper)
    # TODO: implement your own solution here
    #mask_left_edge = np.random.rand(h, w)
    #mask_right_edge = np.random.rand(h, w)

    return mask_left_edge, mask_right_edge
