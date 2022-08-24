import cv2
import numpy as np
from model import model_b as de
cap = cv2.VideoCapture(0)
cond=True
while cond:
    success, img = cap.read()
    de.detection(img)
    cv2.imshow('Image', img)
    k=cv2.waitKey(33)
    if k==27:
        cond=False