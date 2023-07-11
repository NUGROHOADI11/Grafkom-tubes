
# # --------------------------------------------------------------------------------------------------
# # transform (rotate + reflection)
# # --------------------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np

# def draw_line(start_pos, end_pos):
#     """Draws the line between start_pos and end_pos."""
#     plt.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], color='blue')

# def reflect_line(start_pos, end_pos, x):
#     """Reflects the line over the vertical line x."""
#     reflected_start_x = 2 * x - start_pos[0]
#     reflected_end_x = 2 * x - end_pos[0]
#     reflected_start_pos = (reflected_start_x, start_pos[1])
#     reflected_end_pos = (reflected_end_x, end_pos[1])
#     plt.plot([reflected_start_pos[0], reflected_end_pos[0]], [reflected_start_pos[1], reflected_end_pos[1]], color='red')

# def rotate_line(start_pos, end_pos, angle):
#     """Rotates the line by the given angle around its midpoint."""
#     # Calculate midpoint
#     midpoint = ((start_pos[0] + end_pos[0]) / 2, (start_pos[1] + end_pos[1]) / 2)

#     # Translate the line to the origin
#     translated_start_pos = (start_pos[0] - midpoint[0], start_pos[1] - midpoint[1])
#     translated_end_pos = (end_pos[0] - midpoint[0], end_pos[1] - midpoint[1])

#     # Apply rotation
#     rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
#     rotated_start_pos = np.dot(rotation_matrix, translated_start_pos)
#     rotated_end_pos = np.dot(rotation_matrix, translated_end_pos)

#     # Translate back to the original position
#     rotated_start_pos = (rotated_start_pos[0] + midpoint[0], rotated_start_pos[1] + midpoint[1])
#     rotated_end_pos = (rotated_end_pos[0] + midpoint[0], rotated_end_pos[1] + midpoint[1])

#     # Return the rotated positions
#     return rotated_start_pos, rotated_end_pos

# # Variables to store line coordinates
# start_pos = None
# end_pos = None

# def onclick(event):
#     global start_pos, end_pos
#     if start_pos is None:
#         start_pos = (event.xdata, event.ydata)
#     elif end_pos is None:
#         end_pos = (event.xdata, event.ydata)

#         # Clear the plot
#         plt.clf()
#         ax.set_xlim(0, 10)
#         ax.set_ylim(0, 10)
#         ax.set_aspect('equal')

#         # Draw the line
#         draw_line(start_pos, end_pos)

#         # Reflect the line
#         x = event.xdata
#         reflect_line(start_pos, end_pos, x)

#         # Rotate the line
#         angle = np.pi / 4  # Example rotation angle of 45 degrees (pi/4 radians)
#         rotated_start_pos, rotated_end_pos = rotate_line(start_pos, end_pos, angle)

#         # Draw the rotated line
#         plt.plot([rotated_start_pos[0], rotated_end_pos[0]], [rotated_start_pos[1], rotated_end_pos[1]], color='green')

#         # Print the line coordinates
#         print("Line Coordinates:")
#         print("Start Pos:", start_pos)
#         print("End Pos:", end_pos)

#         # Calculate the reflected coordinates
#         reflected_start_x = 2 * x - start_pos[0]
#         reflected_end_x = 2 * x - end_pos[0]
#         reflected_start_pos = (reflected_start_x, start_pos[1])
#         reflected_end_pos = (reflected_end_x, end_pos[1])

#         # Print the transformed coordinates
#         print("\nReflected Line Coordinates:")
#         print("Reflected Start Pos:", reflected_start_pos)
#         print("Reflected End Pos:", reflected_end_pos)

#         # Print the rotated coordinates
#         print("Rotated Line Coordinates:")
#         print("Rotated Start Pos:", rotated_start_pos)
#         print("Rotated End Pos:", rotated_end_pos)
#         print()

#         # Reset the coordinates
#         start_pos = None
#         end_pos = None

#         # Set the aspect ratio to equal
#         ax.set_aspect('equal')

#         # Show the updated plot
#         plt.draw()

# # Set up the plot
# fig, ax = plt.subplots()
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 10)
# ax.set_aspect('equal')

# # Connect the mouse click event to the onclick function
# cid = fig.canvas.mpl_connect('button_press_event', onclick)

# plt.show()

# --------------------------------------------------------------------------------------------------
# transform (translation)
# --------------------------------------------------------------------------------------------------

import tkinter as tk

# Variables to store the coordinates and translation offset
coordinates = []
translation_offset = (0, 0)

def handle_click(event):
    global translation_offset

    # Add clicked coordinates to the list
    coordinates.append((event.x, event.y))

    # Draw a line segment on the canvas
    if len(coordinates) >= 2:
        canvas.create_line(coordinates[-2], coordinates[-1])

        # Translate the line
        translated_coordinates = translate_line(coordinates[-2], coordinates[-1], translation_offset)

        # Draw the translated line
        canvas.create_line(translated_coordinates[0], translated_coordinates[1], fill='red')

        # Display the coordinates
        canvas.create_text(coordinates[-2], text=f"({coordinates[-2][0]}, {coordinates[-2][1]})", anchor=tk.SW)
        canvas.create_text(coordinates[-1], text=f"({coordinates[-1][0]}, {coordinates[-1][1]})", anchor=tk.SW)
        canvas.create_text(translated_coordinates[-2], text=f"({translated_coordinates[-2][0]}, {translated_coordinates[-2][1]})", anchor=tk.SW)
        canvas.create_text(translated_coordinates[-1], text=f"({translated_coordinates[-1][0]}, {translated_coordinates[-1][1]})", anchor=tk.SW)

        # Print the original and transformed coordinates in the console
        print("Original Coordinates:")
        print(f"Start: ({coordinates[-2][0]}, {coordinates[-2][1]})")
        print(f"End: ({coordinates[-1][0]}, {coordinates[-1][1]})")

        print("Transformed Coordinates:")
        print(f"Start: ({translated_coordinates[0][0]}, {translated_coordinates[0][1]})")
        print(f"End: ({translated_coordinates[1][0]}, {translated_coordinates[1][1]})")
        print()

        # Disable further clicks
        canvas.unbind("<Button-1>")

         # Hide the translation buttons
        translate_button1.pack_forget()
        translate_button2.pack_forget()
        translate_button3.pack_forget()
        translate_button4.pack_forget()

        bl = tk.Label(text = "black: original line")
        rl = tk.Label(text = "red: translated line")
        rl.config(foreground="red")
        rl.pack()
        bl.pack()

    # Translate a line segment by a given offset.
def translate_line(start_point, end_point, offset):

    start_x, start_y = start_point
    end_x, end_y = end_point
    offset_x, offset_y = offset
    translated_start_point = (start_x + offset_x, start_y + offset_y)
    translated_end_point = (end_x + offset_x, end_y + offset_y)
    return (translated_start_point, translated_end_point)

def translate(dx, dy):
    global translation_offset
    translation_offset = (dx, dy)

    # Print the translation in the console
    if dx == 0 and dy < 0:
        print("Translate Up")
    elif dx == 0 and dy > 0:
        print("Translate Down")
    elif dx < 0 and dy == 0:
        print("Translate Left")
    elif dx > 0 and dy == 0:
        print("Translate Right")

# Create the main window
window = tk.Tk()

# Create a canvas for drawing
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()


# Create translation buttons
translate_button1 = tk.Button(window, text="Translate Up", command=lambda: translate(0, -40))
translate_button1.pack()
translate_button2 = tk.Button(window, text="Translate Down", command=lambda: translate(0, 40))
translate_button2.pack()
translate_button3 = tk.Button(window, text="Translate Left", command=lambda: translate(-40, 0))
translate_button3.pack()
translate_button4 = tk.Button(window, text="Translate Right", command=lambda: translate(40, 0))
translate_button4.pack()



# Bind the click event to the canvas
canvas.bind("<Button-1>", handle_click)

# Start the main event loop
window.mainloop()
