import urllib2 # library allows to access url
import re # Regular expression library. I used it to search for ".zip" extension in the links.
import os # allows to open and write files
import zipfile

folder = "C:\Users\\thanh\Desktop\Solar_Data_Forecast"

if not os.path.exists(folder): # Directory that I want to save the image to
    os.mkdir(folder) # If no directory create it

url = "http://www.nemweb.com.au/REPORTS/CURRENT/ROOFTOP_PV/FORECAST/"
source = urllib2.urlopen(url).read()

datafiles = re.findall(r'[\w]+\.zip',source, re.M) # regex finds datafiles with ending .zip


for datafile in datafiles:
    remote = url + datafile;
    filename = folder + "/" + datafile
    print "Copying from " + remote + " to " + filename
    if not os.path.exists(filename): #only saves the file if a file with the same name does not exist
        f = open(filename, 'wb')
        f.write(urllib2.urlopen(remote).read())
        f.close()
        zip = zipfile.ZipFile(filename)
        zip.extractall(r'//Apac-intern-vm3/c$/Users/thanh/Desktop/Solar_Power_Generation_Forecast/')
        zip.extractall(r'//Mtippett-vm1/c$/Users/thanh/Desktop/Solar_Power_Generation_Forecast/')
        zip.extractall(r'//Mtippett-vm2/c$/Users/thanh/Desktop/Solar_Power_Generation_Forecast/')
        zip.extractall(r'//Mtippett-vm3/c$/Users/thanh/Desktop/Solar_Power_Generation_Forecast/')

