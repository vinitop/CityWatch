# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:45:54 2023

@author: vinit
"""

import cv2
import numpy as np

# Start the camera feed
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of color in HSV
    lower_color = np.array([0, 70, 50])
    upper_color = np.array([40, 255, 255])

    # Threshold the HSV image to get only the specified color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Get the dominant color in the mask
    dominant_color = cv2.bitwise_or(frame, frame, mask=mask)

    # Store the dominant color
    cv2.imwrite("dominant_color.jpg", dominant_color)

    # Display the results
    cv2.imshow("Mask", mask)
    cv2.imshow("Dominant Color", dominant_color)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()
cv2.destroyAllWindows()
