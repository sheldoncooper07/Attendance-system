FaceRecognition
Real Time face Recognition using LBPH classifier.
To use this you have to copy all 4 .py files and that haarcascade file in same folder with any name suppose "faceRecognition"
Import following modules:
    opencv 4.1.2.30
    Numpy 
    Pillow
    OS
If you use external camera then you have to change cap=cv2.VideoCapture(0) to cap=cv2.VideoCapture(1) in train.py and test.py code
Create another folder named data inside faceRecognition folder.
Open train.py file and select faceRecognition folder and run this file to collect training data and input id of that person(id should be integer).
Now, open classifier.py file with faceRecognition folder selected and run this file it will create a classifier.yml file in that folder.
classifier.yml contains classified faces with their ids.
Now, open test.py to recognize id of faces which are in front of camera.
To check accuracy open accuracy.py file and run. It will print accuracy as well as predicted id.

For error correction
You can get attribure error while running classifier.py file
To resolve this follow the following link
https://github.com/thecodacus/Face-Recognition/issues/3
