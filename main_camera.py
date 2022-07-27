import cv2
import numpy as np
import main_all as m

def inversion(img):
    return cv2.bitwise_not(img)

def rotation(image, angle=30):
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    angle = 30
    scale = 1
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def pivoter(image,code=1):
    return cv2.flip(image, code)


path_image="realTime\\cam.png"
path_weight="poids\\best_char.pt"

cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()
    cv2.imwrite(path_image,frame)
    xyxy_lab=m.realTime(
        adresse_poids=path_weight,
        adresse_image=path_image,
        seuil=0.3
        )
    xp=0
    yp=0
    if len(xyxy_lab)>=1:
        xp=int((xyxy_lab[0][0]+xyxy_lab[0][2])/2)
        yp=int((xyxy_lab[0][1]+xyxy_lab[0][3])/2)
    if xp!=0 and yp!=0:
        (h,w,_)=frame.shape

        image=frame[xyxy_lab[0][1]:xyxy_lab[0][3],xyxy_lab[0][0]:xyxy_lab[0][2]]
        image=cv2.resize(image,(int(w/2),int(w/2)))

        img = np.zeros((h+1,int(w*3/2),3), np.uint8)
        # img[0:h,0:w]=inversion(image)[:,:]
        img[0:h,0:w]=frame[:,:]
        img[22:int(w/2)+22,w:int(w*3/2)]=image[:,:]


        cv2.line(img,(int(w/2)-5,int(h/2)),(int(w/2)+5,int(h/2)),(25,25,25),1)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img,'DETECTIONS',(w+2,20), font, 1,(255,255,255),1,cv2.LINE_AA)
        cv2.line(img,(w,22),(int(w*3/2),22),(255,255,255),1)
        cv2.line(img,(w,22+int(w/2)),(int(w*3/2),22+int(w/2)),(255,255,255),1)
        cv2.putText(img,'INFORMATIONS',(w,44+int(w/2)), font, 1,(255,255,255),1,cv2.LINE_AA)#LINE_AA)
        cv2.circle(img,(xp,yp), 10, (0,0,255), -1)
        cv2.putText(img,xyxy_lab[0][4],(yp,xp-10), font, 1,(255,0,0),1,cv2.LINE_AA)


        cv2.imshow('video',img )
    else :
        cv2.imshow('video', frame)



    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()