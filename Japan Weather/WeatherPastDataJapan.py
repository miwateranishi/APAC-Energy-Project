import requests
import datetime
CityList=["Tokyo","Yokohama","Kawasaki,Kanagawa","Osaka-Shi","Kyoto","Kobe","Sapporo","Sendai-Shi","Fukuoka-Shi","Nagoya-Shi", "Hiroshima-Shi","Kanazawa-Shi","Kochi-Shi"]
#Tokyo: Tokyo, Yokohama, Kawasaki
#Kansai: Osaka-Shi, Kyoto, Kobe
#Hokkaido: Sapporo
#Tohoku: Sendai-Shi
#Kyushu: Fukuoka-Shi
#Chubu: Nagoya
#Chugoku: Hiroshima-Shi
#Hokuriku: Kanazawa-Shi
#Shikoku: Kochi-Shi

Today=datetime.date.today()
OneDay=datetime.timedelta(days=1)
for City in CityList:
    for x in range(1,10):
        URL = "http://api.worldweatheronline.com/free/v2/past-weather.ashx?q="+City+",Japan&format=xml&date="+str(Today-x*OneDay)+"&enddate="+str(Today-x*OneDay)+"&tp=1&key=KEYNUMBER"
        print(URL)
        R= requests.get(URL)
        if (City=="Kawasaki,Kanagawa"):
            City="Kawasaki"
        if (City=="Osaka-Shi"):
            City="Osaka"
        if (City=="Sendai-Shi"):
            City="Sendai"
        if (City=="Fukuoka-Shi"):
            City="Fukuoka"
        if (City=="Hiroshima-Shi"):
            City="Hiroshima"
        if (City=="Kanazawa-Shi"):
            City="Kanazawa"
        if (City=="Kochi-Shi"):
            City="Kochi"
        if (City=="Nagoya-Shi"):
            City="Nagoya"
        Q=open("C:\\users\\mteranishi\\Documents\\Japan Weather\\Past Weather Data\\" + City + " " + str(Today-x*OneDay)  + " Past.txt", "w+")
        Q.write(R.text)
        Q.close()


   
