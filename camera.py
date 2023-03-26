import os
import datetime
import time
import cv2

def camera():
    
    # Open the default camera
    cap = cv2.VideoCapture(0)
        
    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Unable to open the camera")

    else:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if not ret:
            print("Unable to capture the frame")

        else:
            #make a capture image name randomly
            info=datetime.datetime.today()
            d=str(info.day)
            mn=str(info.minute)
            s=str(info.second)
            m=str(info.microsecond)
            pic=d+mn+s+m
            
            # Save the captured image to disk
            cv2.imwrite(f"img{pic}.jpg", frame)
            #os.system(f"img{pic}.jpg")

        # Release the camera and close all windows
        cap.release()
        cv2.destroyAllWindows()
        os.system(f"img{pic}.jpg")
camera()
