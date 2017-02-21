import urllib2 # library allows to access url
import os # allows to open and write files
from datetime import timedelta, date # this library allows me to use timestamps.
import html2text # this library allows me to conver a html page to a text file.
from shutil import copyfile # this library allows me to copy the file.

Cities = ["Canberra", "Newcastle", "Sydney", "Brisbane", "Goldcoast", "Adelaide", "Hobart", "Melbourne", "Perth"]

folder = "C:\Users\\thanh\Desktop\Weather_Data"

def daterange(start_date, end_date): # I need this to loop from 15/11/2016 to "today". This is where I made the function to do tihs.
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2016, 11, 15)
end_date = date.today()
for single_date in daterange(start_date, end_date): # this is the actual loop
    URLfile = single_date.strftime("%Y/%m/%d")
    datafile = single_date.strftime("%Y%m%d")
    Canberraurl = "https://www.wunderground.com/history/airport/YSCB/"+URLfile+"/DailyHistory.html?req_city=Canberra&req_statename=Australia&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=94926&format=1"
    Newcastleurl = "https://www.wunderground.com/history/airport/YWLM/"+URLfile+"/DailyHistory.html?req_city=Newcastle&req_statename=Australia&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=WYWLM&format=1"
    Sydneyurl = "https://www.wunderground.com/history/airport/YSSY/"+URLfile+"/DailyHistory.html?req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1"
    Brisbaneurl = "https://www.wunderground.com/history/airport/YBBN/"+URLfile+"/DailyHistory.html?req_city=Brisbane&req_statename=Australia&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=94578&format=1"
    Goldcoasturl = "https://www.wunderground.com/history/airport/YBCG/"+URLfile+"/DailyHistory.html?req_city=Gold%20Coast&req_statename=Australia&reqdb.zip=00000&reqdb.magic=11&reqdb.wmo=94580&format=1"
    Adelaideurl = "https://www.wunderground.com/history/airport/YPAD/"+URLfile+"/DailyHistory.html?req_city=Adelaide&req_statename=Australia&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=94672&format=1"
    Hobarturl = "https://www.wunderground.com/history/airport/YMHB/"+URLfile+"/DailyHistory.html?format=1"
    Melbourneurl = "https://www.wunderground.com/history/airport/YMMB/"+URLfile+"/DailyHistory.html?req_city=Melbourne&req_state=&req_statename=Australia&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=94868&format=1"
    Perthurl = "https://www.wunderground.com/history/airport/YPPH/"+URLfile+"/DailyHistory.html?format=1"    
    for City in Cities:
        if City == "Canberra":
            url = Canberraurl
            vm = "Apac-intern-vm3"
        elif City == "Newcastle":
            url = Newcastleurl
            vm = "Apac-intern-vm3"
        elif City == "Sydney":
            url = Sydneyurl
            vm = "Apac-intern-vm3"
        elif City == "Brisbane":
            url = Brisbaneurl
            vm = "Mtippett-vm2"            
        elif City == "Goldcoast":
            url = Goldcoasturl
            vm = "Mtippett-vm2"
        elif City == "Adelaide":
            url = Adelaideurl
            vm = "Mtippett-vm3"
        elif City == "Hobart":
            url = Hobarturl
            vm = "Apac-intern-vm3"
        elif City == "Melbourne":
            url = Melbourneurl
            vm = "Apac-intern-vm3"
        elif City == "Perth":
            url = Perthurl
            vm = "Mtippett-vm1"

        filename = folder + "/"+City+"/" + datafile+".txt"
        if not os.path.exists(filename):
            print "Copying from " + url + " to " + filename
            html2text.BODY_WIDTH = 0 # displays word wrapping so no line breaks are made in the middle of a line.
            html_content = urllib2.urlopen(url).read()  # read the html page
            rendered_content = html2text.html2text(html_content) # convert it to text and save to variable rendered_content
            f = open(filename,'w')
            f.write(rendered_content) #save the txt file
            f.close()
            copyfile(filename, "//"+vm+"//c$//Users//thanh//Desktop//Weather_Data//"+ City +"//"+datafile + ".txt")
