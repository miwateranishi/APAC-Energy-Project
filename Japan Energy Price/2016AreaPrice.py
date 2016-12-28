import requests

URL='http://www.jepx.org/market/excel/spot_2016.csv'
data=requests.get(URL)
energydata=data.text
file=open(r'C:\Users\mteranishi\Documents\CSV Files Energy\Japan Energy2016\AreaPrice.csv','w+',encoding=data.encoding)
file.write(energydata)
file.close()

print(URL)