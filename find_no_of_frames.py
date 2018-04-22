import os
import cv2

rootdir = "C:\Users\sonupc\Dropbox\Sem 4-2\Neural Networks\Project\NNFL_Training_Set"
a = "hello.txt"
print (a.endswith("txt"))
mini  = 10000000;

for subdir, dirs1, files in os.walk(rootdir):
	for dir1 in dirs1:
		for subdir, dirs2, files in os.walk(rootdir + "/" + dir1):
			for dir2 in dirs2:
				for subdir, dirs2, files in os.walk(rootdir + "/" + dir1 + "/" + dir2):
					for file in files:
						if file.endswith("avi"):
							#print(file)
							cap = cv2.VideoCapture(rootdir + "/" + dir1 + "/" + dir2 + "/" + file)
							success, image = cap.read()
							length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
							print(file,length)
							if length < mini:
								mini = length;

print mini