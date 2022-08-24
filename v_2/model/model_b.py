import cv2
import numpy as np
from model import model_a as md


def initialiser():
    whT           = 32*11
    confThreshold = 0.2
    nmsThreshold  = 0.1

    classesFile        = 'model\\classes.names'
    modelConfiguration = 'model\\yolo-tiny-obj.cfg'
    modelWeights       = 'model\\yolo-tiny-obj.weights'

    classNames = []
    with open(classesFile,'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    return net,whT,confThreshold,nmsThreshold,classNames

net,whT,confThreshold,nmsThreshold,classNames = initialiser()

def findObjects(outputs,img):
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []
    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w,h = int(det[2]* wT), int(det[3]*hT)
                x,y = int((det[0]*wT)-w/2), int((det[1]*hT)-h/2)
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence))
    
    #print(len(bbox))
    if 2 in classIds:
        indices = cv2.dnn.NMSBoxes(bbox, confs,confThreshold,nmsThreshold)

        for i in indices:
            box = bbox[i]
            x,y,w,h = box[0], box[1], box[2], box[3]
            cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),1)
            gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            pred=md.identifier(gray)
            # cv2.putText(img,f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,0,0),2)
            cv2.putText(img,f'{pred} {int(confs[i]*100)}%',(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,0,0),2)
            # print(classIds[i],x,y,w,h)

def detection(image):
    blob = cv2.dnn.blobFromImage(image, 1/255,(whT,whT),[0,0,0],crop=False)
    net.setInput(blob)
    layerNames = net.getLayerNames()
    outputNames=[]
    for i in net.getUnconnectedOutLayers():
        outputNames.append(layerNames[i-1])
    outputs = net.forward(outputNames)
    findObjects(outputs,image)



