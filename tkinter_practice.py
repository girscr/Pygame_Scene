import tkinter as tk

#create root window
root = tk.Tk()

#create a Canvas widget
canvas = tk.Canvas(root, width = 800, height = 600)
canvas.grid()

#draw a line to the Canvas
canvas.create_line(10, 20, 210, 20)

root.mainloop()