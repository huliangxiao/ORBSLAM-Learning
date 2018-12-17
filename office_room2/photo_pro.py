import os 
import cv2 
import numpy as np 

def getName(num):
	strTmp = []
	strRes = ''

	while(num / 10):
		strTmp.append(num % 10)
		num = num / 10
	strTmp.append(num)
	n = len(strTmp)
	for i in range(0,5-n):
		strRes = strRes + '0'
	for i in range(n-1,-1,-1):
		strRes =strRes + str(strTmp[i])
	return strRes

videoCapture = cv2.VideoCapture('office_room2.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
print(fps)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
	int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)
if not os.path.exists('rgb/'):
    os.makedirs('rgb')
success, frame = videoCapture.read()
idx = 1
while success:
	frame_resize = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_CUBIC)
	cv2.imshow("show", frame_resize) 
	cv2.waitKey(1000/int(fps))
	cv2.imwrite('rgb/'+getName(idx)+'.png',frame_resize)
	success, frame = videoCapture.read()
	idx = idx + 1

