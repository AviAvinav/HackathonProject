from chempy import balance_stoichiometry
import tkinter as tk

x=""

#functions
def balance():
  reac, prod = balance_stoichiometry({textEntryBox1.get()},{textEntryBox2.get()})
  x=("Reactants: " + dict(reac) + "\n" + "Products: " + dict(proc))

window = tk.Tk()
window.Title("Hackathon Project - ChemVis")
window.configure(background="black")


tk.Label(window, text="Chem Visualisations", bg="black", fg="white", font=("arial", 21)).grid(row=0, column=0, sticky=W)
tk.Label(window, text="Here you can do stuff in chemistry", bg="black", fg="white", font=("none", 16)).grid(row=1, column=0, sticky=W)


tk.Label(window, text="Enter Reactants: ", bg="black", fg="white", font=("none", 14)).grid(row=2, column=0, sticky=W)
textEntryBox1 = tk.Entry(window, width=10, bg="black")
textEntryBox1.grid(row=3, column=0, sticky=W)


tk.Label(window, text="Enter Products: ", bg="black", fg="white", font=("none", 14)).grid(row=2, column=2, sticky=W)
textEntryBox2 = tk.Entry(window, width=10, bg="black")
textEntryBox2.grid(row=3, column=2, sticky=W)


tk.Button(window, text="Balance the reactions", width=8, font="none", command=balance).grid(row=4, column=0, sticky=W)

labelx = tk.Label(window, text=x, bg="white", fg="black", width=75, height=6, font=("none", 13))
labelx.grid(row=5, column=0, sticky=W)

window.mainloop()

