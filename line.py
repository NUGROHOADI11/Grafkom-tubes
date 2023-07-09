# --------------------------------------------------------------------------------------------------
# generate line mouse input
# --------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

x_values = []
y_values = []

fig, ax = plt.subplots()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("User Input Line Plot")
ax.grid(True)

def onclick(event):
    # limit 2 input
    if len(x_values) >= 2:
        return

    x = event.xdata
    y = event.ydata
    x_values.append(x)
    y_values.append(y)
    ax.plot(x, y, 'ro')
    
    if len(x_values) == 2:
        ax.plot(x_values, y_values, 'b-')
    
    plt.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.xlim(0, 10)  
plt.ylim(0, 10)  
plt.show()

print("Data Points:")
for i in range(len(x_values)):
    print(f"Data Point {i+1}: ({x_values[i]}, {y_values[i]})")
