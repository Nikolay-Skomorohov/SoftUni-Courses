#! python3

# plovdivForecast.py - takes the weather forecast for Plovdiv
# for the next 10 days and displays it - sinoptik.bg

import sys, os, requests, bs4, re

# Web data collection

resT = requests.get('https://www.sinoptik.bg/plovdiv-bulgaria-100728193')
resT.status_code == requests.codes.ok
plovdivT = bs4.BeautifulSoup(resT.text, features="lxml")

res10 = requests.get('https://www.sinoptik.bg/plovdiv-bulgaria-100728193/10-days')
res10.status_code == requests.codes.ok
plovdiv10 = bs4.BeautifulSoup(res10.text, features="lxml")

# Transform the data

# Data for resT/plovdivT

elemTempT = plovdivT.select('.wfCurrentTemp')
elemFeelT = plovdivT.select('.wfCurrentFeelTemp')
elemDescT = plovdivT.select('.wfCurrentContent strong')
elemWindT = plovdivT.select('.wfCurrentWind')
windRegex = re.compile(r'\d.\d\s[m]\W[s]')

# Data for res10/plovdiv10

elemDate10 = plovdiv10.select('.wf10dayRightDate')
elemTempMax10 = plovdiv10.select('.wf10dayRightTemp')
elemTempMin10 = plovdiv10.select('.wf10dayRightTempLow')
elemDesc10 = plovdiv10.select('.wf10dayRightImg')
elemRain10 = plovdiv10.select('.wf10dayRightRainValue')
elemWind10 = plovdiv10.select('.wf10dayRightWind')
foreRegex = re.compile(r'(alt=")(.*?)("\s)')

# Visualize the data

# Visualization - 10 day forecast

for i in range(0, -10, -1):
    print('Времето в Пловдив на ' + elemDate10[i].getText() + ' ще е:')
    print('Прогноза: ' + foreRegex.search(str(elemDesc10[i])).group(2))
    print('Max температура: ' + elemTempMax10[i].getText())
    print('Мин температура: ' + elemTempMin10[i].getText())
    print('Вероятност за валежи: ' + elemRain10[i].getText())
    print('Вятър: ' + windRegex.search(str(elemWind10[i])).group() )
    print()

# Visualization of the current forecast

print('Времето в Пловдив е:')
print('В момента: ' + elemDescT[0].getText())
print('Температура: ' + elemTempT[0].getText())
print(elemFeelT[0].getText())
print('Вятър: ' + windRegex.search(str(elemWindT[0])).group())
print()
