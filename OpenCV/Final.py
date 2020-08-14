#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import requests
from matplotlib import pyplot as plt
import numpy as np
from moviepy.editor import *

# Webcam Capture
# cap = cv2.VideoCapture("http://10.12.139.207:8080") 

url = "http://10.12.139.207:8080/shot.jpg"

#video = cv2.VideoWriter('video_output.avi',-1,1,(width,height))
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width,height))

clips = []
j = 1
# print('Frames: ',int(url.get(cv2.CAP_PROP_FRAME_COUNT)))


# In[3]:


print("Start")
while(True):
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, -1)
    frame = cv2.resize(frame,(640,480))
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    template = cv2.imread('Screenshot.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)

    threshold = 0.7
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('Detection Video',frame)
    #video.write(frame)
    #clips.append(frame)
    clips.append(ImageClip(frame).set_duration(0.1))
    j=j+1
    # print('Frame:',j)

    if(cv2.waitKey(1)==27):
         break

# cap.release()
print("Done")
cv2.destroyAllWindows()


# In[4]:


concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("Results_part1.mp4", fps=30)
print("Done")


# In[ ]:




