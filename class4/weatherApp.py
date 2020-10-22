# importing the libraries
from tkinter import *
import requests
import json
import datetime

# necessary details
root = Tk()
root.title("Weather App")
root.geometry("450x700")
root['background'] = "WHITE"

panel = Label(root)
panel.place(x=0, y=520)

# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 15))
date.place(x=5, y=130)
month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15))
month.place(x=100, y=130)

# Time
hour = Label(root, text=dt.strftime('%I : %M %p'),
             bg='white', font=("bold", 15))
hour.place(x=10, y=160)

# City Search
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W + E + N + S)


def city_name():

    # API Call
    api_key = "42739001c73e4beba97121628202110"
    base_url = "http://api.weatherapi.com/v1/current.json?"
    complete_url = base_url + "key=" + api_key + "&q=" + city_entry.get()
    response = requests.get(complete_url)
    current_weather = response.json()
    if 'error' not in current_weather.keys():
        # WEATHER INFO
        y = current_weather["current"]
        current_temprature=str(y['temp_c'])+"c"
        current_pressure = y['pressure_mb']
        current_humidiy = y['humidity']
        discription=y['condition']['text']
        current_cloud = y['cloud']

        #LOCATION INFO
        city_name=current_weather['location']['name']
        country_name=current_weather['location']['country']
        lan=current_weather['location']['lon']
        lat=current_weather['location']['lat']

        # Adding the received info into the screen
        lable_temp.configure(text=current_temprature)
        lable_pressure.configure(text=current_pressure)
        lable_humidity.configure(text=current_humidiy)
        labl_desc.configure(text=discription)
        labl_cloud.configure(text=current_cloud)
        lable_citi.configure(text=city_name)
        lable_country.configure(text=country_name)
        lable_lon.configure(text=lan)
        lable_lat.configure(text=lat)
    else:
        # print the error message
        print(current_weather['error']['message'])


# Search Bar and Button
city_nameButton = Button(root, text="Search", command=city_name)
city_nameButton.grid(row=1, column=1, padx=5, stick=W + E + N + S)

# Country  Names and Coordinates
lable_citi = Label(root, text="...", width=0,
                   bg='white', font=("bold", 15))
lable_citi.place(x=10, y=63)

lable_country = Label(root, text="...", width=0,
                      bg='white', font=("bold", 15))
lable_country.place(x=135, y=63)

lable_lon = Label(root, text="...", width=0,
                  bg='white', font=("Helvetica", 15))
lable_lon.place(x=25, y=95)
lable_lat = Label(root, text="...", width=0,
                  bg='white', font=("Helvetica", 15))
lable_lat.place(x=95, y=95)

# Current Temperature

lable_temp = Label(root, text="...", width=0, bg='white',
                   font=("Helvetica", 110), fg='black')
lable_temp.place(x=18, y=220)

# Other weather details
humidity=Label(root, text="humidity% : ", width=0,
             bg='white', font=("bold", 15))
humidity.place(x=3, y=370)

lable_humidity = Label(root, text="...", width=0,
                       bg='white', font=("bold", 15))
lable_humidity.place(x=128, y=370)

pressure=Label(root, text="pressure: ", width=0,
             bg='white', font=("bold", 15))
pressure.place(x=3, y=400)

lable_pressure = Label(root, text="...", width=0,
             bg='white', font=("bold", 15))
lable_pressure.place(x=128, y=400)

desc=Label(root, text="description : ", width=0,
             bg='white', font=("bold", 15))
desc.place(x=3, y=430)

labl_desc = Label(root, text="...", width=0,
                 bg='white', font=("bold", 15))
labl_desc.place(x=128, y=430)

cloud = Label(root, text="cloud %: ", width=0,
             bg='white', font=("bold", 15))
cloud.place(x=3, y=460)

labl_cloud = Label(root, text="...", width=0,
                 bg='white', font=("bold", 15))
labl_cloud.place(x=128, y=460)

root.mainloop()


