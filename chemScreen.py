import chempy
import tkinter as tk

window = tk.Tk()
window.Title("Hackathon Project - ChemVis")
window.configure(background="black")


tk.Label(window, text="Chem Visualisations", bg="black", fg="white", font=("arial", 21)).grid(row=0, column=0, sticky=W)
tk.Label(window, text="Here you can do stuff in chemistry", bg="black", fg="white", font=("none", 16)).grid(row=1, column=0, sticky=W)

textEntryBox1 = tk.Entry(window, width=10, bg="black")
textEntryBox1.grid(row=2, column=0, sticky=W)

textEntryBox2 = tk.Entry(window, width=10, bg="black")
textEntryBox2.grid(row=2, column=2, sticky=W)


window.mainloop()
