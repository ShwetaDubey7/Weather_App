import os
from tkinter import*
import tkinter as tk
import requests 
import time

def openweatherdata():
    citiesdata = dataentry.get()
    #api key = 021a11b4d8d15077eb8b4f44f9239d97
    apilink = "https://api.openweathermap.org/data/2.5/weather?q=" + citiesdata + "&appid=021a11b4d8d15077eb8b4f44f9239d97"
    # convert kelvin to celcius
    ktc = 273.2
    json = requests.get(apilink).json()
    apidata = json['weather'][0]['main']
    temperatue = int(json['main']['temp'] - ktc)
    feelslike = int(json['main']['feels_like'] - ktc)
    lowest = int(json['main']['temp_min'] - ktc)
    highest = int(json['main']['temp_max'] - ktc)
    pressure = json['main']['pressure']
    humidity = json['main']['humidity']
    windspeed = json['wind']['speed']

    maindata = apidata + "\n" + str(temperatue) + "C"
    additionalinfo = "\n" + "Feel like: " + str(feelslike) + "C" + "\n" + "\n" + "Lowest Temperature" + str(lowest) + "C" + "\n" + "Highest Temperature" + str(highest) + "C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "\n" + "Wind Speed: " + str(windspeed)
    # DISPLAY DATA
    data1.config(text=maindata)
    data2.config(text=additionalinfo)
    
os.environ["DISPLAY"] = "99:"

# INITIALISING TKINTER
weatherapp = tk.Tk()
weatherapp.title("Weather Application")
weatherapp.geometry("700x800")
weatherapp.configure(bg="lightblue")

# FONT
font1 = ("times",25,"bold")
font2 = ("times",50,"bold")

# LABELS
data1 = Label(weatherapp, font=font2)
data2 = Label(weatherapp, font=font1)

# ENTRY
dataentry = Entry(weatherapp, justify='center', width=30,font=data2)
dataentry.focus()
dataentry.bind('<Return>', openweatherdata)

Checkbutton = Button(weatherapp, text="Search",command=openweatherdata)

#Build User Interface
dataentry.pack(pady=35)
data1.pack()
data2.pack()
Checkbutton.pack(pady=45)

weatherapp.mainloop()
