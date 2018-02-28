import cv2
import os

video_stream = cv2.VideoCapture(0)
face_cascade = "model.xml"
cascade = cv2.CascadeClassifier(face_cascade)
output_path = "ian/"

frame_num = 0
total_frames = 2500
while(frame_num < total_frames):
    frame_num = frame_num + 1
    if(frame_num % 100 == 0):
            print("Completed %d/%d frames" % (frame_num, total_frames))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    ret, frame = video_stream.read()

    cv2.imshow('frame', frame)

    for i, face in enumerate(cascade.detectMultiScale(frame)):
        if(i > 0):
            continue
        x, y, w, h = face
        sub_face = frame[y:y + h, x:x + w]
        cv2.imwrite(os.path.join(output_path, "{}_{}.jpg".format(frame_num, i)), sub_face)
