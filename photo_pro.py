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
	for i in range(0,6-n):
		strRes = strRes + '0'
	for i in range(n-1,-1,-1):
		strRes =strRes + str(strTmp[i])
	return strRes

videoCapture = cv2.VideoCapture('00.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
print(fps)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
	int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)

file_object = open('times.txt','w')
Ostr = ''

if not os.path.exists('image_0/'):
    os.makedirs('image_0')
success, frame = videoCapture.read()
idx = 0
i = 2
while success:
	if(i % 2 ==0):
		i=1
		frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		frame_resize = cv2.resize(frame_gray, (1241, 376), interpolation=cv2.INTER_CUBIC)
		cv2.imshow("show", frame_resize) 
		Ostr = str(videoCapture.get(cv2.CAP_PROP_POS_MSEC)/1000) + '\n'
		file_object.writelines(Ostr)
		cv2.waitKey(1000/int(fps))
		cv2.imwrite('image_0/'+getName(idx)+'.png',frame_resize)
		idx = idx + 1
	else :
		i+=1
	success, frame = videoCapture.read()
	#print(i)
file_object.close()