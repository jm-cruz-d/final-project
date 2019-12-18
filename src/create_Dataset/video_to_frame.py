#!/bin/bash
import sys
import cv2 
import re
import glob

def video(path):
    for pc in glob.glob(path):
        vidObj = cv2.VideoCapture(pc)
        mpg = pc.split('/')[-1]
        name = re.sub('\.\w+', '', mpg)  
        if vidObj.get(cv2.CAP_PROP_POS_MSEC) < 1500:
            frameRate = 0.5 #//it will capture image in each 0.5 second
            success(frameRate, vidObj, name)      
        else:
            frameRate = 1.0 #//it will capture image in each 1.0 second
            success(frameRate, vidObj, name)     
    return None

def getFrame(sec, vidObj, name):   
    vidObj.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames, image = vidObj.read()   
    if hasFrames:
        cv2.imwrite(f"{name}{int(round(sec*2, 0))}.jpg", image)     # save frame as JPG file           
    return hasFrames

def success(frameRate, vidObj, name):
    sec = 0
    count=1
    success = getFrame(sec, vidObj, name)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec,vidObj, name)

# Get frames from video and insert in the folder of this file.
video(sys.argv[1])

# Calling in Terminal: python3 video_to_frame.py videoPath