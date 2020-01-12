from define_chem2 import *
from data import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#Create Particles
o_list = h_list(5)
m_list = io_list(5)
p_list =o_list+m_list
x_positions = []
y_positions = []
col = []

def main_d():
    t_list = []
    rel = []
    t = 3000
    dt = 1
    ctime = 0
    for x in range(0, t, dt):
        print(t)
        t_list.append(x)
        event_list = d.next_event(p_list, dt)
        d.iteration_g(p_list)
        prev_time = t
        t = t + event_list[0]
        if (event_list[0] < 100):
            if (event_list[1].if_col_react(event_list[2]) == True):
                event_list[1].react()
                event_list[2].react()
            event_list[1].collide_p_plastic(event_list[2])
        ctime = ctime + dt

main_d()
for p in p_list:
    x_positions.append(p.x_list)
    y_positions.append(p.y_list)
    col.append(p.c_list)

print(col)

def current_positions_x(x_positions,i):
    x_current = []
    for x in range(0,len(x_positions)):
        x_current.append(x_positions[x][i])
    return x_current

def current_positions_y(y_positions,i):
    y_current = []
    for x in range(0,len(y_positions)):
        y_current.append(y_positions[x][i])
    return y_current

def current_colour(col,i):
    color_current = []
    for x in range(0,len(col)):
        color_current.append(col[x][i])
    return color_current

#print(current_positions_x(x_positions,1))

#Graphic


# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(1, 1))
plt.xlim(-100,100)
plt.ylim(-100,100)

plt.scatter(current_positions_x(x_positions,1), current_positions_y(y_positions,1), #x,y
                  s=100, lw=0.5)

def update(i):
        plt.clf()
        plt.xlim(-150, 150)
        plt.ylim(-150, 150)
        ax = plt.gca()
        rect = plt.Rectangle((-100, -100), 202, 202, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        plt.scatter(current_positions_x(x_positions,i), current_positions_y(y_positions,i), #x,y,color
                  s=100, lw=0.5,c = current_colour(col,i))

animation = FuncAnimation(fig, update, interval=10)

plt.show()
