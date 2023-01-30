import cv2
import datetime
import time

def capture_faces(camera_index, file_path_prefix):
    # initialize the camera
    camera = cv2.VideoCapture(camera_index)

    # initialize the face detector
    face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    face_count = 0
    while True:
        # capture the current frame
        ret, frame = camera.read()

        # convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces in the frame
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        # draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # show the frame
        cv2.imshow("Faces", frame)

        # write each face to a separate file if faces are detected
        for (x, y, w, h) in faces:
            face_count += 1
            face = frame[y:y+h, x:x+w]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = f"{file_path_prefix}_{timestamp}_{face_count}.jpg"
            cv2.imwrite(file_path, face)

        # break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # sleep for 1 seconds before capturing the next frame
        time.sleep(1)

    # release the camera and close the window
    camera.release()
    cv2.destroyAllWindows()

# capture faces from multiple cameras
for i in range(1):
    file_path_prefix = f"face_{i}"
    capture_faces(i, file_path_prefix)