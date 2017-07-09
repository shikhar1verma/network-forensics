#!/usr/bin/env python
'''
This script will print all the files and folders
deleted and present in recycle bin in windows.
'''
import os
from _winreg import *           #module to tweak the windows key registry

def sid2user(sid):                                                      #It wil open the required key in the windows registry
      try:
            key = OpenKey(HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"+ '\\' + sid)
            (value, type) = QueryValueEx(key, 'ProfileImagePath')
            user = value.split('\\')[-1]
            return user
      except:
            return sid


def returnDir():                                                        #It will give the path of Recycle bin in windows
     dirs=['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
     for recycleDir in dirs:
          if os.path.isdir(recycleDir): return recycleDir
     return None

def findRecycled(recycleDir):                                           #It will print the list of deleted files and folders present in Recycle bin
      dirList = os.listdir(recycleDir)
      for sid in dirList:
           files = os.listdir(recycleDir + sid)
           user = sid2user(sid)
           print '\n[*] Listing Files For User: ' + str(user)
           for file in files:
                 print '[+] Found File: ' + str(file)

def main():                                     #the main function
      recycledDir = returnDir()
      findRecycled(recycledDir)

if __name__ == '__main__':
      main()                                    #the code starts from here
