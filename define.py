import random
import math
import numpy as np

L = 100

class Particle:
    def __init__(self, id, mass, radius,x, y,vx,vy):
        self.id = id
        self.mass = mass
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.x_list = []
        self.y_list = []
        self.c_list = []

    def move(self):  # What to do during time when no event is occuring (such as collision)
        self.x = self.x + self.vx
        self.y = self.y + self.vy


    def collide_p_plastic(self, other):  # What/How to update after particle collision (Elastic Collision)
        prev_self_v_vec = np.array([self.vx, self.vy])
        prev_other_v_vec = np.array([other.vx, other.vy])

        v_vec = (self.mass*prev_self_v_vec + other.mass*prev_other_v_vec)/(self.mass+other.mass)

        self.vx = v_vec[0]
        self.vy = v_vec[1]
        other.vx = v_vec[0]
        other.vy = v_vec[1]
        #print("collision",self.vx,self.id)
        self.x = self.x+1
        self.y = self.y+1

    def collide_p_elastic(self,other):
        prev_self_v_vec = np.array([self.vx, self.vy])
        prev_other_v_vec = np.array([other.vx, other.vy])
        sum_mass = self.mass+other.mass
        self_velocity = ((self.mass-other.mass)/sum_mass)*prev_self_v_vec + (2*other.mass/sum_mass)*prev_other_v_vec
        other_velocity = ((2*self.mass)/sum_mass)*prev_self_v_vec + ((other.mass-self.mass)/sum_mass)*prev_other_v_vec
        self.vx = self_velocity[0]
        self.vy = self_velocity[1]
        other.vx = other_velocity[0]
        other.vy = other_velocity[1]

    def collide_w_x(self):  # What/How to update after wall collision (Reflection)
        self.vx = -self.vx

    def collide_w_y(self):
        self.vy = -self.vy


def if_wall_collision_x(particle):  # Find if wall collision occurred

    if (particle.x >= (L - 1) or particle.x <= (-1 * L + 1)):
        return True

    else:
        return False

def if_wall_collision_y(particle):  # Find if wall collision occurred

    if (particle.y >= (L - 1) or particle.y <= (-1 * L + 1)):
        return True

    else:
        return False


def if_particle_collision(particle1, particle2):  # Find if particle collision occurred
    dx = abs(particle2.x - particle1.x)
    dy = abs(particle2.y - particle1.y)
    dist = math.hypot(dx, dy)

    if (dist <= particle1.radius + particle2.radius+1):
        return True

    else:
        return False

def generate_p_list(n):  # How to generate particles in simulation, ID is 1-n
    p_list = []
    rando = 0
    for x in range(0, n):  # Generate n number of particles and put them in list of particles
        rando = rando + 1
        p_list.append(Particle(rando, 1,7 ,random.randint(-L + 1, L - 1),random.randint(-L + 1, L - 1),1,1))
    return p_list



def next_event(p_list,dt):
    event_list = [1000, 1, 2]
    for x in p_list:  # For every particle,
        for y in p_list:  # Find next collision with all other particles
            if (x != y):  # If particle is not itself

                t = 0  # Set time to zero

                if (if_particle_collision(x, y) == True):
                    pass

                else:

                    c = x  # Make copy of x particle
                    d = y  # Make copy of y particle
                    bool = if_particle_collision(c,d)
                    while (bool == False):  # Until Particle copies collide, keep moving particle pair until collision

                        bool = if_particle_collision(c,d)

                        if(t>=99):
                            bool = True

                        if (if_wall_collision_x(c)):
                            c.collide_w_x()

                        if(if_wall_collision_y(c)):
                            c.collide_w_y()

                        if(if_wall_collision_x(d)):
                            d.collide_w_x()

                        if(if_wall_collision_y(d)):
                            d.collide_w_y()

                        c.move()  # Move C Particle
                        d.move()  # Mode D Particle
                        t += dt  # Add 1 to total time

                        #print(t, math.hypot(d.x-c.x,d.y-c.y), c.id, d.id)  # For Debug

                    if (t < event_list[0]):  # Set time of next event (and info such as particles in event)
                        #print(event_list)
                        #print("change", t)  # For Debug
                        #print(c.position, d.position, c.id, d.id)  # For Debug
                        event_list[0] = t
                        event_list[1] = x
                        event_list[2] = y

    return event_list

def create_particle_graphics(p_list):
    gph_list = [] #create list of graphical objects for order in p_list
    for i in range(0,len(p_list)):
        gph_list.append(turtle.Turtle())
        gph_list[i].color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        gph_list[i].shape("circle")
        gph_list[i].shapesize(0.5)
        gph_list[i].penup()
    #gph_list[0].pendown()
    return gph_list

def create_particle_graphics_chem(p_list):
    gph_list = [] #create list of graphical objects for order in p_list
    for i in range(0,len(p_list)):
        gph_list.append(turtle.Turtle())
        gph_list[i].color(p_list[i].colour)
        gph_list[i].shape("circle")
        gph_list[i].shapesize(0.5)
        gph_list[i].penup()
    #gph_list[0].pendown()
    return gph_list

def iteration(p_list,gph_list):
    for particle in p_list:

        i = p_list.index(particle)

        gph_list[i].color(particle.colour)

        particle.move()  # Calculate New Position

        gph_list[i].speed(math.sqrt(particle.vx**2+particle.vy**2))  #Change speed to new speed
        gph_list[i].goto(particle.x, particle.y) #Move Particles on Screen


        if(if_wall_collision_y(particle)):
            particle.collide_w_y()

        if(if_wall_collision_x(particle)):
            particle.collide_w_x()

def iteration_g(p_list):
    for particle in p_list:

        particle.move()  # Calculate New Position
        particle.x_list.append(particle.x)
        particle.y_list.append(particle.y)
        particle.c_list.append(particle.colour)

        if(if_wall_collision_y(particle)):
            particle.collide_w_y()

        if(if_wall_collision_x(particle)):
            particle.collide_w_x()
