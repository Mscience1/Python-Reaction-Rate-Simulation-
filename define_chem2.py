from define import *

L = 100

color_dictionary = {
"white": (255, 255, 255),
"black": (0, 0, 0),
"red": (255, 0, 0),
"green": (0, 255, 0),
"blue": (0, 0, 255),
"gold": (255, 215, 0),
"navy": (0, 0, 128),
"orange": (255, 69, 0),
"yellow": (255,255,0),}

activation_energy = 8 #in J/mol
temp = 731 #In Kelvin
R = 8.314 #in J/mol * Kelvin
avo_const = 6.022*10**23
avrg_Ek = (3/2)*(R/avo_const) * temp #Average Kinetic Energy
mol_mass_Cl = 35.453 #g/mol
mol_mass_Br = 79.904 #g/mol
n_I = 8 #number of I molecules
n_H = 14 #number of H molecules
m_Br = (mol_mass_Br*n_I)/avo_const/n_I * 10**24#mass of single Br molecule; grams
m_Cl = (mol_mass_Cl*n_H)/avo_const/n_H * 10**24#mass of single Cl molecule; grams
velo_H = math.sqrt(2*avrg_Ek/m_Cl) #Velocity of hydrogen particle
velo_I = math.sqrt(2*avrg_Ek/m_Br) #Velocity of Iodine particle

class Cl_Particle(Particle):
    def __init__(self):
        id,mass,radius,x,y,vx,vy = 0,m_Cl,5,random.randint(-L + 1, L - 1),random.randint(-L + 1, L - 1),random.randrange(1,3),random.randrange(1,3)
        Particle.__init__(self,id,mass,radius,x,y,vx,vy)
        self.molecule = "Cl"
        self.energy = self.mass*np.linalg.norm(np.array([self.vx, self.vy]))**2
        self.colour = 'w'

    def if_col_react(self,other):
        if (self.molecule  == "Cl" and other.molecule == "Br_2"):
            c = self
            d = other
            c.collide_p_plastic(d)
            c_vec = np.linalg.norm(np.array([self.vx, self.vy]))
            d_vec = np.linalg.norm(np.array([other.vx, other.vy]))
            d_energy = d.mass * d_vec
            c_energy = c.mass * c_vec
            if (abs((c_energy + d_energy) - (self.energy + other.energy)) > activation_energy):
                return True

    def react(self):
        self.colour = 'm'
        self.mass = m_Cl+m_Br
        self.radius = 5
        self.molecule = "ClBr"


class Br_Particle(Particle):
    def __init__(self):
        id,mass, radius, x, y, vx, vy = 1,m_Br*2, 6, random.randint(-L + 1, L - 1),random.randint(-L + 1, L - 1), random.randrange(1,3),random.randrange(1,3)
        Particle.__init__(self, id, mass, radius, x, y, vx, vy)
        self.molecule = "Br_2"
        self.energy = self.mass * np.linalg.norm(np.array([self.vx, self.vy])) ** 2
        self.colour = 'b'

    def if_col_react(self,other):
        if (self.molecule  == "Br_2" and other.molecule == "Cl"):
            print("E:",self.energy+other.energy)
            c = self
            d = other
            c.collide_p_plastic(d)
            c_vec = np.linalg.norm(np.array([self.vx, self.vy]))
            d_vec = np.linalg.norm(np.array([other.vx, other.vy]))
            d_energy = d.mass*d_vec
            c_energy = c.mass*c_vec
            if((self.energy+other.energy)-(c_energy+d_energy) > activation_energy):
                return True

    def react(self):
        self.colour = 'm'
        self.mass = m_Br
        self.radius = 6
        self.molecule = "Br"

def h_list(n):
    oplist = []
    rando = 0
    for x in range(0, n):  # Generate n number of Chloride particles and put them in list of H_2 particles
        rando = rando + 1
        oplist.append(Cl_Particle())
    return oplist

def io_list(n):
    mplist = []
    rando = 0
    for x in range(0, n):  # Generate n number of Bromine particles and put them in list of I_2 particles
        rando = rando + 1
        mplist.append(Br_Particle())
    return mplist


