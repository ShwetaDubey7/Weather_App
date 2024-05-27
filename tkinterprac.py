import os
from tkinter import*
from tkinter.messagebox import*
from tkinter.ttk import*

from root import root

os.environ["DISPLAY"] = ":0"
#
weather = Tk()
weather.title("Temperature Difference")
weather.configure(bg="teal")
weather.geometry("600x1000")

labelhighest = Label(weather, text="High Temperature")
labellowest = Label(weather, text="Low Temperature")
labeldiff = Label(weather, text="Difference in Temperature")

entryhighest = Entry(weather)
entrylowest = Entry(weather)
entrydiff = Entry(weather)

def diff():
    lowest = entrylowest.get()
    highest = entryhighest.get()
    lowest = float(lowest)
    highest = float(highest)
    tempdiff = highest - lowest
    entrydiff.insert(0,tempdiff)

calculate = Button(weather, text="diff", command=diff)

    #building UI

labelhighest.grid(row=1,column=0)
entryhighest.grid(row=1,column=1)
labellowest.grid(row=2,column=0)
entrylowest.grid(row=2,column=1)
calculate.grid(row=3,column=0)
labeldiff.grid(row=4,column=0)
entrydiff.grid(row=4,column=1)

root.mainloop()