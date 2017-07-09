#!/usr/bin/env python
'''
This script give the mac address of connected
wireless networks through laptop.It take the
information from windows registry in windows.
'''
from _winreg import *   #library helps to extract information from the windows registry in windows

def val2addr(val):      #it will convert the hex value into redable mac address
    addr = ''
    for ch in val:
        addr += '%02x '%ord(ch)
        addr = addr.strip(' ').replace(' ',':')[0:17]
        return addr

def printNets():                                    #it will print the key of different networks
    net="SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged" #path of the key registry
    key = OpenKey(HKEY_LOCAL_MACHINE, net)          #through OpenKey we access the windows registry
    print '\n[*] Networks You have Joined.'
    for i in range(10):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key,str(guid))         #openning the network key
            (n, addr, t) = EnumValue(netKey, 5)     #getting some part of information of that key
            (n, name, t) = EnumValue(netKey, 4)
            macAddr = val2addr(addr)                #calling function to get readable mac address
            netName = str(name)
            print '[+] ' + netName + ' ' + macAddr
            CloseKey(netKey)
        except Exception as e:
            print '[-] ERROR ='+str(e)

def main():
    printNets()             #calling the print function

if __name__ == '__main__':  #main code
    main()
