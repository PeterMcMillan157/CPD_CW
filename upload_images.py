# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:01:09 2022

@author: Peter
"""


import boto3
import time
ACCESS_KEY = "XXXXXXXXXXXXXXXXXXXX"
SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXXXXX"


#Tell program which bucket to upload to
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
#BUCKET = "cpds1937053"
BUCKET = "s1937053mybucket"

#upload 1st image
s3.upload_file("image1.jpg",BUCKET, "image1.jpg")
print("image uploaded")

#wait 30 seconds
time.sleep(30)

#upload 2nd image
s3.upload_file("image2.png",BUCKET, "image2.png")
print("image uploaded")


#wait 30 seconds
time.sleep(30)

#upload 3rd image
s3.upload_file("image3.jpg",BUCKET, "image3.jpg")
print("image uploaded")

#wait 30 seconds
time.sleep(30)

#upload 4th image
s3.upload_file("image4.jpg", BUCKET,"image4.jpg")
print("image uploaded")

#wait 30 seconds
time.sleep(30)

#upload 5th image
s3.upload_file("image5.jpg",BUCKET, "image5.jpg")
print("image uploaded")

print("All images uploaded")