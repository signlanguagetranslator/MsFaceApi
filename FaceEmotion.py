import cognitive_face as CF
import cv2
import os
import numpy as np

# Replace with a valid subscription key (keeping the quotes in place).
KEY = '109ed867d2ec4525b21c6084239c232e'
CF.Key.set(KEY)

# Replace with your regional Base URL
BASE_URL = 'https://faceapi125.cognitiveservices.azure.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

cap = cv2.VideoCapture('video.gif')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
cntEmo = np.zeros(8, dtype=int)

while True:
    ret,frame = cap.read()

    if ret == False:
        break
    cv2.imwrite("frame.jpg", frame)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
    img_url = 'frame.jpg'
    faces = CF.face.detect(img_url, face_id =False, attributes='emotion')
    maxEmo = 0
    maxVal = 0

    for face in faces:
        emotion = face['faceAttributes']['emotion']
        i = 0
        for emo in face['faceAttributes']['emotion']:
            val = emotion[emo]
            if maxVal < val:
                maxEmo = i
                maxVal = val
            i += 1
        cntEmo[maxEmo] += 1
        maxVal = 0
        
facelist = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
maxVal = 0
res = 'anger'
i = 0
for k in cntEmo:
    if maxVal < k:
        maxVal = k
        res = facelist[i]
    i += 1
print(res)
