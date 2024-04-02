"""
using this file to conduct age recognition and gender recognition
"""
import cv2
import numpy as np

def findGender(img, original):
    #load the pre-trained models for gender recognition
    gender_net = cv2.dnn.readNetFromCaffe("D:\\HKU_Resources\\Python_Tutorials\\FaceRecognition\\gender_deploy.prototxt", "D:\\HKU_Resources\\Python_Tutorials\\FaceRecognition\\gender_net.caffemodel")
    
    #preprocess the face image for gender recognition
    blob = cv2.dnn.blobFromImage(img, 1.0, (227,227), (78.426, 87.767, 114.897), swapRB = False)

    #perform gender recognition
    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    gender_idx = np.argmax(gender_preds)
    if gender_idx == 1:
        gender = "Male"
    else:
        gender = "Female"
    

    #show
    text = "Gender: " + str(gender)
    cv2.putText(original, text, (10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 1)
    return gender
