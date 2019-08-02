import cognitive_face as CF
import cv2
import os

# Replace with a valid subscription key (keeping the quotes in place).
KEY = 'MyKey'
CF.Key.set(KEY)

# Replace with your regional Base URL
BASE_URL = 'https://faceapi125.cognitiveservices.azure.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

cap = cv2.VideoCapture('video.gif')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while True:
    ret,frame = cap.read()

    if ret == False:
        break
    cv2.imwrite("frame.jpg", frame)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
    img_url = 'frame.jpg'
    faces = CF.face.detect(img_url, face_id =False, attributes='emotion')
    maxEmo = 'anger'
    maxVal = 0

    for face in faces:
        emotion = face['faceAttributes']['emotion']
        for emo in face['faceAttributes']['emotion']:
            val = emotion[emo]
            if maxVal < val:
                maxEmo = emo
        print(maxEmo)
    os.remove('frame.jpg')
