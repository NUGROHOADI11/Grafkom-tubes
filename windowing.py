# --------------------------------------------------------------------------------------------------
# windowing (bressenham)
# --------------------------------------------------------------------------------------------------

import tkinter as tk

# Global variables to store line coordinates
x_start, y_start = None, None
x_end, y_end = None, None

def on_mouse_press(event):
    global x_start, y_start
    x_start = event.x
    y_start = event.y

def on_mouse_release(event):
    global x_end, y_end
    x_end = event.x
    y_end = event.y
    draw_line()
    display_coordinates()

def draw_line():
    # Draw the line on the canvas
    canvas.create_line(x_start, y_start, x_end, y_end)

def display_coordinates():
    print(f"Start: ({x_start}, {y_start})")
    print(f"End: ({x_end}, {y_end})")

# Create a window
window = tk.Tk()

# Set the window size and position
window.geometry("400x400")

# # Set the window outline
# window.configure(borderwidth=2, relief="solid", highlightthickness=2)

# Create a canvas
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()
canvas.configure(borderwidth=2, relief="solid", highlightthickness=2)

# Bind mouse events
canvas.bind("<Button-1>", on_mouse_press)
canvas.bind("<ButtonRelease-1>", on_mouse_release)

# Run the GUI main loop
window.mainloop()
