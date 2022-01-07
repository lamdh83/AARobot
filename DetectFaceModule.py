# íntall visual studio Desktop development with C++
# íntall cmake
# íntall dlib 19.18
#face-recognition
#MACGIC CAMERA License key: k7eUWBqG4H
# Email Address: freebies@thesoftware.shop

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv





class detectFace():
    def __init__(self, path='ImagesAttendance'):
        self.path = path
        self.images = []
        self.classNames = []
        self.encodeListKnown = []
        myList = os.listdir(path)
        print(myList)
        # Doc danh sach anh trong thu muc
        self.f = open('Attendance.csv', 'w')
        self.writer = csv.writer(self.f)
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        # print(f'tao:{self.classNames}')
        # encode face trong danh sach face da doc tu tren  .
        for img in self.images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            self.encodeListKnown.append(encode)
        # print(self.encodeListKnown)

    def detect(self, img):
        xcenter= 0
        ycenter= 0
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
            # print(matches)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = self.classNames[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                # print(f'{x1},{x2},{y1},{y2}')
                xcenter = int(x1 + (x2 - x1) / 2)
                ycenter = int(y1 + (y2 - y1) / 2)
                # print(f'{xcenter, ycenter}')
                # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # cv2.rectangle(img, (xcenter, ycenter), (xcenter + 10 , ycenter + 10), (0, 255, 0), cv2.FILLED)

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                # Luu vao file
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                self.writer.writerow(f'\n{name},{dtString}')



        # img = cv2.resize(img, (640, 480))
        # cv2.imshow('Webcam', img)
        # cv2.waitKey(1)
        return xcenter, ycenter






def main():
    cap = cv2.VideoCapture("1.mp4")
    det = detectFace()
    while True:
        success, img = cap.read()
        det.detect(img)
        cv2.imshow("hinh", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()