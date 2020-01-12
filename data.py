import define as d
import matplotlib.pyplot as plt
import numpy as np

#Create Particles
p_list = d.generate_p_list(5)

def Energy_Total(p_list): #Find Total System Energy
    E_tot = 0
    for p in p_list:
        v = np.linalg.norm(np.array([p.vx, p.vy]))
        E_v = p.mass*v**2
        E_tot = E_tot+E_v
    return E_tot

def probab(listt): #List probabilities of each item in list to occur
    prob = []
    for l in listt:
        probi = listt.count(l)/len(listt)
        prob.append(probi)
    return prob

def plot(xl,yl,list1,list2): #Plot Graph
    plt.figure()
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.scatter(list1,list2)
    plt.plot(list1,list2)

def second_main_p():
    Energy_list = []
    t_list = []
    t = 10
    dt = 1
    ctime = 0
    for x in range(0, t, dt):
        t_list.append(x)
        Energy_list.append(Energy_Total(p_list))
        event_list = d.next_event(p_list, dt)
        d.iteration_g(p_list)
        prev_time = t
        t = t + event_list[0]
        if (event_list[0] < 100):
            event_list[1].collide_p(event_list[2])
        ctime = ctime + dt
    plot("t(s)","Energy(J)",t_list,Energy_list)
    plt.show()

#second_main_p()


