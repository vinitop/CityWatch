# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 23:59:21 2023

@author: vinit
"""

import cv2

# Load the video capture object
cap = cv2.VideoCapture("video.mp4")

# Define the background subtraction object
fgbg = cv2.createBackgroundSubtractorMOG2()

# Loop over the frames of the video
while True:
    # Read the next frame
    ret, frame = cap.read()

    # If there are no more frames, break the loop
    if not ret:
        break

    # Apply background subtraction to the frame
    foreground_mask = fgbg.apply(frame)

    # Convert the foreground mask to a binary image
    _, foreground_mask = cv2.threshold(foreground_mask, 128, 255, cv2.THRESH_BINARY)

    # Find the contours in the foreground mask
    contours, _ = cv2.findContours(foreground_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    for contour in contours:
        # If the contour is small, ignore it
        if cv2.contourArea(contour) < 1000:
            continue

        # Otherwise, draw a bounding box around the contour
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Frame", frame)

    # If the user presses the "q" key, break the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object
cap.release()

# Destroy all the windows
cv2.destroyAllWindows()
