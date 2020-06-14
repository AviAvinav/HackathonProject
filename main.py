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

def search():
  os.open('search.py')
  window.destroy()
  exit()

def ChemVis():
  os.open('chemScreen.py')
  window.destroy()
  exit()

def Graphs():
  os.open('graphs.py')
  window.destroy()
  exit()
  
def exiting():
  window.destroy()
  exit()
  
#code for pics and name
pic = tk.PhotoImage(file="images//First.jpg")
tk.Label(window, bg="black", image=pic).grid(row=0, column=0, sticky=W)
tk.Label(window, text="Hackathon Project", bg="black", fg="white", font="none").grid(row=1, column=0, sticky=W)

#code for population buttons

#population densities
tk.Button(window, text='Population Densities', width=6, command=population_densities).grid(row=2, column=0, sticky=W)

#Search
tk.Button(window, text='Search', width=6, command=search).grid(row=3, column=0, sticky=W)

#Chem Visualisations
tk.Button(window, text='Chem Visualisations', width=6, command=ChemVis).grid(row=4, column=0, sticky=W)

#Graphs
tk.Button(window, text='Graphs', width=6, command=Graphs).grid(row=5, column=0, sticky=W)

#Exit Button
tk.Button(window, text='Exit', width=6, command=exiting).grid(row=6, column=0, sticky=W)

    
window.mainloop()
