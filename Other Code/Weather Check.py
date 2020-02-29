#! python3

# plovdivForecast.py - takes the weather forecast for Plovdiv
# for the next 10 days and displays it - sinoptik.bg

import requests
impor

# Web data collection

res_temp = requests.get('https://www.sinoptik.bg/plovdiv-bulgaria-100728193')
plovdiv_temp_now = bs4.BeautifulSoup(res_temp.text, features="lxml")

res_10day = requests.get('https://www.sinoptik.bg/plovdiv-bulgaria-100728193/10-days')
plovdiv_temp_10day = bs4.BeautifulSoup(res_10day.text, features="lxml")

# Transform the data

# Data for res_temp/plovdiv_temp_now

elem_temp_now = plovdiv_temp_now.select('.wfCurrentTemp')
elem_feel_now = plovdiv_temp_now.select('.wfCurrentFeelTemp')
elem_desc_now = plovdiv_temp_now.select('.wfCurrentContent strong')
elem_wind_now = plovdiv_temp_now.select('.wfCurrentWind')
wind_regex = re.compile(r'\d.\d\s[m]\W[s]')

# Data for res_10day/plovdiv_temp_10day

elem_date_10day = plovdiv_temp_10day.select('.wf10dayRightDate')
elem_temp_max_10day = plovdiv_temp_10day.select('.wf10dayRightTemp')
elem_temp_min_10day = plovdiv_temp_10day.select('.wf10dayRightTempLow')
elem_desc_10day = plovdiv_temp_10day.select('.wf10dayRightImg')
elem_rain_10day = plovdiv_temp_10day.select('.wf10dayRightRainValue')
elem_wind_10day = plovdiv_temp_10day.select('.wf10dayRightWind')
regex_10day = re.compile(r'(alt=")(.*?)("\s)')

# Visualize the data

# Visualization - 10 day forecast

for i in range(0, -10, -1):
    print('Времето в Пловдив на ' + elem_date_10day[i].getText() + ' ще е:')
    print('Прогноза: ' + regex_10day.search(str(elem_desc_10day[i])).group(2))
    print('Max температура: ' + elem_temp_max_10day[i].getText())
    print('Мин температура: ' + elem_temp_min_10day[i].getText())
    print('Вероятност за валежи: ' + elem_rain_10day[i].getText())
    print('Вятър: ' + wind_regex.search(str(elem_wind_10day[i])).group())
    print()

# Visualization of the current forecast

print('Времето в Пловдив е:')
print('В момента: ' + elem_desc_now[0].getText())
print('Температура: ' + elem_temp_now[0].getText())
print(elem_feel_now[0].getText())
print('Вятър: ' + wind_regex.search(str(elem_wind_now[0])).group())
print()
