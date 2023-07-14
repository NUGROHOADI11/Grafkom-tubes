# --------------------------------------------------------------------------------------------------
# generate ellipse
# --------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


class EllipseDrawer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True, linestyle='--')

        self.points = []
        self.ellipse = None
        self.lines = []  # Added list to store the lines

        self.fig.canvas.mpl_connect('button_press_event', self.on_press)

    def on_press(self, event):
        if event.button == 1:
            self.points.append((event.xdata, event.ydata))
            self.draw_dots()

            if len(self.points) == 2:
                self.draw_ellipse()
                self.draw_lines()  # Draw the lines
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

        self.ellipse = Ellipse((center_x, center_y), width, height, fill=True, edgecolor='black')
        self.ax.add_patch(self.ellipse)
        plt.draw()

    def draw_lines(self):
        start_x, start_y = self.points[0]
        end_x, end_y = self.points[1]
        center_x = (start_x + end_x) / 2
        center_y = (start_y + end_y) / 2
        width = abs(end_x - start_x)
        height = abs(end_y - start_y)

        self.lines.append(self.ax.axvline(start_x, linestyle='--', color='lightgreen'))
        self.lines.append(self.ax.axhline(start_y, linestyle='--', color='lightgreen'))
        self.lines.append(self.ax.axvline(end_x, linestyle='--', color='lightgreen'))
        self.lines.append(self.ax.axhline(end_y, linestyle='--', color='lightgreen'))

        plt.draw()

    def print_ellipse_coordinates(self):
        start_x, start_y = self.points[0]
        end_x, end_y = self.points[1]
        center_x = (start_x + end_x) / 2
        center_y = (start_y + end_y) / 2
        width = abs(end_x - start_x)
        height = abs(end_y - start_y)

        print("Ellipse Coordinates:")
        print(f"Point 1: ({round(start_x)}, {round(start_y)})")
        print(f"Point 2: ({round(end_x)}, {round(end_y)})")
        print(f"Center: ({round(center_x)}, {round(center_y)})")
        print(f"Width: {round(width)}")
        print(f"Height: {round(height)}")

    def show(self):
        plt.show()


drawer = EllipseDrawer()
drawer.show()
