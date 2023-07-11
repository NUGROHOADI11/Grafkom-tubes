# --------------------------------------------------------------------------------------------------
# generate line bressenham
# --------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import math

x_values = []
y_values = []

fig, ax = plt.subplots()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("User Input Line Plot")
ax.grid(True)

def onclick(event):
    if len(x_values) >= 2:
        return

    x = event.xdata
    y = event.ydata
    x_values.append(x)
    y_values.append(y)
    ax.plot(x, y, 'ro')

    if len(x_values) == 2:
        ax.plot(x_values, y_values, 'b-')

        x0 = round(x_values[0])
        y0 = round(y_values[0])
        x1 = round(x_values[1])
        y1 = round(y_values[1])

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        err = dx - dy

        turns = []
        while x0 != x1 or y0 != y1:
            turns.append((x0, y0))
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

        turns.append((x1, y1))

        print("Coordinates:")
        print(f"Point 1: ({round(x_values[0])}, {round(y_values[0])})")
        print(f"Point 2: ({round(x_values[1])}, {round(y_values[1])})")

        print("Step-by-step Turns:")
        for i, turn in enumerate(turns):
            print(f"Step {i+1}: {turn}")

    plt.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()
