import tkinter as tk
import os

#code for main screen
window = tk.Tk()
window.title("Hackathon Project")
window.configure(background="black")

#functions
def population_densities():
  os.open('populationDensities.py')
  window.destroy()
  exit()
  
#code for pics and name
pic = tk.PhotoImage(file="images\\first.png")
tk.Label(window, text="Hackathon Project", bg="black", fg="white", font="none").grid(row=0, column=0, sticky=W)

#code for population buttons
   #population densities
tk.Button(window, text='Population Densities', width=6, command=population_densities).grid(row=1, column=0, sticky=W)
   
    
window.mainloop()
