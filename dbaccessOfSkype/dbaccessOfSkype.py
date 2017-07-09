#!/usr/bin/env python
'''
to get the required information from the
table of database.We use sqlite3 here.
'''
import sqlite3          #sqlite databse

def printProfile(skypeDB):              #here we using skype database for extracting the information
	conn = sqlite3.connect(skypeDB) #connecting to the database
	c = conn.cursor()               #getting the cursor like a pointer in some OS
	c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")  #through sql command extracting required collumn from table
	for row in c:                   #printing required information
		print '[*] -- Found Account --'
		print '[+] User: '+str(row[0])
		print '[+] Skype Username: '+str(row[1])
		print '[+] Location: '+str(row[2])+','+str(row[3])
		print '[+] Profile Date: '+str(row[4])

def main():
	skypeDB = "/home/shikhar/Downloads/main.db"         #giving the path of database
	printProfile(skypeDB)                               #calling the function

if __name__ == "__main__":          #code starts from here
	main()
