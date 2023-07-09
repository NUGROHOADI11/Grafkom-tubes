# --------------------------------------------------------------------------------------------------
# clipping (cohen-sutterland)
# --------------------------------------------------------------------------------------------------

import tkinter as tk

# Initialize the window and canvas
window = tk.Tk()
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()
canvas.configure(borderwidth=2, relief="solid", highlightthickness=2)

# Variables to store the line coordinates
x1, y1 = None, None
x2, y2 = None, None

# Function to handle mouse click events
def handle_mouse_click(event):
    global x1, y1
    x1 = min(max(event.x, 0), canvas_width)
    y1 = min(max(event.y, 0), canvas_height)

# Function to handle mouse release events
def handle_mouse_release(event):
    global x2, y2
    x2 = min(max(event.x, 0), canvas_width)
    y2 = min(max(event.y, 0), canvas_height)
    draw_line()
    display_coordinates()

# Function to draw the line on the canvas
def draw_line():
    canvas.create_line(x1, y1, x2, y2)

# Function to display the coordinates in the console
def display_coordinates():
    coordinates = f"({x1}, {y1}) - ({x2}, {y2})"
    print("Line coordinates:", coordinates)

# Bind mouse click and release events to the canvas
canvas.bind("<Button-1>", handle_mouse_click)
canvas.bind("<ButtonRelease-1>", handle_mouse_release)

# Start the GUI main loop
window.mainloop()
