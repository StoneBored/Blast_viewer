from tkinter import *
import tkinter as Tk
from tkinter import ttk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import re
from matplotlib.colors import LogNorm
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)



def main():

    root = Tk.Tk()
    gui = Window(root)
    gui.root.mainloop()

    return None
class Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Ground Vibration Estimation")
        self.root.geometry('1450x500')

        # FRAMES

        parameters_frame =LabelFrame(self.root, text="Blast parameters", padx=20,pady=20)
        parameters_frame.place(x = 40, y = 1)
        self.parameters_frame = parameters_frame

        receiver_frame = LabelFrame(self.root,text="Receiver parameters", padx=20,pady=20)
        receiver_frame.place(x = 40, y = 330)
        self.receiver_frame = receiver_frame

        sources_frame = LabelFrame(self.root,text="Blast coordinates", padx=1,pady=1)
        sources_frame.place(x = 35, y = 200)
        self.sources_frame = sources_frame

        graph_frame =LabelFrame(self.root, text="")
        graph_frame.place(x = 300, y = 1)
        self.graph_frame = graph_frame

        map_frame =LabelFrame(self.root, text="")
        map_frame.place(x = 870, y = 1)
        self.map_frame = map_frame


        # INITAL DATA
        
        self.distance = 100
        self.kasite = 1140
        self.asite = -1.6

        self.receivor1_x = 10
        self.receivor1_y = -10

        self.receivor2_x = 25
        self.receivor2_y = -25

        self.receivor3_x = 50
        self.receivor3_y = -50

        self.receivor4_x = 70
        self.receivor4_y = -70
        
        self.receivor5_x = 80
        self.receivor5_y = -80
        
        self.charge_PX_1 = -50
        self.charge_PY_1 = 50
        self.charge_C_1 = 100

        self.charge_PX_2 = -50
        self.charge_PY_2 = -50
        self.charge_C_2 = 100

        self.charge_PX_3 = 0
        self.charge_PY_3 = 0
        self.charge_C_3 = 0

        self.charge_PX_4 = 0
        self.charge_PY_4 = 0
        self.charge_C_4 = 0

        self.charge_PX_5 = 0
        self.charge_PY_5 = 0
        self.charge_C_5 = 0


        # ------------------------------------------------------------------------------------------------
        # RESTRICTING ENTRYS TO INTEGERTS AND FLOATS ONLY
        def correct_1(v,inp):

            pattern = re.compile(r'^(\d*\-?\d*\d*\.?\d*)$')
            if pattern.match(inp) is not None:
                return True
            elif inp is "":
                return True
            else:
                return False

        def correct_2(v,inp):

            pattern = re.compile(r'^(\d*)$')
            if pattern.match(inp) is not None:
                return True
            elif inp is "":
                return True
            else:
                return False

        reg_1 = root.register(correct_1)
        reg_2 = root.register(correct_2)
        # ------------------------------------------------------------------------------------------------
    
        # LABELS AND ENTRYS PARAMETERS
        # CHARGES

        Label(sources_frame, text = "     X     :").grid(row=1, column=0)
        Label(sources_frame, text = "     Y     :").grid(row=2, column=0)
        Label(sources_frame, text = "Charge kg  :").grid(row=3, column=0)

        Label(sources_frame, text = "P1").grid(row=0, column=1)
        self.charge_entry_PX_1 = Entry(sources_frame,  width = 5)
        self.charge_entry_PY_1 = Entry(sources_frame,  width = 5)
        self.charge_entry_C_1 = Entry(sources_frame,  width = 5)
        self.charge_entry_PX_1.grid(row=1, column=1)
        self.charge_entry_PY_1.grid(row=2, column=1)
        self.charge_entry_C_1.grid(row=3, column=1)
        self.charge_entry_PX_1.insert(0, -50)
        self.charge_entry_PY_1.insert(0, 50)
        self.charge_entry_C_1.insert(0, 100)
        self.charge_entry_PX_1.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.charge_entry_PY_1.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.charge_entry_C_1.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        Label(sources_frame, text = "P2").grid(row=0, column=2)
        self.charge_entry_PX_2 = Entry(sources_frame,  width = 5)
        self.charge_entry_PY_2 = Entry(sources_frame,  width = 5)
        self.charge_entry_C_2 = Entry(sources_frame,  width = 5)
        self.charge_entry_PX_2.grid(row=1, column=2)
        self.charge_entry_PY_2.grid(row=2, column=2)
        self.charge_entry_C_2.grid(row=3, column=2)
        self.charge_entry_PX_2.insert(0, -50)
        self.charge_entry_PY_2.insert(0, -50)
        self.charge_entry_C_2.insert(0, 100)
        self.charge_entry_PX_2.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.charge_entry_PY_2.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.charge_entry_C_2.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        Label(sources_frame, text = "P3").grid(row=0, column=3)
        self.charge_entry_PX_3 = Entry(sources_frame,  width = 5)
        self.charge_entry_PY_3 = Entry(sources_frame,  width = 5)
        self.charge_entry_C_3 = Entry(sources_frame,  width = 5)
        self.charge_entry_PX_3.grid(row=1, column=3)
        self.charge_entry_PY_3.grid(row=2, column=3)
        self.charge_entry_C_3.grid(row=3, column=3)
        self.charge_entry_PX_3.insert(0, 0)
        self.charge_entry_PY_3.insert(0, 0)
        self.charge_entry_C_3.insert(0, 0)
        self.charge_entry_PX_3.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.charge_entry_PY_3.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.charge_entry_C_3.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        Label(sources_frame, text = "P4").grid(row=0, column=4)
        self.charge_entry_PX_4 = Entry(sources_frame,  width = 5)
        self.charge_entry_PY_4 = Entry(sources_frame,  width = 5)
        self.charge_entry_C_4 = Entry(sources_frame,  width = 5)
        self.charge_entry_PX_4.grid(row=1, column=4)
        self.charge_entry_PY_4.grid(row=2, column=4)
        self.charge_entry_C_4.grid(row=3, column=4)
        self.charge_entry_PX_4.insert(0, 0)
        self.charge_entry_PY_4.insert(0, 0)
        self.charge_entry_C_4.insert(0, 0)
        self.charge_entry_PX_4.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.charge_entry_PY_4.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.charge_entry_C_4.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        Label(sources_frame, text = "P5").grid(row=0, column=5)
        self.charge_entry_PX_5 = Entry(sources_frame,  width = 5)
        self.charge_entry_PY_5 = Entry(sources_frame,  width = 5)
        self.charge_entry_C_5 = Entry(sources_frame,  width = 5)
        self.charge_entry_PX_5.grid(row=1, column=5)
        self.charge_entry_PY_5.grid(row=2, column=5)
        self.charge_entry_C_5.grid(row=3, column=5)
        self.charge_entry_PX_5.insert(0, 0)
        self.charge_entry_PY_5.insert(0, 0)
        self.charge_entry_C_5.insert(0, 0)
        self.charge_entry_PX_5.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.charge_entry_PY_5.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.charge_entry_C_5.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        distance = Label(self.parameters_frame ,  text = "Distance (m)")
        self.distance_entry = Entry(self.parameters_frame ,  width = 15)
        self.distance_entry.grid(row=1, column=1)
        distance.grid(row=1, column=0)
        self.distance_entry.insert(0,100)
        self.distance_entry.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        kasite = Label(self.parameters_frame ,  text = "Site constant (Kg)")
        self.kasite_entry = Entry(self.parameters_frame ,  width = 15)
        self.kasite_entry.grid(row=2, column=1)
        kasite.grid(row=2, column=0)
        self.kasite_entry.insert(0,1140)
        self.kasite_entry.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        asite = Label(parameters_frame ,  text = "Site exponent (b)")
        self.asite_entry = Entry(self.parameters_frame ,  width = 15)
        self.asite_entry.grid(row=3, column=1)
        asite.grid(row=3, column=0)
        self.asite_entry.insert(0,-1.6)
        self.asite_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        # RECEIVER LABEL AND ENTRYS
        Label(receiver_frame, text = "X :").grid(row=1, column=0)
        Label(receiver_frame, text = "Y :").grid(row=2, column=0)

        Label(receiver_frame, text = "R1").grid(row=0, column=1)
        self.receivor1_x_entry = Entry(receiver_frame,  width = 5)
        self.receivor1_y_entry = Entry(receiver_frame,  width = 5)
        self.receivor1_x_entry.grid(row=1, column=1)
        self.receivor1_y_entry.grid(row=2, column=1)
        self.receivor1_x_entry.insert(0, 10)
        self.receivor1_y_entry.insert(0, -10)
        self.receivor1_x_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.receivor1_y_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        Label(receiver_frame, text = "R2").grid(row=0, column=2)
        self.receivor2_x_entry = Entry(receiver_frame,  width = 5)
        self.receivor2_y_entry = Entry(receiver_frame,  width = 5)
        self.receivor2_x_entry.grid(row=1, column=2)
        self.receivor2_y_entry.grid(row=2, column=2)
        self.receivor2_x_entry.insert(0, 25)
        self.receivor2_y_entry.insert(0, -25)
        self.receivor2_x_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.receivor2_y_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))


        Label(receiver_frame, text = "R3").grid(row=0, column=3)
        self.receivor3_x_entry = Entry(receiver_frame,  width = 5)
        self.receivor3_y_entry = Entry(receiver_frame,  width = 5)
        self.receivor3_x_entry.grid(row=1, column=3)
        self.receivor3_y_entry.grid(row=2, column=3)
        self.receivor3_x_entry.insert(0, 50)
        self.receivor3_y_entry.insert(0, -50)
        self.receivor3_x_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.receivor3_y_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        Label(receiver_frame, text = "R4").grid(row=0, column=4)
        self.receivor4_x_entry = Entry(receiver_frame,  width = 5)
        self.receivor4_y_entry = Entry(receiver_frame,  width = 5)
        self.receivor4_x_entry.grid(row=1, column=4)
        self.receivor4_y_entry.grid(row=2, column=4)
        self.receivor4_x_entry.insert(0, 70)
        self.receivor4_y_entry.insert(0, -70)
        self.receivor4_x_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.receivor4_y_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        Label(receiver_frame, text = "R5").grid(row=0, column=5)
        self.receivor5_x_entry = Entry(receiver_frame,  width = 5)
        self.receivor5_y_entry = Entry(receiver_frame,  width = 5)
        self.receivor5_x_entry.grid(row=1, column=5)
        self.receivor5_y_entry.grid(row=2, column=5)
        self.receivor5_x_entry.insert(0, 80)
        self.receivor5_y_entry.insert(0, -80)
        self.receivor5_x_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.receivor5_y_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        # RADIOBUTTONS AND RESULTS FRAME, IT SHOULD BE TOGETHER

        self.var = StringVar(value="dBV")
        c_pascal = Radiobutton(parameters_frame, text="PPV", variable=self.var, value = "PPV")
        c_pascal.grid(row=5, column=0)
        c_dbl = Radiobutton(parameters_frame, text="dBV", variable=self.var, value = "dBV")
        c_dbl.grid(row=5, column=1)
        self.var1 = self.var.get()

        # BUTTON AND COMMANDS
        button1 = Button(self.parameters_frame, text = "Calculate",command = self.update_values)
        parameters_frame.bind("<Return>", self.update_values)
        button1.grid(row=6, column=1)



        self.test_1()
        frame_1=Frame(self.graph_frame)
        frame_1.pack()
        self.frame_1=frame_1
        chart_1 = FigureCanvasTkAgg(self.figure1,self.frame_1)
        chart_1.get_tk_widget().pack()
        self.chart_1 =chart_1
        toolbar_1 = NavigationToolbar2Tk(chart_1,self.frame_1)
        toolbar_1.update()
        chart_1.get_tk_widget().pack()

        self.test_1()
        frame_2=Frame(self.map_frame)
        frame_2.pack()
        self.frame_2=frame_2
        chart_2 = FigureCanvasTkAgg(self.figure2,self.frame_2)
        chart_2.get_tk_widget().pack()
        self.chart_2 =chart_2
        toolbar_2 = NavigationToolbar2Tk(chart_2,self.frame_2)
        toolbar_2.update()
        chart_2.get_tk_widget().pack()

    #  GENERAL COMMAND FOR BUTTON
    def update_values(self, event=None):

        self.distance = int(self.distance_entry.get())
        self.kasite = int(self.kasite_entry.get())
        self.asite = float(self.asite_entry.get())

        self.receivor1_x = int(self.receivor1_x_entry.get())
        self.receivor1_y = int(self.receivor1_y_entry.get())
        

        self.receivor2_x = int(self.receivor2_x_entry.get())
        self.receivor2_y = int(self.receivor2_y_entry.get())

        self.receivor3_x = int(self.receivor3_x_entry.get())
        self.receivor3_y = int(self.receivor3_y_entry.get())

        self.receivor4_x = int(self.receivor4_x_entry.get())
        self.receivor4_y = int(self.receivor4_y_entry.get())

        self.receivor5_x = int(self.receivor5_x_entry.get())
        self.receivor5_y = int(self.receivor5_y_entry.get())

        self.charge_PX_1 = int(self.charge_entry_PX_1.get())
        self.charge_PY_1 = int(self.charge_entry_PY_1.get())
        self.charge_C_1 = int(self.charge_entry_C_1.get())

        self.charge_PX_2 = int(self.charge_entry_PX_2.get())
        self.charge_PY_2 = int(self.charge_entry_PY_2.get())
        self.charge_C_2 = int(self.charge_entry_C_2.get())

        self.charge_PX_3 = int(self.charge_entry_PX_3.get())
        self.charge_PY_3 = int(self.charge_entry_PY_3.get())
        self.charge_C_3 = int(self.charge_entry_C_3.get())

        self.charge_PX_4 = int(self.charge_entry_PX_4.get())
        self.charge_PY_4 = int(self.charge_entry_PY_4.get())
        self.charge_C_4 = int(self.charge_entry_C_4.get())

        self.charge_PX_5 = int(self.charge_entry_PX_5.get())
        self.charge_PY_5 = int(self.charge_entry_PY_5.get())
        self.charge_C_5 = int(self.charge_entry_C_5.get())

        
        
        self.var1 = self.var.get()
        self.plot_values_1()
        self.plot_values_2()
        return None


    # FUNCTION FOR MAP IN DBL AND PA
    def test_1(self):


        r1 = [self.receivor1_x, self.receivor1_y]
        r2 = [self.receivor2_x, self.receivor2_y]
        r3 = [self.receivor3_x, self.receivor3_y]
        r4 = [self.receivor4_x, self.receivor4_y]
        r5 = [self.receivor5_x, self.receivor5_y]

        r_postions = [r1, r2, r3, r4, r5]

        # GRAPH

        N = self.distance
        x = np.linspace(-N, N, 500)
        y = np.linspace(-N, N, 500)
        X,Y = np.meshgrid(x,y)

        # CENTER POINT
        p1 = [self.charge_PX_1 ,self.charge_PY_1, self.charge_C_1]
        p2 = [self.charge_PX_2 ,self.charge_PY_2, self.charge_C_2]
        p3 = [self.charge_PX_3 ,self.charge_PY_3, self.charge_C_3]
        p4 = [self.charge_PX_4 ,self.charge_PY_4, self.charge_C_4]
        p5 = [self.charge_PX_5 ,self.charge_PY_5, self.charge_C_5]

        p_charge = [p1, p2, p3, p4, p5]
        
        # DISTANCE
        # R = np.sqrt((((p[0]-X)**2)+((p[1]-Y)**2)))


        if (self.var1 == "dBV"):
        # EQUATION
    
            
            z_log = 0
            for px, py, charge in p_charge:
                r = np.sqrt((((px-X)**2)+((py-Y)**2)))
                z = 10 * np.log10((((( r / (charge**(1 / 2)) )**self.asite) * self.kasite)/(0.000001))**2)
                z_log += 10**(z/10)
            z_total = 10*np.log10(z_log)

            Z= np.array(z_total).reshape(len(y),len(x))
            # z1 = [10 * np.log10(((((i/(10**(1/2)))**self.asite) * self.kasite)/(0.000001))**2) for i in np.arange(0.1, (N+1)*np.sqrt(2))]
            figure2 = plt.figure(figsize = (5,4), dpi = 110)
            self.figure2 = figure2
            noisemap = figure2.add_subplot(111)

            c = noisemap.contourf(X,Y,Z,levels=np.round(np.linspace(z_total.min(),z_total.max(),26),1),cmap=cm.jet)
            figure2.colorbar(c,ax=noisemap).ax.set_title('dBV')
            levls = np.array([140,148,160])

            cs_1 = noisemap.contour(X,Y,Z,levels = levls,colors='k',linestyles=('-','-.','--'))
            plt.plot(levls[0],'k-',label="140 dBV")
            plt.plot( levls[1],'k-.',label="148 dBV")
            plt.plot( levls[2],'k--',label="160 dBV")
           

        elif (self.var1 == "PPV"):

            z_log = 0
            for px, py, charge in p_charge:
                r = np.sqrt((((px-X)**2)+((py-Y)**2)))
                z = 10 * np.log10(((((( r / (charge**(1 / 2)) )**self.asite) * self.kasite)/(0.000001))**2))
                z_log += 10**(z/10)
                z_suma = 10*np.log10(z_log)
            z_total = 0.000001 * 10**(z_suma/20)

            Z= np.array(z_total).reshape(len(y),len(x))
            # z_pascal = [(( i / (self.charge_C_1**(1 / 3)) )**-1.45) * 516 for i in np.arange(0.5,(self.distance +1)*np.sqrt(2)) ]
            florr = np.log10(z_total.min())
            florr_1 = np.floor(florr)
            florr2 = np.log10(z_total.max())
            florr_2 = np.ceil(florr2)
            rango = np.arange(florr_1 , florr_2)
            levs_1 = [10**n for n in np.arange(florr_1, florr_2)]
            levs_2 = [2*10**n for n in np.arange(florr_1 , florr_2)]
            levs_3 = [3*10**n for n in np.arange(florr_1 , florr_2)]
            levs_4 = [5*10**n for n in np.arange(florr_1 , florr_2)]
            levs_5 = [8*10**n for n in np.arange(florr_1 , florr_2-1)]

            levs_total = sorted(levs_1 + levs_2 + levs_3 + levs_4 + levs_5)
            lvl = levs_total
            levls = np.array([10,25,100])
            figure2 = plt.figure(figsize = (5,4), dpi = 110)
            self.figure2 = figure2
            noisemap = figure2.add_subplot(111)
            c = noisemap.contourf(X,Y,Z,levels=lvl,norm=LogNorm(),cmap=cm.jet)
            cs_1 = noisemap.contour(X,Y,Z,levels = levls,colors='k',linestyles=('-','-.','--'))
            figure2.colorbar(c,ax=noisemap,ticks=[1, 10, 100, 1000, 10000]).ax.set_title('PPV')
            plt.plot(levls[0],'k-',label="10 PPV")
            plt.plot( levls[1],'k-.',label="25 PPV")
            plt.plot( levls[2],'k--',label="100 PPV")

            
        fontP = FontProperties()
        fontP.set_size('x-small')
        plt.legend(loc='upper right', prop=fontP)
        plt.xlabel('Distance (m)')
        plt.ylabel('Distance (m)',labelpad=0)
        plt.title('Vibration Map')


        Xflat, Yflat, Zflat = X.flatten(), Y.flatten(), Z.flatten()
        def fmt(x, y):
    # get closest point with known data
            dist = np.linalg.norm(np.vstack([Xflat - x, Yflat - y]), axis=0)
            idx = np.argmin(dist)
            z = Zflat[idx]
            return 'x={x:.5f}  y={y:.5f}  z={z:.5f}'.format(x=x, y=y, z=z)
       

        plt.gca().format_coord = fmt

        plt.scatter(r1[0], r1[1],c='w')
        plt.scatter(r2[0], r2[1],c='w')
        plt.scatter(r3[0], r3[1],c='w')
        plt.scatter(r4[0], r4[1],c='w')
        plt.scatter(r5[0], r5[1],c='w')



        annotations=["R1","R2","R3","R4","R5"]
        r_x = [r1[0], r2[0], r3[0], r4[0], r5[0]]
        r_y = [r1[1], r2[1], r3[1], r4[1], r5[1]]
    
        for i, label in enumerate(annotations):
            plt.annotate(label, (r_x[i], r_y[i]))

        plt.xlim(-N,N)
        plt.ylim(-N,N)
        plt.tick_params(axis='x', labelsize=8)
        plt.tick_params(axis='y', labelsize=8)
        plt.grid(True, which="both", ls="-")


        Xflat, Yflat, Zflat = X.flatten(), Y.flatten(), Z.flatten()
        z_values = []
        # if 
        for x, y in r_postions:
            dist = np.linalg.norm(np.vstack([Xflat - x, Yflat - y]), axis=0)
            idx = np.argmin(dist)
            z = Zflat[idx]
            z_values.append(z)
      
        figure1 = plt.figure(figsize = (5,4), dpi = 110)
        barras = figure1.add_subplot(111)
        self.figure1=figure1

        langs = ['R1', 'R2', 'R3', 'R4', 'R5']
        bars = barras.bar(langs,z_values)
        plt.grid(True, which="both", ls="-")
        
        plt.ylabel('Distance (m)',labelpad=0)
        plt.title('Receivers Levels')
        plt.tick_params(axis='x', labelsize=8)
        plt.tick_params(axis='y', labelsize=8)

        for value in bars:
            height = value.get_height()
            plt.text(value.get_x() + value.get_width()/2.,
                    1.002*height,'%d' % float(height), ha='center', va='bottom')
        
        if (self.var1 == "dBV"):
            plt.ylim(z_total.min()/1.1 , max(z_values)*1.25)
            plt.ylabel('Vibration Level (dBV)')
            x1 = [0, 1, 2, 3, 4 ]
            curve_1 = [140, 140, 140, 140, 140]
            curve_2 = [148, 148, 148, 148, 148]
            curve_3 = [160, 160, 160, 160, 160]
            plt.plot(x1, curve_1,'b--',label="160 dBV: Maximum for Structural Damage Level" )
            plt.plot(x1, curve_2,'r--',label="148 dBV: Maximum for Human Comfort Level" )
            plt.plot(x1, curve_3,'g--',label="140 dBV: Annoying")
            fontP = FontProperties()
            fontP.set_size('x-small')
            plt.legend(loc='upper right', prop=fontP)
           
          
        elif (self.var1 == 'PPV'):
            plt.yscale('log')
            plt.ylabel('Peak Particle Velocity (mm / s)',labelpad=0)
            plt.ylim(z_total.min()/10 , max(z_values)*100)
            x1 = [0, 1, 2, 3, 4, ]
            curve_1 = [100, 100, 100, 100, 100]
            curve_2 = [25, 25, 25, 25, 25]
            curve_3 = [10, 10, 10, 10, 10]
            plt.plot(x1, curve_1,'b--',label="100 mm/s: Maximum for Structural Damage Level" )
            plt.plot(x1, curve_2,'r--',label="25 mm/s: Maximum for Human Comfort Level" )
            plt.plot(x1, curve_3,'g--',label="10 mm/s: Annoying")
            fontP = FontProperties()
            fontP.set_size('x-small')
            plt.legend(loc='upper right', prop=fontP)
    
    # # FUNCTION FOR PLOT THE GRAPH VALUES
    def plot_values_1(self):
        self.test_1()
        self.frame_1.destroy()
        frame_1=Frame(self.graph_frame)
        frame_1.pack()
        self.frame_1=frame_1
        chart_1 = FigureCanvasTkAgg(self.figure1,self.frame_1)
        chart_1.get_tk_widget().pack()
        toolbar_1 = NavigationToolbar2Tk(chart_1,self.frame_1)
        toolbar_1.update()
        # chart._tkcanvas()
        chart_1.get_tk_widget().pack()
        return None
    
    #  FUNCTION FOR PLOT THE MAP VALUES
    def plot_values_2(self):
        self.test_1()
        self.frame_2.destroy()
        frame_2=Frame(self.map_frame)
        frame_2.pack()
        self.frame_2=frame_2
        chart_2 = FigureCanvasTkAgg(self.figure2,self.frame_2)
        chart_2.get_tk_widget().pack()
        toolbar_2 = NavigationToolbar2Tk(chart_2,self.frame_2)
        toolbar_2.update()
        chart_2.get_tk_widget().pack()
        return None

   
    pass
main()