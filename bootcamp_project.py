import requests

from datetime import datetime

api_key = '34845a85a98f47ccb5dae0c153fd06bc'
location = input("Enter the name of city : ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp'])- 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt= api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S: %p")

with open('bootcamp_project.txt', 'w') as project:
    project.write("---------------------------------------------------------------"+"\n")
    project.write("Weather Stats for - {} || {}".format(location.upper(),date_time+"\n"))
    project.write("---------------------------------------------------------------"+"\n")

    project.write("Current Temperature is: {:.2f} deg C".format(temp_city)+"\n")
    project.write("Current Weather Description : ")
    project.write(str(weather_desc.upper()))
    project.write("\n")
    project.write("Current Humidity : ") 
    project.write(str(hmdt)),
    project.write('%'+"\n")
    project.write("Current Wind Speed : ")
    project.write(str(wind_spd)) 
    project.write('kmph'+"\n")
    project.close()