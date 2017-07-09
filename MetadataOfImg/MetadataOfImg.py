#!/usr/bin/env python
'''
this will tell about the EXIF metadata of the
image. And if the gps data available it will
prin the longitude and latitude of the location
'''
from PIL import Image                       #import the pillow library of python
from PIL.ExifTags import TAGS, GPSTAGS

path = raw_input('Enter path: ')                    #get the path of the image
image = Image.open(path)
print image
info = image._getexif()
exifData={}
if info:
    for (tag, value) in info.items():
        decoded = TAGS.get(tag, tag)
        if decoded == 'GPSInfo':
            for t in value:
                sub_decoded = GPSTAGS.get(t, t)
                gps_data[sub_decoded] = value[t]
        else:

            exifData[decoded] = value
    print exifData                                  #it will print the exif information of the image
    print gps_data                                  #it will tell about the location where the image was taken
