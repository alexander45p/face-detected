import cv2 
print(cv2.__version__)

tace_cascade = cv2.cascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.videoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.recTangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.inshow('img', img)
        k = cv2.waitkey(30)
        if k == 27: # 27 es el asscii para esc
            break
        
cap.release()