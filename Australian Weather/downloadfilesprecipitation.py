# note this script is not fully autonomous. You will need to access the stations via http://www.bom.gov.au/climate/data/ first. This can be made autonomous by using the chrome webdriver library.

import urllib2 # library allows to access url
import re # Regular expression library. I used it to search for ".zip" extension in the links.
import os # allows to open and write files
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
    remote = "http://www.bom.gov.au/tmp/cdio/IDCJAC0009_"+Station+"_2017.zip" # This is the link to the file.
    filename = "C:\Users\\thanh\Desktop\Weather_Data"+"/"+City+"/Rainfall/rainfall.zip" # This is where I want to save the file
    print "Copying from " + remote + " to " + filename
    f = open(filename,'wb')
    f.write(urllib2.urlopen(remote).read())
    f.close()
    zip = zipfile.ZipFile(filename)
    zip.extractall("//"+vm+"//c$//Users//thanh//Desktop//Weather_Data//"+ City +"//Rainfall")
