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
plt.rcParams['savefig.dpi'] = 1200




def main():

    root = Tk.Tk()
    gui = Window(root)
    gui.root.mainloop()

    return None

class Window:

    def __init__(self,root):

        self.root = root
        self.root.title("Overpressure Estimation")
        self.root.geometry('1450x500')
        # self.root.resizable(width=False, height=False)
        # self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0, weight=1)

        # FRAMES

        parameters_frame =LabelFrame(self.root, text="Blast parameters", padx=20,pady=20)
        parameters_frame.place(x = 40, y = 1)
        self.parameters_frame = parameters_frame

        receiver_frame = LabelFrame(self.root,text="Receiver coordinates", padx=20,pady=20)
        receiver_frame.place(x = 40, y = 200)
        self.receiver_frame = receiver_frame

        result_frame = LabelFrame(self.root,text="Results", padx=1,pady=1)
        result_frame.place(x = 10, y = 330)
        self.result_frame = result_frame

        graph_frame =LabelFrame(self.root, text="")
        graph_frame.place(x = 300, y = 1)
        self.graph_frame = graph_frame

        map_frame =LabelFrame(self.root, text="")
        map_frame.place(x = 870, y = 1)
        self.map_frame = map_frame


        # INITAL DATA
        self.charge = 5
        self.distance = 200
        self.kasite = 516
        self.asite = -1.45

        self.receivor1_x = 50
        self.receivor1_y = 0

        self.receivor2_x = 0
        self.receivor2_y = 0

        self.receivor3_x = 0
        self.receivor3_y = 0

        self.receivor4_x = 0
        self.receivor4_y = 0
        
        self.receivor5_x = 0
        self.receivor5_y = 0

        self.r = [0,0,0,0,0]
        self.total_level = [0,0,0,0,0]

        # ------------------------------------------------------------------------------------------------
        # RESTRICTING ENTRYS TO INTEGERTS AND FLOATS ONLY
        def correct_1(v,inp):

            pattern = re.compile(r'^(\d*\-?\d*\d*\.?\d*)$')
            if pattern.match(inp) is not None:
                return True
            elif inp == "":
                return True
            else:
                return False

        def correct_2(v,inp):

            pattern = re.compile(r'^(\d*)$')
            if pattern.match(inp) is not None:
                return True
            elif inp == "":
                return True
            else:
                return False

        reg_1 = root.register(correct_1)
        reg_2 = root.register(correct_2)
        # ------------------------------------------------------------------------------------------------
    
        # LABELS AND ENTRYS PARAMETERS
        charge = Label(self.parameters_frame ,  text = "Charge Q (Kg)")
        self.charge_entry = Entry(self.parameters_frame ,  width = 15)
        self.charge_entry.grid(row=0, column=1)
        self.charge_entry.insert(0,5)
        charge.grid(row=0, column=0)
        self.charge_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        distance = Label(self.parameters_frame ,  text = "Distance (m)")
        self.distance_entry = Entry(self.parameters_frame ,  width = 15)
        self.distance_entry.grid(row=1, column=1)
        distance.grid(row=1, column=0)
        self.distance_entry.insert(0,200)
        self.distance_entry.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        kasite = Label(self.parameters_frame ,  text = "Site constant (K)")
        self.kasite_entry = Entry(self.parameters_frame ,  width = 15)
        self.kasite_entry.grid(row=2, column=1)
        kasite.grid(row=2, column=0)
        self.kasite_entry.insert(0,516)
        self.kasite_entry.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        asite = Label(parameters_frame ,  text = "Site exponent (a)")
        self.asite_entry = Entry(self.parameters_frame ,  width = 15)
        self.asite_entry.grid(row=3, column=1)
        asite.grid(row=3, column=0)
        self.asite_entry.insert(0,-1.45)
        self.asite_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        # RECEIVER LABEL AND ENTRYS
        Label(receiver_frame, text = "X :").grid(row=1, column=0)
        Label(receiver_frame, text = "Y :").grid(row=2, column=0)

        Label(receiver_frame, text = "R1").grid(row=0, column=1)
        self.receivor1_x_entry = Entry(receiver_frame,  width = 5)
        self.receivor1_y_entry = Entry(receiver_frame,  width = 5)
        self.receivor1_x_entry.grid(row=1, column=1)
        self.receivor1_y_entry.grid(row=2, column=1)
        self.receivor1_x_entry.insert(0, 50)
        self.receivor1_y_entry.insert(0, 0)
        self.receivor1_x_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.receivor1_y_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        Label(receiver_frame, text = "R2").grid(row=0, column=2)
        self.receivor2_x_entry = Entry(receiver_frame,  width = 5)
        self.receivor2_y_entry = Entry(receiver_frame,  width = 5)
        self.receivor2_x_entry.grid(row=1, column=2)
        self.receivor2_y_entry.grid(row=2, column=2)
        self.receivor2_x_entry.insert(0, 0)
        self.receivor2_y_entry.insert(0, 0)
        self.receivor2_x_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.receivor2_y_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))


        Label(receiver_frame, text = "R3").grid(row=0, column=3)
        self.receivor3_x_entry = Entry(receiver_frame,  width = 5)
        self.receivor3_y_entry = Entry(receiver_frame,  width = 5)
        self.receivor3_x_entry.grid(row=1, column=3)
        self.receivor3_y_entry.grid(row=2, column=3)
        self.receivor3_x_entry.insert(0, 0)
        self.receivor3_y_entry.insert(0, 0)
        self.receivor3_x_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.receivor3_y_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        Label(receiver_frame, text = "R4").grid(row=0, column=4)
        self.receivor4_x_entry = Entry(receiver_frame,  width = 5)
        self.receivor4_y_entry = Entry(receiver_frame,  width = 5)
        self.receivor4_x_entry.grid(row=1, column=4)
        self.receivor4_y_entry.grid(row=2, column=4)
        self.receivor4_x_entry.insert(0, 0)
        self.receivor4_y_entry.insert(0, 0)
        self.receivor4_x_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.receivor4_y_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        Label(receiver_frame, text = "R5").grid(row=0, column=5)
        self.receivor5_x_entry = Entry(receiver_frame,  width = 5)
        self.receivor5_y_entry = Entry(receiver_frame,  width = 5)
        self.receivor5_x_entry.grid(row=1, column=5)
        self.receivor5_y_entry.grid(row=2, column=5)
        self.receivor5_x_entry.insert(0, 0)
        self.receivor5_y_entry.insert(0, 0)
        self.receivor5_x_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        self.receivor5_y_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        # RADIOBUTTONS AND RESULTS FRAME, IT SHOULD BE TOGETHER

        self.var = StringVar(value="dBL")
        c_pascal = Radiobutton(parameters_frame, text="kPa", variable=self.var, value = "kPa")
        c_pascal.grid(row=5, column=0)
        c_dbl = Radiobutton(parameters_frame, text="dBL", variable=self.var, value = "dBL")
        c_dbl.grid(row=5, column=1)

        Label(result_frame,textvariable=self.var).grid(row=2, column=0)

        self.var1 = self.var.get()

        Label(result_frame, text = "Distance (m) :").grid(row=1, column=0)
        Label(result_frame, text = "R1").grid(row=0, column=1)
        self.receivor1_distance_entry = Entry(result_frame,  width = 6)
        self.receivor1_dbl_entry = Entry(result_frame,  width = 6)
        self.receivor1_distance_entry.grid(row=1, column=1)
        self.receivor1_dbl_entry.grid(row=2, column=1)
        self.receivor1_distance_entry.insert(0, self.r[0])
        self.receivor1_dbl_entry.insert(0, self.total_level[0])

        Label(result_frame, text = "R2").grid(row=0, column=2)
        self.receivor2_distance_entry = Entry(result_frame,  width = 6)
        self.receivor2_dbl_entry = Entry(result_frame,  width = 6)
        self.receivor2_distance_entry.grid(row=1, column=2)
        self.receivor2_dbl_entry.grid(row=2, column=2)
        self.receivor2_distance_entry.insert(0, self.r[1])
        self.receivor2_dbl_entry.insert(0, self.total_level[1])

        Label(result_frame, text = "R3").grid(row=0, column=3)
        self.receivor3_distance_entry = Entry(result_frame,  width = 6)
        self.receivor3_dbl_entry = Entry(result_frame,  width = 6)
        self.receivor3_distance_entry.grid(row=1, column=3)
        self.receivor3_dbl_entry.grid(row=2, column=3)
        self.receivor3_distance_entry.insert(0, self.r[2])
        self.receivor3_dbl_entry.insert(0, self.total_level[2])

        Label(result_frame, text = "R4").grid(row=0, column=4)
        self.receivor4_distance_entry = Entry(result_frame,  width = 6)
        self.receivor4_dbl_entry = Entry(result_frame,  width = 6)
        self.receivor4_distance_entry.grid(row=1, column=4)
        self.receivor4_dbl_entry.grid(row=2, column=4)
        self.receivor4_distance_entry.insert(0, self.r[3])
        self.receivor4_dbl_entry.insert(0, self.total_level[3])

        Label(result_frame, text = "R5").grid(row=0, column=5)
        self.receivor5_distance_entry = Entry(result_frame,  width = 6)
        self.receivor5_dbl_entry = Entry(result_frame,  width = 6)
        self.receivor5_distance_entry.grid(row=1, column=5)
        self.receivor5_dbl_entry.grid(row=2, column=5)
        self.receivor5_distance_entry.insert(0, self.r[4])
        self.receivor5_dbl_entry.insert(0, self.total_level[4])

        # BUTTON AND COMMANDS
        button1 = Button(self.parameters_frame, text = "Calculate",command = self.update_values)
        parameters_frame.bind("<Return>", self.update_values)
        button1.grid(row=6, column=1)

        self.result_values()

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

        self.test_2()
        frame_2=Frame(self.map_frame)
        # frame_2=Frame(self.map_frame, width=1000)
        # frame_2.grid(row=0,column=1)
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

        self.charge = int(self.charge_entry.get())
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

        
        self.var1 = self.var.get()
        self.result_values()
        self.plot_values_1()
        self.plot_values_2()
        return None

    # FUNCTION FOR GRAPH IN DBL AND PA
    def test_1(self):
        p = [0, 0]
        r1 = [self.receivor1_x, self.receivor1_y]
        r2 = [self.receivor2_x, self.receivor2_y]
        r3 = [self.receivor3_x, self.receivor3_y]
        r4 = [self.receivor4_x, self.receivor4_y]
        r5 = [self.receivor5_x, self.receivor5_y]

        p_coordiantes = [r1, r2, r3, r4, r5]
        dis_rec = []

        for rx, ry in p_coordiantes:

            dis_rec.append(np.sqrt((((rx-p[0])**2)+((ry-p[1])**2))))

        r = np.array(dis_rec)
        self.r = r

        total_level = []   

        if (self.var1 == "dBL"):
            for i in dis_rec:
                total_level.append(20 * np.log10((1000*(((i/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002))))
            
            total_level = np.array(total_level)
            self.total_level = np.round(total_level,1)
            
            z1 = [20 * np.log10((1000*(((i/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002)))
                       for i in np.arange(0.1,(self.distance + 1) * np.sqrt(2)) ]

            line_1 = [120 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_2 = [125 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_3 = [133 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            x1 = np.arange(1,(self.distance + 1) * np.sqrt(2))

            figure1 = plt.figure(figsize = (5,4), dpi = 110)
            figure1.add_subplot(111)
            self.figure1=figure1


            plt.plot(z1,label="Decay Curve")
            plt.plot(x1, line_3,'b--',label="130 dbL: Maximum for Structural Damage Level" )
            plt.plot(x1, line_2,'r--',label="125 dbL: Maximum for Human Comfort Level" )
            plt.plot(x1, line_1,'g--',label="120 dbL: Annoying") 

            plt.ylabel('Pressure Level(dBL)',labelpad=1)
            plt.title('SPL DECAY')
            plt.xscale('log')
            plt.xlim(1,(self.distance + 1) * np.sqrt(2))
            plt.ylim(z1[-1],z1[1]+5)


        elif (self.var1 == "kPa"):
            for i in dis_rec:
                total_level.append(((i/(self.charge**(1/3)))**self.asite) * self.kasite)
            
            total_level = np.array(total_level)
            self.total_level = np.round(total_level,1)

            z1 = [(((i/(self.charge**(1/3)))**self.asite) * self.kasite)
                       for i in np.arange(0.1,(self.distance + 1) * np.sqrt(2)) ]
            # print(z1)
            line_1 = [20/1000 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_2 = [36.5/1000 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_3 = [89.3/1000 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            x1 = np.arange(1,(self.distance + 1) * np.sqrt(2))  

            figure1 = plt.figure(figsize = (5,4), dpi = 110)
            figure1.add_subplot(111)
            self.figure1=figure1

            plt.plot(z1,label="Decay Curve")
            plt.plot(x1, line_3,'b--',label="89.3 kPa: Maximum for Structural Damage Level" )
            plt.plot(x1, line_2,'r--',label="36.5 kPa: Maximum for Human Comfort Level" )
            plt.plot(x1, line_1,'g--',label="20 kPa: Annoying")

            plt.ylabel('Pressure (kPa)',labelpad=1)
            plt.title('kPa DECAY')
            plt.xscale('log')
            plt.yscale('log')
            plt.xlim(1,(self.distance + 1) * np.sqrt(2))
            plt.ylim(z1[-1],z1[1]+5 ) 


        # plt.scatter(r[0], total_level[0])
        # plt.scatter(r[1], total_level[1])
        # plt.scatter(r[2], total_level[2])
        # plt.scatter(r[3], total_level[3])
        # plt.scatter(r[4], total_level[4])
        # fontP = FontProperties()
        # fontP.set_size('x-small')
        # plt.xlabel('Distance (m)')
        # plt.legend(loc='upper right', prop=fontP)
        # plt.tick_params(axis='x', labelsize=8)
        # plt.tick_params(axis='y', labelsize=8)
        # plt.grid(True, which="both", ls="-")
        annotations=["R1","R2","R3","R4","R5"]
    
        for i, label in enumerate(annotations):
            plt.annotate(label, (r[i], total_level[i]))

        plt.scatter(r[0], total_level[0])
        plt.scatter(r[1], total_level[1])
        plt.scatter(r[2], total_level[2])
        plt.scatter(r[3], total_level[3])
        plt.scatter(r[4], total_level[4])
        fontP = FontProperties()
        fontP.set_size('x-small')
        plt.xlabel('Distance (m)')
        plt.legend(loc='upper right', prop=fontP)
        plt.tick_params(axis='x', labelsize=8)
        plt.tick_params(axis='y', labelsize=8)
        plt.grid(True, which="both", ls="-")

    # FUNCTION FOR MAP IN DBL AND PA
    def test_2(self):

        # MAXIMUM LEVELS
        theta = np.linspace(0, 2*np.pi, 100)
    
        r_1 = (self.charge**(1/3)) * ((2000/self.kasite)**(1/self.asite))
        xr_1 = r_1*np.cos(theta)
        yr_1 = r_1*np.sin(theta)

        r_2 = (self.charge**(1/3)) * (3557/self.kasite)**(1/self.asite)
        xr_2 = r_2*np.cos(theta)
        yr_2 = r_2*np.sin(theta)

        r_3 = (self.charge**(1/3)) * (8934/self.kasite)**(1/self.asite)
        xr_3 = r_3*np.cos(theta)
        yr_3 = r_3*np.sin(theta)

        r1 = [self.receivor1_x, self.receivor1_y]
        r2 = [self.receivor2_x, self.receivor2_y]
        r3 = [self.receivor3_x, self.receivor3_y]
        r4 = [self.receivor4_x, self.receivor4_y]
        r5 = [self.receivor5_x, self.receivor5_y]

        # GRAPH

        # z1 = [np.round(10 * np.log10(1000*(((((i/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002))**2)),0) 
        #                for i in np.arange(1,(self.distance + 1) * np.sqrt(2)) ]
        z1 = [np.round(20 * np.log10((1000*(((i/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002))),0) 
                       for i in np.arange(1,(self.distance + 1) * np.sqrt(2)) ]
        
        N = self.distance
        x = np.linspace(-N, N, 2000)
        y = np.linspace(-N, N, 2000)
        X,Y = np.meshgrid(x,y)

        # CENTER POINT
        p = [0 , 0]
        
        # DISTANCE
        R = np.sqrt((((p[0]-X)**2)+((p[1]-Y)**2)))


        if (self.var1 == "dBL"):
        # EQUATION
    
            # z = 10 * np.log10(1000*(((((R/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002))**2))
            z = 20 * np.log10((1000*(((R/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002)))
            Z= np.array(z).reshape(len(y),len(x))
            figure2 = plt.figure(figsize = (5,4), dpi = 110)
            self.figure2 = figure2
            noisemap = figure2.add_subplot(111)

            levls = np.array([120,125,133])
            cs_1 = noisemap.contour(X,Y,Z,levels = levls,colors='k',linestyles=('-','-.','--'))

            c = noisemap.contourf(X,Y,Z,levels=np.round(np.linspace(z1[-1],z1[0],25),3),cmap=cm.jet)
            # c = noisemap.contourf(X,Y,Z,cmap=cm.jet)
            figure2.colorbar(c,ax=noisemap).ax.set_title('dBL')

            levls = np.array([120,125,133])
            cs_1 = noisemap.contour(X,Y,Z,levels = levls,colors='k',linestyles=('-','-.','--'))
            plt.plot(levls[0],'k-',label="120 dBL")
            plt.plot( levls[1],'k-.',label="125 dBL")
            plt.plot( levls[2],'k--',label="133 dBL")
            

        elif (self.var1 == "kPa"):

            z = (( R/ (self.charge**(1 / 3)) )**self.asite) * self.kasite
            Z= np.array(z).reshape(len(y),len(x))
            z_pascal = [(( i / (self.charge**(1 / 3)) )**self.asite) * 516 for i in np.arange(0.5,(N +1)*np.sqrt(2)) ]

            florr = np.log10(z_pascal[-1])
            florr_1 = np.floor(florr)
            florr2 = np.log10(z_pascal[0])
            florr_2 = np.ceil(florr2)
            rango = np.arange(florr_1 , florr_2)
            levs_1 = [10**n for n in np.arange(florr_1, florr_2)]
            levs_2 = [3*10**n for n in np.arange(florr_1 , florr_2)]
            levs_3 = [5*10**n for n in np.arange(florr_1 , florr_2)]
            levs_4 = [8*10**n for n in np.arange(florr_1 , florr_2-1)]
            levs_5 = sorted(levs_1 + levs_2 + levs_3 + levs_4)

            # florr = np.log10(z.min())
            # florr_1 = np.floor(florr)
            # florr2 = np.log10(z.max())
            # florr_2 = np.ceil(florr2)
            # rango = np.arange(florr_1 , florr_2)
            # levs_1 = [10**n for n in np.arange(florr_1, florr_2)]
            # levs_2 = [2*10**n for n in np.arange(florr_1 , florr_2)]
            # levs_3 = [3*10**n for n in np.arange(florr_1 , florr_2)]
            # levs_4 = [5*10**n for n in np.arange(florr_1 , florr_2)]
            # levs_5 = [8*10**n for n in np.arange(florr_1 , florr_2-1)]

            # levs_total = sorted(levs_1 + levs_2 + levs_3 + levs_4 + levs_5)
            # lvl = levs_total



            levls = np.array([20/1000,35/1000,89/1000])
            figure2 = plt.figure(figsize = (5,4), dpi = 110)
            self.figure2 = figure2
            noisemap = figure2.add_subplot(111)
            c = noisemap.contourf(X,Y,Z,levels=levs_5,norm=LogNorm(),cmap=cm.jet)
            
            cs_1 = noisemap.contour(X,Y,Z,levels = levls,colors='k',linestyles=('-','-.','--'))
            figure2.colorbar(c,ax=noisemap,ticks=[1, 10, 100, 1000, 10000]).ax.set_title('kPa')
            
            # plt.plot(xr_3 , yr_3 , 'k--',label="89 kPa")
            # plt.plot(xr_2 , yr_2 , 'k-.',label="35 kPa")
            # plt.plot(xr_1 , yr_1 , 'k-',label="20 k55Pa")
            plt.plot(levls[0],'k-',label="20 Pa")
            plt.plot( levls[1],'k-.',label="35 Pa")
            plt.plot( levls[2],'k--',label="89 Pa")
            
  
        plt.xlabel('Distance (m)')
        plt.ylabel('Distance (m)',labelpad=0)
        plt.title('Noise Map')
        Xflat, Yflat, Zflat = X.flatten(), Y.flatten(), Z.flatten()
        def fmt(x, y):

    # get closest point with known data
            dist = np.linalg.norm(np.vstack([Xflat - x, Yflat - y]), axis=0)
            idx = np.argmin(dist)
            z = Zflat[idx]
            return 'x={x:.5f}  y={y:.5f}  z={z:.5f}'.format(x=x, y=y, z=z)

        annotations=["R1","R2","R3","R4","R5"]
        r_x = [r1[0], r2[0], r3[0], r4[0], r5[0]]
        r_y = [r1[1], r2[1], r3[1], r4[1], r5[1]]
    
        for i, label in enumerate(annotations):
            plt.annotate(label, (r_x[i], r_y[i]))

        
        plt.gca().format_coord = fmt
        
        plt.scatter(r1[0], r1[1],c='w')
        plt.scatter(r2[0], r2[1],c='w')
        plt.scatter(r3[0], r3[1],c='w')
        plt.scatter(r4[0], r4[1],c='w')
        plt.scatter(r5[0], r5[1],c='w')

        fontP = FontProperties()
        fontP.set_size('small')
        plt.legend(loc='upper left', prop=fontP)
        plt.xlim(-N,N)
        plt.ylim(-N,N)
        plt.tick_params(axis='x', labelsize=8)
        plt.tick_params(axis='y', labelsize=8)
        plt.grid(True, which="both", ls="-")
    
    # FUNCTION FOR RESULTS IN DBL AND PA
    def result_values(self):
        
        self.receivor1_distance_entry.delete(0, END)
        self.receivor1_dbl_entry.delete(0, END)

        self.receivor2_distance_entry.delete(0, END)
        self.receivor2_dbl_entry.delete(0, END)

        self.receivor3_distance_entry.delete(0, END)
        self.receivor3_dbl_entry.delete(0, END)

        self.receivor4_distance_entry.delete(0, END)
        self.receivor4_dbl_entry.delete(0, END)

        self.receivor5_distance_entry.delete(0, END)
        self.receivor5_dbl_entry.delete(0, END)

        p = [0, 0]
        r1 = [self.receivor1_x, self.receivor1_y]
        r2 = [self.receivor2_x, self.receivor2_y]
        r3 = [self.receivor3_x, self.receivor3_y]
        r4 = [self.receivor4_x, self.receivor4_y]
        r5 = [self.receivor5_x, self.receivor5_y]

        p_coordiantes = [r1, r2, r3, r4, r5]
        dis_rec = []

        for rx, ry in p_coordiantes:

            dis_rec.append(np.sqrt((((rx-p[0])**2)+((ry-p[1])**2))))

        r = np.array(dis_rec)
        self.r = np.round(r,1)
        total_level = [] 

        if (self.var1 == "dBL"):
            for i in dis_rec:
                total_level.append(20 * np.log10((1000*(((i/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002))))

        elif (self.var1 == "kPa"):
            for i in dis_rec:
                total_level.append(((i/(self.charge**(1/3)))**self.asite) * self.kasite)


        total_level = np.array(total_level)
        self.total_level = np.round(total_level,1)

        self.receivor1_distance_entry.insert(0, self.r[0])
        self.receivor1_dbl_entry.insert(0, self.total_level[0])

        self.receivor2_distance_entry.insert(0, self.r[1])
        self.receivor2_dbl_entry.insert(0, self.total_level[1])

        self.receivor3_distance_entry.insert(0, self.r[2])
        self.receivor3_dbl_entry.insert(0, self.total_level[2])

        self.receivor4_distance_entry.insert(0, self.r[3])
        self.receivor4_dbl_entry.insert(0, self.total_level[3])

        self.receivor5_distance_entry.insert(0, self.r[4])
        self.receivor5_dbl_entry.insert(0, self.total_level[4])
  
        return None

    # FUNCTION FOR PLOT THE GRAPH VALUES
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
        self.test_2()
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