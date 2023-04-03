# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 23:06:48 2023

@author: vinit
"""

import cv2
import numpy as np
import pytesseract

# Load the video source (e.g. a camera feed)
cap = cv2.VideoCapture(0)

# Set the width and height of the frames in the video stream
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

# Define the cascade classifier for detecting cars and bikes
car_cascade = cv2.CascadeClassifier('cars.xml')
bike_cascade = cv2.CascadeClassifier('bikes.xml')

# Load the license plate recognition model
# (This may require downloading and installing additional packages)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars and bikes in the frame
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    bikes = bike_cascade.detectMultiScale(gray, 1.1, 1)

    # Loop over the cars and bikes
    for (x, y, w, h) in cars:
        # Draw a rectangle around the car
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Crop the license plate region from the car
        plate = frame[y:y + h, x:x + w]

        # Use OCR to recognize the license plate text
        text = pytesseract.image_to_string(plate, lang='eng')

        # Store the license plate text and car count
        with open('license_plates.txt', 'a') as f:
            f.write(f'Car: {text}\n')

    for (x, y, w, h) in bikes:
        # Draw a rectangle around the bike
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Crop the license plate region from the bike (if any)
        plate = frame[y:y + h, x:x + w]

        # Use OCR to recognize the license plate text (if any)
        text = pytesseract.image_to_string(plate, lang='eng')

        # Store the license plate text and bike count
        with open('license_plates.txt', 'a') as f:
            f.write(f'Bike: {text}\n')

    # Write the processed frame to the output video
    out.write(frame)

    # Display the processed frame
    cv2.imshow('Processed Frame', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video writer and destroy the windows
out.release()
cv2.destroyAllWindows()