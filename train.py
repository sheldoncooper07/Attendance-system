import cv2

id= int(input('Enter your id:'))
cap = cv2.VideoCapture(0)
i=0
while(True):
    check,frame = cap.read()
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=5,minSize=(1,1),flags=cv2.CASCADE_SCALE_IMAGE)
    vertices=[]
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),2)
        cv2.putText(frame, str(id), (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 1, cv2.LINE_AA)
        vertices=[x,y,x+w,y+h]
        
    cv2.imshow('frame',frame)
    
    if len(vertices)==4:
        roi_img = frame[vertices[1]:vertices[3], vertices[0]:vertices[2]]
        cv2.imwrite("data/"+str(id)+'.'+str(i)+'.jpg',roi_img)
        i+=1
        if i//50==1:
            break
        
    if cv2.waitKey(1) & 0xFF==ord('1'):
        break

cap.release()  
cv2.destroyAllWindows()