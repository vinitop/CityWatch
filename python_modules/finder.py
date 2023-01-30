# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:46:37 2023

@author: vinit
"""
import face_recognition
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def select_image():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path

def find_matches(known_image):
    directory = filedialog.askdirectory()
    known_encoding = face_recognition.face_encodings(known_image)[0]
    match = []

    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image = face_recognition.load_image_file(os.path.join(directory, filename))
            face_encodings = face_recognition.face_encodings(image)

            if len(face_encodings) > 0:
                encoding = face_encodings[0]
                results = face_recognition.compare_faces([known_encoding], encoding)
                if results[0]:
                    match.append(filename)

    if len(match) > 0:
        message = "\n".join(match)
        messagebox.showinfo("Match Found", message)
    else:
        messagebox.showinfo("Match Not Found", "No matches found in the selected directory")

known_image = face_recognition.load_image_file(select_image())
find_matches(known_image)
