# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:01:09 2022

@author: Peter
"""


import boto3
import time


#Tell program which bucket to upload to
s3 = boto3.resource('s3')
BUCKET = "cpds1937053"

#upload 1st image
s3.Bucket(BUCKET).upload_file("image1.jpg", "image1.jpg")

#wait 30 seconds
time.sleep(30)

#upload 2nd image
s3.Bucket(BUCKET).upload_file("image2.png", "image2.png")


#wait 30 seconds
time.sleep(30)

#upload 3rd image
s3.Bucket(BUCKET).upload_file("image3.jpg", "image3.jpg")

#wait 30 seconds
time.sleep(30)

#upload 4th image
s3.Bucket(BUCKET).upload_file("image4.jpg", "image4.jpg")

#wait 30 seconds
time.sleep(30)

#upload 5th image
s3.Bucket(BUCKET).upload_file("image5.jpg", "image5.jpg")

print("All images uploaded")