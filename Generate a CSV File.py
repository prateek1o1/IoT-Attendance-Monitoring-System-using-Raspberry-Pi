# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import urllib  
import argparse
import datetime
import imutils
import time
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="feed_data",
	help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())


print("[INFO] starting video stream...")
vs=VideoStream("http://192.168.1.103:8080/video").start()
time.sleep(2.0)
 

csv = open(args["output"], "w")
found = set()
csv.write("{},{}\n".format('Date','Student Identity'))
while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	barcodes = pyzbar.decode(frame)

	for barcode in barcodes:

		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
		# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first

		barcodeData  = barcode.data.decode("utf-8")
		barcodeType = barcode.type
 
		# draw the barcode data and barcode type on the image
		text = "{} ({})".format(barcodeData, barcodeType)
		j = text [ 7 : 10 ]
		cv2.putText(frame, text, (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
							   
		# if the barcode text is currently not in our CSV file, write
		# the timestamp + barcode to disk and update the set
		
		if j not in found:
			csv.write("{},{}\n".format(datetime.datetime.now().strftime("%a %b %d %Y"),
				j))
			csv.flush()
			found.add(j)

			# show the output frame
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()


import pandas as pd
import csv
DATABASE={'194':'Prashant Kumar','013':'Tanuj Singhal','321':'Tarun Kumar','017':'Zakir Ali','014':'Padam Prakash','082':'Ashi Gupta','304':'Ankit Pandey','345':'Yashashree Patil','311':'Joel','133':'saloni miharia','063':'Abhishek Soni','045':'Dharamveer Dharmacharya','232':'Chirag Bharadwaj','197':'Rakshit Shandilya','179':'Shubham Bhatnagar','175':'Palash Jain','217':'Prateek Chhimwal'}
file1="C:\\Users\\i'm 10\\Desktop\\Data_Feed.csv"
student_df=pd.read_csv(file1,delimiter=',',names=['A','B'])
print(student_df,"\n")
s=pd.read_csv(file1,header=None, index_col=False)[1]
j=s.value_counts()
x=j.to_dict()
w=csv.writer(open("C:\\Users\\i'm 10\\Desktop\\Attendence_Report.csv","w"))
w.writerow(['Student Identity','Name','Attendance'])
for key,value in x.items():
        if(key=='Student Identity'):
            pass
        else:
            w.writerow([key,DATABASE[key],(value/30)*100])
			
with open("C:\\Users\\i'm 10\\Desktop\\Attendence_Report.csv","w") as csvfile:
	csvfile.close()
