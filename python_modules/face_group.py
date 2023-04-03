import os
import cv2
import numpy as np
from sklearn.cluster import DBSCAN
import face_recognition

def group_faces(dir_path):
    # Load all the images in the directory
    images = []
    image_paths = []
    for filename in os.listdir(dir_path):
        image_path = os.path.join(dir_path, filename)
        if os.path.isfile(image_path):
            image = cv2.imread(image_path)
            images.append(image)
            image_paths.append(image_path)

    # Compute the face encodings for each image
    face_encodings = []
    for image in images:
        face_encoding = face_recognition.face_encodings(image)
        if face_encoding:
            face_encodings.append(face_encoding[0])
        else:
            print("No face found in", image_path)

    # Group similar face encodings together using DBSCAN clustering
    face_encodings = np.array(face_encodings)
    db = DBSCAN(eps=0.3, min_samples=2).fit(face_encodings)
    labels = db.labels_

    # Create a dictionary to store the face encodings and their corresponding image path
    face_dict = {}
    for i, label in enumerate(labels):
        if label not in face_dict:
            face_dict[label] = []
        face_dict[label].append(image_paths[i])

    # Create a directory for each person
    person_index = 0
    for label, image_paths in face_dict.items():
        if label == -1:
            continue
        person_index += 1
        person_dir = f"person_{person_index}"
        os.mkdir(os.path.join(dir_path, person_dir))

        # Move the image to the corresponding person directory
        for image_path in image_paths:
            os.rename(image_path, os.path.join(dir_path, person_dir, os.path.basename(image_path)))

# Example usage
group_faces("faces")
