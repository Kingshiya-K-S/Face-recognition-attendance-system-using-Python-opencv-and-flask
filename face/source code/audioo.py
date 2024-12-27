import cv2
from simple_facerec import SimpleFacerec
import os
from pygame import mixer


mixer.init()
mixer.music.load("forest-lullaby-110624.wav")
mixer.music.set_volume(0.7)

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
cap = cv2.VideoCapture(0)


def play_audio():
    mixer.music.play()

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        if name == "Kingshiya K S":
            play_audio()
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        # frame = cv2.resize(frame, (1080, 1920))
        cv2.imwrite("image.jpg", frame)
        break

cap.release()
cv2.destroyAllWindows()