import os
import cv2

rootdir = "/home/shrehal/NN Project"

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
							try:
								os.mkdir(rootdir + "/" + dir1 + "/" + dir2 + "/" + "extract")	#directory shoul exist for imwrite to actually write
							except:
								print("extract directory already exists")
							success, image = cap.read()
							count = 0; 
							while success:
								success,image = cap.read()
								dir3 = os.path.join(rootdir,dir1,dir2,"extract")
								print(os.path.join(dir3, "frame%d.jpg" % count))
								dir4 = os.path.join(dir3, "frame%d.jpg" % count)
								cv2.imwrite(dir4, image)     # save frame as JPEG file
								if cv2.waitKey(10) == 27:                     # exit if Escape is hit
										break
								count += 1

print (mini)