from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.support.select import Select
import time
import os
import datetime
#import pdb
#MonthList=["January","February","March","April","May","June","July","August","September","October","November"]
#MonthNoList=["01","02","03","04","05","06","07","08","09","10","11"]

CityList=["Tokyo","Yokohama","Kawasaki","Osaka","Kyoto","Kobe","Sapporo","Sendai","Fukuoka","Nagoya","Hiroshima","Kanazawa","Kochi"]
#CityList=["Kawasaki","Osaka","Kyoto","Kobe","Sapporo","Sendai","Fukuoka","Nagoya","Hiroshima","Kanazawa","Kochi"]
Today=datetime.date.today()
OneDay=datetime.timedelta(days=1)

driver=webdriver.Chrome("C:\\Users\mteranishi\Documents\\Python Scripts\\chromedriver.exe")

for City in CityList:
	MonthTest="MonthTest"
	StartDate=Today - datetime.timedelta(days=5) #choose how many days back you want to start taking data from
	TotalDays=(Today - StartDate).days +1
	for x in range(TotalDays): 
		Day = StartDate + datetime.timedelta(days=x)
		MonthStr = Day.strftime("%B")
		Month = Day.strftime("%m")
		Year = Day.strftime("%y")
		DayNum = Day.strftime("%d")
		DateDay = Day.strftime("%x")
		
		if (int(str(DayNum))<10):  #Converts DayNum into a single character string if less than 10
			a,b=str(DayNum)
			DayNum=b
		
		if not (MonthTest == MonthStr):  # Changes the URL for each month
			if (MonthTest=="MonthTest"):
				driver.get("https://www.timeanddate.com/weather/japan/" + City + "/historic")
				time.sleep(2)
			
			MonthTest=MonthStr
			driver.find_element_by_xpath('//*[@id="month"]').send_keys(MonthStr + " 20" + Year)
			time.sleep(2)
			
		driver.find_element_by_xpath('//*[@id="wt-his-select"]').send_keys( DayNum + " " + MonthStr + " 20" + Year)
		print("Year:" + Year)
		time.sleep(1)
		
		Q=open( "C:\\users\\mteranishi\\Documents\\Japan Weather\\New Weather Data\\" + City + " " + DayNum+ "-" + MonthStr + "20" + Year + ".txt","w+")
		Q.write("City:"+City+".\n")
		for y in range(1,49):
			try:
				timestamp=driver.find_element_by_xpath('//*[@id="wt-his"]/tbody/tr[' + str(y) + ']/th').text
				if (len(timestamp)>8):
					timestamp=timestamp[0:8]
					
				if (len(timestamp)==7):
					timestamp= "0" + timestamp
			
				timestamp=timestamp[0:5]
				#print( "debug: 2.")
	
				temp=driver.find_element_by_xpath('//*[@id="wt-his"]/tbody/tr[' + str(y) + ']/td[2]').text
				wind=driver.find_element_by_xpath('//*[@id="wt-his"]/tbody/tr[' + str(y) + ']/td[4]').text
				windtest=wind[0:6]
				a,b,c,d,e,f=windtest
				#print( "debug: 3.")
				if (d=="w"):
					wind="0 km/h"
				Q.write( DateDay + " " + timestamp + ";" + temp + "," + wind + ".\n")
                
			
			except:
				print("fail" + str(y) + "---" + DayNum+ "-" + MonthStr)
				pass
		Q.close()
	
driver.quit()
