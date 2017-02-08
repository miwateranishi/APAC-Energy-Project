# note this script is not fully autonomous. You will need to access the stations via http://www.bom.gov.au/climate/data/ first. Can be fixed by using webdriver.

import urllib2
import re
import os
import zipfile

Cities = ["Canberra", "Newcastle", "Sydney", "Brisbane", "Goldcoast", "Adelaide", "Hobart", "Melbourne"]




for City in Cities:
    if City == "Canberra":
        Station = "070247"
        vm = "Apac-intern-vm3"
    elif City == "Newcastle":
        Station = "061055"
        vm = "Apac-intern-vm3"
    elif City == "Sydney":
        Station = "066062"
        vm = "Apac-intern-vm3"
    elif City == "Brisbane":
        Station = "040913"
        vm = "Mtippett-vm2"            
    elif City == "Goldcoast":
        Station = "040416"
        vm = "Mtippett-vm2"
    elif City == "Adelaide":
        Station = "023090"
        vm = "Mtippett-vm3"
    elif City == "Hobart":
        Station = "094029"
        vm = "Apac-intern-vm3"
    elif City == "Melbourne":
        Station = "086338"
        vm = "Apac-intern-vm3"
    read = "http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_nccObsCode=136&p_display_type=dailyDataFile&p_startYear=&p_c=&p_stn_num=="+Station
    remote = "http://www.bom.gov.au/tmp/cdio/IDCJAC0009_"+Station+"_2017.zip"
    filename = "C:\Users\\thanh\Desktop\Weather_Data"+"/"+City+"/Rainfall/rainfall.zip"
    print "Copying from " + remote + " to " + filename
    f = open(filename,'wb')
    urllib2.urlopen(read).read()
    f.write(urllib2.urlopen(remote).read())
    f.close()
    zip = zipfile.ZipFile(filename)
    zip.extractall("//"+vm+"//c$//Users//thanh//Desktop//Weather_Data//"+ City +"//Rainfall")
