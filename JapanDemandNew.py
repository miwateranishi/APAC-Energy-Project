import requests
import datetime

Today=datetime.datetime.now()
Today=Today.strftime('%Y%m%d')


#Chubu
URL1='http://denki-yoho.chuden.jp/denki_yoho_content_data/juyo_cepco003.csv'
Data1=requests.get(URL1)
Demand1=Data1.text
file1=open(r'C:\Users\mteranishi\Documents\CSV Files Energy\Chubu Denryoku\ChubuDemand_'+Today+'.csv','w+',encoding=Data1.encoding)
file1.write(Demand1)
file1.close()
print(URL1)

#Chugoku
URL2='http://www.energia.co.jp/jukyuu/sys/juyo_07_'+Today+'.csv'
Data2=requests.get(URL2)
Demand2=Data2.text
file2=open(r'C:\Users\mteranishi\Documents\CSV Files Energy\Chugoku Denryoku\ChugokuDemand_'+Today+'.csv','w+',encoding=Data2.encoding)
file2.write(Demand2)
file2.close()
print(URL2)

#Hokkaido
URL3='http://denkiyoho.hepco.co.jp/area/data/juyo_01_'+Today+'.csv'
Data3=requests.get(URL3)
Demand3=Data3.text
file3=open(r'C:\Users\mteranishi\Documents\CSV Files Energy\Hokkaido Denryoku\HokkaidoDemand_'+Today+'.csv','w+',encoding=Data3.encoding)
file3.write(Demand3)
file3.close()
print(URL3)

#Hokuriku
URL4='http://www.rikuden.co.jp/denki-yoho/csv/juyo_05_' + Today + '.csv'
Data4=requests.get(URL4)#gets data from web
Demand4=Data4.text
file4=open(r'C:\Users\mteranishi\Documents\CSV Files Energy\Hokuriku Denryoku\HokurikuDemand_'+Today+'.csv','w+',encoding=Data4.encoding)
file4.write(Demand4)
file4.close()
print (URL4)

#Kansai
URL5='http://www.kepco.co.jp/yamasou/juyo1_kansai.csv'
Data5=requests.get(URL5)
Demand5=Data5.text
file5=open(r'C:\Users\mteranishi\Documents\CSV Files Energy\Kansai Denryoku\KansaiDemand_'+Today+'.csv','w+',encoding=Data5.encoding)
file5.write(Demand5)
file5.close()
print(URL5)

#Kyushu
URL6='http://www.kyuden.co.jp/power_usages/csv/juyo-hourly-' + Today + '.csv'
Data6=requests.get(URL6)#gets data from web
Demand6=Data6.text
file6=open(r'C:\Users\mteranishi\Documents\CSV Files Energy\Kyushu Denryoku\KyushuDemand_'+Today+'.csv','w+',encoding=Data6.encoding)
file6.write(Demand6)
file6.close()
print(URL6)

#Shikoku
URL7='http://www.yonden.co.jp/denkiyoho/juyo_shikoku.csv'
Data7=requests.get(URL7)
Demand7=Data7.text
file7=open(r'C:\Users\mteranishi\Documents\CSV Files Energy\Shikoku Denryoku\ShikokuDemand_'+Today+'.csv','w+',encoding=Data7.encoding)
file7.write(Demand7)
file7.close()
print(URL7)

#Tohoku
URL8='http://setsuden.tohoku-epco.co.jp/common/demand/juyo_02_'+Today+'.csv'
Data8=requests.get(URL8)
Demand8=Data8.text
file8=open(r'C:\Users\mteranishi\Documents\CSV Files Energy\Tohoku Denryoku\TohokuDemand_'+Today+'.csv','w+',encoding=Data8.encoding)
file8.write(Demand8)
file8.close()
print(URL8)

#Kanto/Tokyo
URL9='http://www.tepco.co.jp/forecast/html/images/juyo-j.csv'
Data9=requests.get(URL9)
Demand9=Data9.text
file9=open(r'C:\Users\mteranishi\Documents\CSV Files Energy\Tokyo Denryoku\TokyoDemand_'+Today+'.csv','w+',encoding=Data9.encoding)
file9.write(Demand9)
file9.close()
print(URL9)


