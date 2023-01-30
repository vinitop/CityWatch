# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:46:37 2023

@author: vinit
"""
import face_recognition
import cv2
import os
import tkinter as tk
from tkinter import filedialog

def select_image():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path

def face_match(known_image_path, images_dir):
    known_image = face_recognition.load_image_file(known_image_path)
    known_encoding = face_recognition.face_encodings(known_image)[0]

    match_list = []
    for filename in os.listdir(images_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(images_dir, filename)
            current_image = face_recognition.load_image_file(image_path)
            current_encoding = face_recognition.face_encodings(current_image)

            if len(current_encoding) > 0:
                result = face_recognition.compare_faces([known_encoding], current_encoding[0])

                if result[0]:
                    match_list.append(filename)
    
    return match_list

def show_match(match_list):
    if len(match_list) > 0:
        match_window = tk.Toplevel()
        match_window.title("Match Found")
        
        label = tk.Label(match_window, text="Matched Files:")
        label.pack()

        for filename in match_list:
            file_label = tk.Label(match_window, text=filename)
            file_label.pack()
    else:
        tk.messagebox.showinfo("No Match", "No match found.")

if __name__ == "__main__":
    known_image_path = select_image()
    images_dir = filedialog.askdirectory()

    match_list = face_match(known_image_path, images_dir)
    show_match(match_list)
