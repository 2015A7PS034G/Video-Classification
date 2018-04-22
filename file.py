import os
import cv2
rootdir = "./NNFL_Training_Set"
items =  os.walk(rootdir).next()[1]
for subdir in items:
	path = rootdir + "/" + subdir
	videoDirs = os.walk(rootdir + "/" + subdir).next()[1]
	for video in videoDirs:
		currPath = rootdir + "/" + subdir + "/" + video
		files = os.listdir(currPath)
		for item in files:
			if item.endswith(".avi"):
				vidCap = cv2.VideoCapture(currPath + "/" + item)
				length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	
				
		
