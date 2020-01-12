from define_chem2 import *
from data import *
import seaborn as sns
from xlwt import Workbook

#Create Particles
o_list = h_list(20)
m_list = io_list(70)
p_list =o_list+m_list

def molecule_id_numbers(p_lis):
    reacted = []
    not_reacted = []
    for p in p_lis:
        if(p.molecule == "ClBr"):
            reacted.append(p)
        else:
            not_reacted.append(p)
    return len(reacted)

def molecule_concen(p_lis):
    def molecule_id_numbers(p_lis):
        reacted = []
        not_reacted = []
        for p in p_lis:
            if (p.molecule == "ClBr"):
                reacted.append(p)
            else:
                not_reacted.append(p)
        return (len(reacted)*10000)/(100**3*(6.022*10**23))

def molecule_concen_Cl(p_lis):
    def molecule_id_numbers(p_lis):
        reacted = []
        not_reacted = []
        for p in p_lis:
            if (p.molecule == "Cl"):
                reacted.append(p)
            else:
                not_reacted.append(p)
        return (len(reacted)*10000)/(100**3*(6.022*10**23))

def molecule_concen_Br(p_lis):
    def molecule_id_numbers(p_lis):
        reacted = []
        not_reacted = []
        for p in p_lis:
            if (p.molecule == "Br"):
                reacted.append(p)
            else:
                not_reacted.append(p)
        return (len(reacted)*10000)/(100**3*(6.022*10**23))

def Cl_id_numbers(p_lis):
    reacted = []
    not_reacted = []
    for p in p_lis:
        if (p.molecule == "Cl"):
            reacted.append(p)
        else:
            not_reacted.append(p)
    return len(reacted)

def Br_id_numbers(p_lis):
    reacted = []
    not_reacted = []
    for p in p_lis:
        if (p.molecule == "Br"):
            reacted.append(p)
        else:
            not_reacted.append(p)
    return len(reacted)

def third_main_p():
    t_list = []
    Energy_list = []
    rel = []
    h_2 = []
    i_2 = []
    conc = []
    concH = []
    concI = []
    ep = []
    tpo = []
    epi = []
    epn = []
    t = 200
    dt = 1
    ctime = 0
    for x in range(0, t, dt):
        print(t)
        t_list.append(x)
        Energy_list.append(Energy_Total(p_list))
        rel.append(molecule_id_numbers(p_list))
        h_2.append(Cl_id_numbers(p_list))
        i_2.append(Br_id_numbers(p_list))
        conc.append(molecule_concen(p_list))
        concH.append(molecule_concen_Cl(p_list))
        concI.append(molecule_concen_Br(p_list))
        event_list = d.next_event(p_list, dt)
        for k in range(0,event_list[0]):
            d.iteration_g(p_list)
        prev_time = t
        t = t + event_list[0]
        if (event_list[0] < 100):
            if (event_list[1].if_col_react(event_list[2]) == True):
                event_list[1].react()
                event_list[2].react()
                event_list[1].collide_p_plastic(event_list[2])
                event_list[2].collide_p_plastic(event_list[1])
                ep.append(Cl_id_numbers(p_list))
                tpo.append(x)
                epi.append(molecule_id_numbers(p_list))
                epn.append(Energy_Total(p_list))
            else:
                event_list[1].collide_p_elastic(event_list[2])
                event_list[2].collide_p_elastic(event_list[1])

        ctime = ctime + dt
    plot("t(s)", "N(reacted) - ClBr", t_list, rel)
    plot("t(s)", "Energy(J)", t_list, Energy_list)
    plot("t(s)","Cl",t_list,h_2)
    plot("t(s)", "Br_2", t_list, i_2)
    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')
    for some in range(0,len(tpo)):
        sheet1.write(some,0,tpo[some])
    for boopy in range(0,len(ep)):
        sheet1.write(boopy,1,ep[boopy])
    for gazoom in range(0,len(epi)):
        sheet1.write(gazoom,2,epi[gazoom])
    for zork in range(0,len(epn)):
        sheet1.write(zork,3,epn[zork])

    wb.save('xlwt Run1NEW.xls')

third_main_p()


v = []
s = []

for p in p_list:
    v.append(np.linalg.norm(np.array([p.vx, p.vy])))
    s.append(abs(np.linalg.norm(np.array([p.vx, p.vy]))))


plt.figure()
plt.xlabel("v(m/s)")
plt.ylabel("Prob")
sns.distplot(v)

plt.figure()
plt.xlabel("Speed")
plt.ylabel("Prob")
sns.distplot(s)

plt.show()
