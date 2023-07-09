# --------------------------------------------------------------------------------------------------
# generate ellipse
# --------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

class EllipseDrawer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.grid(True, linestyle='--')

        self.points = []
        self.ellipse = None

        self.fig.canvas.mpl_connect('button_press_event', self.on_press)

    def on_press(self, event):
        if event.button == 1:
            self.points.append((event.xdata, event.ydata))
            self.draw_dots()

            if len(self.points) == 2:
                self.draw_ellipse()
                self.fig.canvas.mpl_disconnect(self.fig.canvas.mpl_connect('button_press_event', self.on_press))
                self.print_ellipse_coordinates()

    def draw_dots(self):
        x = [point[0] for point in self.points]
        y = [point[1] for point in self.points]
        self.ax.plot(x, y, 'ro')
        plt.draw()

    def draw_ellipse(self):
        start_x, start_y = self.points[0]
        end_x, end_y = self.points[1]
        center_x = (start_x + end_x) / 2
        center_y = (start_y + end_y) / 2
        width = abs(end_x - start_x)
        height = abs(end_y - start_y)

        self.ellipse = Ellipse((center_x, center_y), width, height, fill=False, edgecolor='black')
        self.ax.add_patch(self.ellipse)
        plt.draw()

    def print_ellipse_coordinates(self):
        start_x, start_y = self.points[0]
        end_x, end_y = self.points[1]
        center_x = (start_x + end_x) / 2
        center_y = (start_y + end_y) / 2
        width = abs(end_x - start_x)
        height = abs(end_y - start_y)

        print("Ellipse Coordinates:")
        print(f"Center: ({center_x}, {center_y})")
        print(f"Width: {width}")
        print(f"Height: {height}")

    def show(self):
        plt.show()

# Create the ellipse drawer instance and start the plot
drawer = EllipseDrawer()
drawer.show()
