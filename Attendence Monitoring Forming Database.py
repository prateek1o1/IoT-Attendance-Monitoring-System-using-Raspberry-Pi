from imutils.video import VideoStream
from pyzbar import pyzbar
import urllib  
import argparse
import datetime
import imutils
import time
import cv2
import pandas as pd
import csv
listed=[]


print("[INFO] starting video stream...")
vs=VideoStream("http://192.168.43.1:8080/video").start()

found = set()

while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	barcodes = pyzbar.decode(frame)

	for barcode in barcodes:

		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
		barcodeData  = barcode.data.decode("utf-8")
		barcodeType = barcode.type
 
		text = "{} ({})".format(barcodeData, barcodeType)
		j = text [ 7 : 10 ]
		cv2.putText(frame, text, (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
							   
		
		if j not in found:
			found.add(j)
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
	  print("[INFO] cleaning up...")
	  cv2.destroyAllWindows()
	  vs.stop()
	  break
   

listed=list(found)
DATABASE={'194':'Prashant Kumar','013':'Tanuj Singhal','321':'Tarun Kumar','017':'Zakir Ali','014':'Padam Prakash','082':'Ashi Gupta','304':'Ankit Pandey','345':'Yashashree Patil','311':'Joel','133':'Saloni miharia','063':'Abhishek Soni','045':'Dharamveer Dharmacharya','232':'Chirag Bharadwaj','197':'Rakshit Shandilya','179':'Shubham Bhatnagar','175':'Palash Jain','217':'Prateek Chhimwal','103':'Navneet'}

ind=['Prashant Kumar','Tanuj Singhal','Tarun Kumar','Zakir Ali','Padam Prakash','Ashi Gupta','Ankit Pandey','Yashashree Patil','Joel','Saloni miharia','Abhishek Soni','Dharamveer Dharmacharya','Chirag Bharadwaj','Rakshit Shandilya','Shubham Bhatnagar','Palash Jain','Prateek Chhimwal','Navneet']

file1="//home//pi//AttendenceReport.csv"
df=pd.read_csv(file1,delimiter=',',index_col=0)
print("Enter Day\n")
d=int(input())
newlisted=[]
#listed->newlisted
for c in range(len(listed)):
	newlisted.append(DATABASE[listed[c]])

for k in newlisted:
	 i=ind.index(k)
	 df.iloc[i,d]=1    
	 m=sum(df.iloc[i,1:31])
	 m=m*100
	 m=float(m/30)
	 df.iloc[i,31]=m
	
   
df.to_csv("//home//pi//AttendenceReport.csv")
