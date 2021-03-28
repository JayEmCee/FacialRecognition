import face_recognition
import cv2
import random

video_capture = cv2.VideoCapture(0)

rodolfo_image = face_recognition.load_image_file("rodolfo.jpg")
rodolfo_face_encoding = face_recognition.face_encodings(rodolfo_image)[0]

jerron_image = face_recognition.load_image_file("jerron.jpg")
jerron_face_encoding = face_recognition.face_encodings(jerron_image)[0]

erasmus_image = face_recognition.load_image_file("erasmus.jpg")
erasmus_face_encoding = face_recognition.face_encodings(erasmus_image)[0]

known_face_encodings = [
    rodolfo_face_encoding,
    jerron_face_encoding,
    erasmus_face_encoding
]
known_face_names = [
    "Rodolfo",
    "Jerron"
]

#Array of insults
insults = [
	"you suck",
	"your mother never loved you",
	"random insult no 4",
	"get rekt",
	"git gud",
	"FATAL ERROR"
]

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        print(random.choice(insults) + " " + name)



    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(random.choice(insults))
video_capture.release()
cv2.destroyAllWindows()
