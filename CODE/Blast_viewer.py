import customtkinter
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

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
import gc
from tkinter import messagebox

plt.rcParams.update({'figure.max_open_warning': 0})
plt.rcParams['savefig.dpi'] = 1200
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():

    root = customtkinter.CTk()
    gui = Window(root)
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.quit()
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    gui.root.mainloop()
    

    return None

class Window:
    def __init__(self,root):

        # s = ttk.Style()
        # s.configure('Red.TLabelframe.Label', font=('courier', 15, 'bold'))

        # ------------------------------------------------------------------------------------------------
        # FRAMES
        self.root = root
        self.root.title("Blast Viewer. BETA")
        img = PhotoImage(file=resource_path("image.png"))  # Replace "image.png" with any image file.
        self.root.iconphoto(False, img)
        # self.root.iconbitmap(r'C:\Users\Matias Rios\Desktop\Codigo_Python\Blast_viewer_modernGUI\favicon.ico')
        self.root.geometry('1450x1000')
        self.root.resizable(False,False)

        mapsize_frame =LabelFrame(self.root,text="Map boundaries", padx=10,pady=10, width=210, height=100, font=("TkDefaultFont", 9, "bold"))
        # mapsize_frame =customtkinter.CTkFrame(self.root, padx=10,pady=10, width=210, height=100)
        mapsize_frame.grid(row = 0, column = 2, sticky = W , padx=20, pady=20)
        self.mapsize_frame = mapsize_frame

        blast_frame =LabelFrame(self.root, text="Blast parameters",  padx=10,pady=10, width=210, height=160, font=("TkDefaultFont", 9, "bold"))
        # blast_frame.place(x = 40, y = 120)
        # blast_frame.grid_propagate(False)
        blast_frame.grid(row = 1, column = 2, sticky = W, padx=20, pady=20)
        self.blast_frame = blast_frame

        airblast_frame =LabelFrame(self.root, text="Airblast constants",  padx=10,pady=10, width=210, height=100, font=("TkDefaultFont", 9, "bold"))
        # airblast_frame.place(x = 40, y = 300)
        # airblast_frame.grid_propagate(False)
        airblast_frame.grid(row = 2, column = 2, sticky = W, padx=20, pady=20)
        self.airblast_frame = airblast_frame

        groundvibration_frame =LabelFrame(self.root, text="Ground Vibration constants",  padx=10,pady=10, width=210, height=100, font=("TkDefaultFont", 9, "bold"))
        # groundvibration_frame.place(x = 40, y = 420)
        # groundvibration_frame.grid_propagate(False)
        groundvibration_frame.grid(row = 3, column = 2, sticky = W, padx=20, pady=20)
        self.groundvibration_frame = groundvibration_frame


        receiver_frame = LabelFrame(self.root,text="Receiver coordinates",  padx=10,pady=10, width=210, height=100, font=("TkDefaultFont", 9, "bold"))
        # receiver_frame.place(x = 40, y = 550)
        # receiver_frame.grid_propagate(False)
        receiver_frame.grid(row = 4, column = 2, sticky = W, padx=20, pady=20)
        self.receiver_frame = receiver_frame

        calculate_frame = customtkinter.CTkFrame(self.root,  padx=10,pady=10)
        # calculate_frame.place(x = 40, y = 670)
        calculate_frame.grid(row = 5, column = 2, sticky = W, padx=20, pady=20)
        self.calculate_frame = calculate_frame

        airblast_graph_frame =LabelFrame(self.root, text="")
        airblast_graph_frame.place(x = 300, y = 1)
        # airblast_graph_frame.grid(row = 0, column = 3, padx=1, pady=1)
        self.airblast_graph_frame = airblast_graph_frame

        airblast_map_frame =LabelFrame(self.root, text="")
        airblast_map_frame.place(x = 870, y = 1)
        self.airblast_map_frame = airblast_map_frame

        ground_graph_frame =LabelFrame(self.root, text="")
        ground_graph_frame.place(x = 300, y = 500)
        self.ground_graph_frame = ground_graph_frame

        ground_map_frame =LabelFrame(self.root, text="")
        ground_map_frame.place(x = 870, y = 500)
        self.ground_map_frame = ground_map_frame


        # ------------------------------------------------------------------------------------------------
        #INITIAL DATA
        self.distance = 200
        self.grid_size = 20
        self.color_level = 25

        self.charge = 5

        self.kasite = 516
        self.asite = -1.45

        self.kground = 1140
        self.bsite = -1.6

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

        self.r = [0,0,0,0,0]
        self.total_level = [0,0,0,0,0]

        self.charge_PX_1 = -50
        self.charge_PY_1 = 50

        self.blast_radio_1 = 50
        self.blast_radio_2 = 100
        self.blast_radio_3 = 150


        
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
        
        distance = Label(self.mapsize_frame ,  text = "Map Size (m):    ")
        self.distance_entry = Entry(self.mapsize_frame ,  width = 15)
        self.distance_entry.grid(row=1, column=1)
        distance.grid(row=1, column=0)
        self.distance_entry.insert(0,200)
        self.distance_entry.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        grid_size = Label(self.mapsize_frame ,  text = "Grid Size (m):   ")
        self.grid_size_entry = Entry(self.mapsize_frame ,  width = 15)
        self.grid_size_entry.grid(row=2, column=1)
        grid_size.grid(row=2, column=0)
        self.grid_size_entry.insert(0,20)
        self.grid_size_entry.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        color_level = Label(self.mapsize_frame ,  text = "Color Division:     ")
        self.color_level_entry = Entry(self.mapsize_frame ,  width = 15)
        self.color_level_entry.grid(row=3, column=1)
        color_level.grid(row=3, column=0)
        self.color_level_entry.insert(0,25)
        self.color_level_entry.config(validate="key",validatecommand=(reg_2,'%v','%P'))


        charge = Label(self.blast_frame ,  text = "Charge Q (kg): ")
        self.charge_entry = Entry(self.blast_frame ,  width = 15)
        self.charge_entry.grid(row=0, column=1)
        self.charge_entry.insert(0,5)
        charge.grid(row=0, column=0)
        self.charge_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))

        
        Label(self.blast_frame, text = "X Coordinate: ").grid(row=1, column=0)
        Label(self.blast_frame, text = "Y Coordinate: ").grid(row=2, column=0)
        self.charge_entry_PX_1 = Entry(self.blast_frame,  width = 15)
        self.charge_entry_PY_1 = Entry(self.blast_frame,  width = 15)
        self.charge_entry_PX_1.insert(0,-50)
        self.charge_entry_PY_1.insert(0,50)
        self.charge_entry_PX_1.grid(row=1, column=1)
        self.charge_entry_PY_1.grid(row=2, column=1)

        Label(self.blast_frame, text = "Blast radio 1 (m): ").grid(row=3, column=0)
        Label(self.blast_frame, text = "Blast radio 2 (m): ").grid(row=4, column=0)
        Label(self.blast_frame, text = "Blast radio 3 (m): ").grid(row=5, column=0)
        self.blast_radio_entry_1 = Entry(self.blast_frame,  width = 15)
        self.blast_radio_entry_2 = Entry(self.blast_frame,  width = 15)
        self.blast_radio_entry_3 = Entry(self.blast_frame,  width = 15)
        self.blast_radio_entry_1.grid(row=3, column=1)
        self.blast_radio_entry_2.grid(row=4, column=1)
        self.blast_radio_entry_3.grid(row=5, column=1)
        self.blast_radio_entry_1.config(validate="key",validatecommand=(reg_2,'%v','%P'))
        self.blast_radio_entry_2.config(validate="key",validatecommand=(reg_2,'%v','%P'))
        self.blast_radio_entry_3.config(validate="key",validatecommand=(reg_2,'%v','%P'))
        self.blast_radio_entry_1.insert(0,50)
        self.blast_radio_entry_2.insert(0,100)
        self.blast_radio_entry_3.insert(0,150)

       
        kasite = Label(self.airblast_frame ,  text = "Site constant (Ka)")
        self.kasite_entry = Entry(self.airblast_frame ,  width = 15)
        self.kasite_entry.grid(row=0, column=1)
        kasite.grid(row=0, column=0)
        self.kasite_entry.insert(0,516)
        self.kasite_entry.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        asite = Label(self.airblast_frame ,  text = "Site exponent (a)")
        self.asite_entry = Entry(self.airblast_frame ,  width = 15)
        self.asite_entry.grid(row=1, column=1)
        asite.grid(row=1, column=0)
        self.asite_entry.insert(0,-1.45)
        self.asite_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
        
        kground = Label(self.groundvibration_frame ,  text = "Site constant (Kg)")
        self.kground_entry = Entry(self.groundvibration_frame ,  width = 15)
        self.kground_entry.grid(row=0, column=1)
        kground.grid(row=0, column=0)
        self.kground_entry.insert(0,1140)
        self.kground_entry.config(validate="key",validatecommand=(reg_2,'%v','%P'))

        bsite = Label(self.groundvibration_frame ,  text = "Site exponent (b)")
        self.bsite_entry = Entry(self.groundvibration_frame ,  width = 15)
        self.bsite_entry.grid(row=1, column=1)
        bsite.grid(row=1, column=0)
        self.bsite_entry.insert(0,-1.6)
        self.bsite_entry.config(validate="key",validatecommand=(reg_1,'%v','%P'))
    
        # ------------------------------------------------------------------------------------------------
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


        # ------------------------------------------------------------------------------------------------
        # RADIOBUTTONS
        self.var_air = StringVar(value="dBL")
        c_pascal = customtkinter.CTkRadioButton(airblast_frame, text="kPa", variable=self.var_air, value = "kPa",height=15, width=15)
        c_pascal.grid(row=3, column=0)
        c_dbl = customtkinter.CTkRadioButton(airblast_frame, text="dBL", variable=self.var_air, value = "dBL",height=15, width=15)
        c_dbl.grid(row=3, column=1)
        self.var_air_ = self.var_air.get()

        self.var_ground = StringVar(value="dBV")
        c_vibration = customtkinter.CTkRadioButton(groundvibration_frame, text="PPV", variable=self.var_ground, value = "PPV",height=15, width=15)
        c_vibration.grid(row=3, column=0)
        c_dbv = customtkinter.CTkRadioButton(groundvibration_frame, text="dBV", variable=self.var_ground, value = "dBV",height=15, width=15)
        c_dbv.grid(row=3, column=1)
        self.var_ground_ = self.var_ground.get()

        # ------------------------------------------------------------------------------------------------
        # BUTTON AND COMMAND
        calculate_button = customtkinter.CTkButton(self.calculate_frame, text = "Calculate",command = self.update_values, width=180,height=50,border_width=2,text_font='bold')
        calculate_button.grid(row=0, column=0)
       
        # ------------------------------------------------------------------------------------------------
        #INITIAL CALCULATION
        self.graph_pressure()
        frame_graph_pressure=Frame(self.airblast_graph_frame)
        frame_graph_pressure.pack()
        self.frame_graph_pressure=frame_graph_pressure
        chart_graph_pressure = FigureCanvasTkAgg(self.figure_graph_pressure,self.frame_graph_pressure)
        chart_graph_pressure.get_tk_widget().pack()
        self.chart_graph_pressure =chart_graph_pressure
        toolbar_graph_pressure = NavigationToolbar2Tk(chart_graph_pressure,self.frame_graph_pressure)
        toolbar_graph_pressure.update()
        chart_graph_pressure.get_tk_widget().pack()

        self.map_pressure()
        frame_map_pressure=Frame(self.airblast_map_frame)
        frame_map_pressure.pack()
        self.frame_map_pressure=frame_map_pressure
        chart_map_pressure = FigureCanvasTkAgg(self.figure_map_pressure,self.frame_map_pressure)
        chart_map_pressure.get_tk_widget().pack()
        self.chart_map_pressure =chart_map_pressure
        toolbar_map_pressure = NavigationToolbar2Tk(chart_map_pressure,self.frame_map_pressure)
        toolbar_map_pressure.update()
        chart_map_pressure.get_tk_widget().pack()

        self.graph_vibration()
        frame_graph_vibration=Frame(self.ground_graph_frame)
        frame_graph_vibration.pack()
        self.frame_graph_vibration=frame_graph_vibration
        chart_graph_vibration = FigureCanvasTkAgg(self.figure_graph_vibration,self.frame_graph_vibration)
        chart_graph_vibration.get_tk_widget().pack()
        self.chart_graph_vibration =chart_graph_vibration
        toolbar_graph_vibration = NavigationToolbar2Tk(chart_graph_vibration,self.frame_graph_vibration)
        toolbar_graph_vibration.update()
        chart_graph_vibration.get_tk_widget().pack()

        self.map_vibration()
        frame_map_vibration=Frame(self.ground_map_frame)
        frame_map_vibration.pack()
        self.frame_map_vibration=frame_map_vibration
        chart_map_vibration = FigureCanvasTkAgg(self.figure_map_vibration,self.frame_map_vibration)
        chart_map_vibration.get_tk_widget().pack()
        self.chart_map_vibration =chart_map_vibration
        toolbar_map_vibration = NavigationToolbar2Tk(chart_map_vibration,self.frame_map_vibration)
        toolbar_map_vibration.update()
        chart_map_vibration.get_tk_widget().pack()


        # ------------------------------------------------------------------------------------------------
        #  GENERAL COMMAND FOR BUTTON
    def update_values(self, event=None):

        def calculate():

            img = PhotoImage(file=resource_path("image.png"))  # Replace "image.png" with any image file.
            
            popup = Tk.Toplevel()
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            popup.geometry("+%d+%d" % (x + 600, y + 450))
            Tk.Label(popup, text="Calculating..",font=('',12)).pack(side="top", fill=None, pady=25)

            progress_var = Tk.DoubleVar()
            progress_bar = ttk.Progressbar(popup, variable=progress_var,mode='determinate',length=280)
            progress_bar.pack(side="top",fill=None,expand=True, padx=30, pady=5)

            popup.iconphoto(False, img)

            self.distance = int(self.distance_entry.get())
            self.grid_size = int(self.grid_size_entry.get())
            self.color_level = int(self.color_level_entry.get())

            self.charge = int(self.charge_entry.get())

            self.kasite = int(self.kasite_entry.get())
            self.asite = float(self.asite_entry.get())

            self.kground = int(self.kground_entry.get())
            self.bsite = float(self.bsite_entry.get())


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

            self.blast_radio_1 = int(self.blast_radio_entry_1.get())
            self.blast_radio_2 = int(self.blast_radio_entry_2.get())
            self.blast_radio_3 = int(self.blast_radio_entry_3.get())
            
            
            self.var_air_ = self.var_air.get()
            self.var_ground_ = self.var_ground.get()


            def on_calculate():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    root.quit()
                    root.destroy()
        
            # starttime = timeit.default_timer()
            
            popup.update()
            progress_var.set(25)
            self.plot_graph_pressure()
            popup.update()
            progress_var.set(25)
            
            popup.update()
            progress_var.set(50)
            self.plot_map_pressure()

            self.plot_graph_vibration()
            popup.update()
            progress_var.set(75)

            popup.update()
            progress_var.set(100)
            self.plot_map_vibration()
            popup.update()
            progress_var.set(100)

            # print("The time difference is :", timeit.default_timer() - starttime)
            popup.after(100, popup.destroy)

            popup2 = Tk.Toplevel()
            popup2.iconphoto(False, img)
            popup2.geometry("+%d+%d" % (x + 650, y + 450))
            Tk.Label(popup2, text="                   Done!                   ",font=('',12)).pack(side="top", fill=X, pady=25)
            popup2.after(1000, popup2.destroy)
            gc.collect()

        if float(self.distance_entry.get())/float(self.grid_size_entry.get())  >  10000 :
            
            if messagebox.askokcancel("WARNING", "The relation Map size/Grid size is too big. This will cause a highly ram usage and time computation causing the program to crash. Do you want to continue?"):
                
                calculate()
        
        elif float(self.distance_entry.get())/float(self.grid_size_entry.get())  >  1000 :
            
            if messagebox.askokcancel("Warning", "Small grid size with a big map size results in longer calculation time with high ram usage. Do you want to continue?"):
                
                calculate()

        else:
        
            calculate()

    
        return None


    # ------------------------------------------------------------------------------------------------
    # FUNCTION FOR GRAPH IN DBL AND PA
    def graph_pressure(self):

        def overpressure_function_db(self,blast):

            blast_radio = 20 * np.log10((1000*(((blast/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002)))
            return  blast_radio

        def overpressure_function_kpa(self,blast):

            blast_radio = ((blast/(self.charge**(1/3)))**self.asite) * self.kasite
            return  blast_radio

        p  =  [self.charge_PX_1, self.charge_PY_1]
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

        if (self.var_air_ == "dBL"):


            for i in dis_rec:
                total_level.append(20 * np.log10((1000*(((i/(self.charge**(1/3)))**self.asite) 
                                    * self.kasite)/(0.00002))))
            
            total_level = np.array(total_level)
            self.total_level = np.round(total_level,1)
            
            z1 = [20 * np.log10((1000*(((i/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002)))
                       for i in np.arange(0.1,(self.distance + 1) * np.sqrt(2)) ]

            
            blast_radio_1 = overpressure_function_db(self,self.blast_radio_1)
            blast_radio_2 = overpressure_function_db(self,self.blast_radio_2)
            blast_radio_3 = overpressure_function_db(self,self.blast_radio_3)

            line_1 = [blast_radio_1 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_2 = [blast_radio_2 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_3 = [blast_radio_3 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            x1 = np.arange(1,(self.distance + 1) * np.sqrt(2))

            figure_graph_pressure = plt.figure(figsize = (5,4), dpi = 110)
            figure_graph_pressure.add_subplot(111)
            self.figure_graph_pressure=figure_graph_pressure


            plt.plot(z1,label="Decay Curve")
            plt.plot(x1, line_1,'b--',label='Blast radio 1: '+str(self.blast_radio_1)+'='+str(np.round(blast_radio_1,0))+'dBL')
            plt.plot(x1, line_2,'r--',label='Blast radio 2: '+str(self.blast_radio_2)+' = '+str(np.round(blast_radio_2,0))+'dBL' )
            plt.plot(x1, line_3,'g--',label='Blast radio 3: '+str(self.blast_radio_3)+' = '+str(np.round(blast_radio_3,0))+'dBL')  

            plt.ylabel('Pressure Level(dBL)',labelpad=1)
            plt.title('SPL DECAY')
            plt.xscale('log')
            plt.xlim(1,(self.distance + 1) * np.sqrt(2))
            plt.ylim(z1[-1],z1[1]+5)


        elif (self.var_air_ == "kPa"):

            for i in dis_rec:
                total_level.append(((i/(self.charge**(1/3)))**self.asite) 
                                    * self.kasite)
            
            total_level = np.array(total_level)
            self.total_level = np.round(total_level,1)

            z1 = [(((i/(self.charge**(1/3)))**self.asite) * self.kasite)
                       for i in np.arange(0.1,(self.distance + 1) * np.sqrt(2)) ]
            
            blast_radio_1 = overpressure_function_kpa(self,self.blast_radio_1)
            blast_radio_2 = overpressure_function_kpa(self,self.blast_radio_2)
            blast_radio_3 = overpressure_function_kpa(self,self.blast_radio_3)
            

            line_1 = [blast_radio_1 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_2 = [blast_radio_2 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_3 = [blast_radio_3 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]

            x1 = np.arange(1,(self.distance + 1) * np.sqrt(2))  

            figure_graph_pressure = plt.figure(figsize = (5,4), dpi = 110)
            figure_graph_pressure.add_subplot(111)
            self.figure_graph_pressure=figure_graph_pressure

            plt.plot(z1,label="Decay Curve")
            plt.plot(x1, line_1,'b--',label='Blast radio 1: '+str(self.blast_radio_1)+'m = '+str(np.round(blast_radio_1,1))+'kPa')
            plt.plot(x1, line_2,'r--',label='Blast radio 2: '+str(self.blast_radio_2)+'m = '+str(np.round(blast_radio_2,1))+'kPa' )
            plt.plot(x1, line_3,'g--',label='Blast radio 3: '+str(self.blast_radio_3)+'m = '+str(np.round(blast_radio_3,1))+'kPa')
            plt.ylabel('Pressure (kPa)',labelpad=1)
            plt.title('kPa DECAY')
            plt.xscale('log')
            plt.yscale('log')
            plt.xlim(1,(self.distance + 1) * np.sqrt(2))
            plt.ylim(z1[-1],z1[1]+5 ) 

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

    # ------------------------------------------------------------------------------------------------
    # FUNCTION FOR MAP IN DBL AND PA
    def map_pressure(self):

        def overpressure_function_db(self,blast):

            blast_radio = 20 * np.log10((1000*(((blast/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002)))
            return  blast_radio

        def overpressure_function_kpa(self,blast):

            blast_radio = ((blast/(self.charge**(1/3)))**self.asite) * self.kasite
            return  blast_radio

        r1 = [self.receivor1_x, self.receivor1_y]
        r2 = [self.receivor2_x, self.receivor2_y]
        r3 = [self.receivor3_x, self.receivor3_y]
        r4 = [self.receivor4_x, self.receivor4_y]
        r5 = [self.receivor5_x, self.receivor5_y]
 
        N = self.distance
        steps = (2*N)//self.grid_size
        x = np.linspace(-N, N, steps+1)
        y = np.linspace(-N, N, steps+1)
        X,Y = np.meshgrid(x,y)

        p = [self.charge_PX_1, self.charge_PY_1]
        R = np.sqrt((((p[0]-X)**2)+((p[1]-Y)**2)))


        if (self.var_air_ == "dBL"):
       
            z = 20 * np.log10((1000*(((R/(self.charge**(1/3)))**self.asite) * self.kasite)/(0.00002)))
            Z = np.array(z).reshape(len(y),len(x))
            figure_map_pressure = plt.figure(figsize = (5,4), dpi = 110)
            self.figure_map_pressure = figure_map_pressure
            noisemap = figure_map_pressure.add_subplot(111)
            
            blast_radio_1 = overpressure_function_db(self,self.blast_radio_1)
            blast_radio_2 = overpressure_function_db(self,self.blast_radio_2)
            blast_radio_3 = overpressure_function_db(self,self.blast_radio_3)

            levls = np.array([blast_radio_3,blast_radio_2,blast_radio_1])
            cs_1 = noisemap.contour(X,Y,Z,levels = levls,colors='k',linestyles=('-','-.','--'))

            c = noisemap.contourf(X,Y,Z,levels=np.round(np.linspace(80,230,self.color_level+1),3),cmap=cm.jet)
            figure_map_pressure.colorbar(c,ax=noisemap).ax.set_title('dBL')

            plt.plot( levls[2],'k--',label=str(np.round(blast_radio_1,0))+' dBL')
            plt.plot( levls[1],'k-.',label=str(np.round(blast_radio_2,0))+' dBL')
            plt.plot( levls[0],'k-',label=str(np.round(blast_radio_3,0))+' dBL')
            

        elif (self.var_air_ == "kPa"):

            z = (( R/ (self.charge**(1 / 3)) )**self.asite) * self.kasite
            Z= np.array(z).reshape(len(y),len(x))
        
            levs_1 = [10**n for n in np.arange(np.log10(0.0002), np.log10(2000)+1,7/self.color_level)]
            
            blast_radio_1 = overpressure_function_kpa(self,self.blast_radio_1)
            blast_radio_2 = overpressure_function_kpa(self,self.blast_radio_2)
            blast_radio_3 = overpressure_function_kpa(self,self.blast_radio_3)
            
            levls_ranges = np.array([blast_radio_3,blast_radio_2,blast_radio_1])

            figure_map_pressure = plt.figure(figsize = (5,4), dpi = 110)
            self.figure_map_pressure = figure_map_pressure
            noisemap = figure_map_pressure.add_subplot(111)
            c = noisemap.contourf(X,Y,Z,levels=levs_1,norm=LogNorm(),cmap=cm.jet)
           
            cs_1 = noisemap.contour(X,Y,Z,levels = levls_ranges,colors='k',linestyles=('-','-.','--'))
            figure_map_pressure.colorbar(c,ax=noisemap,ticks=[0.001, 0.01, 0.1 , 1, 10, 100, 1000, 10000]).ax.set_title('kPa')
            
            plt.plot(levls_ranges[2],'k--',label=str(np.round(blast_radio_1,1))+' kPa')
            plt.plot(levls_ranges[1],'k-.',label=str(np.round(blast_radio_2,1))+' kPa')
            plt.plot(levls_ranges[0],'k-',label=str(np.round(blast_radio_3,1))+' kPa')
            
        plt.xlabel('Distance (m)')
        plt.ylabel('Distance (m)',labelpad=0)
        plt.title('Noise Map')

        Xflat, Yflat, Zflat = X.flatten(), Y.flatten(), Z.flatten()

        def fmt(x, y):

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
        fontP.set_size('x-small')
        plt.legend(loc='upper right', prop=fontP)
        plt.xlim(-N,N)
        plt.ylim(-N,N)
        plt.tick_params(axis='x', labelsize=8)
        plt.tick_params(axis='y', labelsize=8)
        plt.grid(True, which="both", ls="-")


    # ------------------------------------------------------------------------------------------------
    # FUNCTION FOR GRAPH IN DBV AND PPV
    def graph_vibration(self):

        def groundvibration_function_dbv(self,blast):

            blast_radio = 10 * np.log10((((((blast/(self.charge**(1/2)))**self.bsite) * self.kground)/(0.000001))**2))
            return  blast_radio

        def groundvibration_function_ppv(self,blast):

            blast_radio = ((blast/(self.charge**(1/2)))**self.bsite) * self.kground
            return  blast_radio

        p = [self.charge_PX_1, self.charge_PY_1]
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

        if (self.var_ground_ == "dBV"):
            for i in dis_rec:
                total_level.append(10 * np.log10((((((i/(self.charge**(1/2)))**self.bsite) * self.kground)/(0.000001))**2)))
            
            total_level = np.array(total_level)
            self.total_level = np.round(total_level,1)
            
            z1 = [(10 * np.log10((((((i/(self.charge**(1/2)))**self.bsite) * self.kground)/(0.000001))**2))) 
                       for i in np.arange(0.1,(self.distance + 1) * np.sqrt(2)) ]

            blast_radio_1 = groundvibration_function_dbv(self,self.blast_radio_1)
            blast_radio_2 = groundvibration_function_dbv(self,self.blast_radio_2)
            blast_radio_3 = groundvibration_function_dbv(self,self.blast_radio_3)

            line_1 = [blast_radio_1 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_2 = [blast_radio_2 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_3 = [blast_radio_3 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]

            x1 = np.arange(1,(self.distance + 1) * np.sqrt(2))

            figure_graph_vibration = plt.figure(figsize = (5,4), dpi = 110)
            figure_graph_vibration.add_subplot(111)
            self.figure_graph_vibration=figure_graph_vibration

            plt.plot(z1,label="Decay Curve")
            plt.plot(x1, line_1,'b--',label='Blast radio 1: '+str(self.blast_radio_1)+'='+str(np.round(blast_radio_1,0))+' dBV')
            plt.plot(x1, line_2,'r--',label='Blast radio 2: '+str(self.blast_radio_2)+' = '+str(np.round(blast_radio_2,0))+' dBV' )
            plt.plot(x1, line_3,'g--',label='Blast radio 3: '+str(self.blast_radio_3)+' = '+str(np.round(blast_radio_3,0))+' dBV') 

            plt.ylabel('Vibration Level(dBV)',labelpad=1)
            plt.title('Vibration Level DECAY')
            plt.xscale('log')
            plt.xlim(1,(self.distance + 1) * np.sqrt(2))
            plt.ylim(z1[-1],z1[1]+5)


        elif (self.var_ground_ == "PPV"):
            for i in dis_rec:
                total_level.append(((i/(self.charge**(1/2)))**self.bsite) * self.kground)
            
            total_level = np.array(total_level)
            self.total_level = np.round(total_level,1)

            z1 = [(((i/(self.charge**(1/2)))**self.bsite) * self.kground) 
                       for i in np.arange(0.1,(self.distance + 1) * np.sqrt(2)) ]

            blast_radio_1 = groundvibration_function_ppv(self,self.blast_radio_1)
            blast_radio_2 = groundvibration_function_ppv(self,self.blast_radio_2)
            blast_radio_3 = groundvibration_function_ppv(self,self.blast_radio_3)
            
            line_1 = [blast_radio_1 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_2 = [blast_radio_2 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]
            line_3 = [blast_radio_3 for i in np.arange(1,(self.distance + 1) * np.sqrt(2))]

            x1 = np.arange(1,(self.distance + 1) * np.sqrt(2))  

            figure_graph_vibration = plt.figure(figsize = (5,4), dpi = 110)
            figure_graph_vibration.add_subplot(111)
            self.figure_graph_vibration=figure_graph_vibration

            plt.plot(z1,label="Decay Curve")
            plt.plot(x1, line_1,'b--',label='Blast radio 1: '+str(self.blast_radio_1)+'m = '+str(np.round(blast_radio_1,1))+' mm/s')
            plt.plot(x1, line_2,'r--',label='Blast radio 2: '+str(self.blast_radio_2)+'m = '+str(np.round(blast_radio_2,1))+' mm/s' )
            plt.plot(x1, line_3,'g--',label='Blast radio 3: '+str(self.blast_radio_3)+'m = '+str(np.round(blast_radio_3,1))+' mm/s')

            plt.ylabel('Peak Particle Velocity (mm / s)',labelpad=1)
            plt.title('PPV DECAY')
            plt.xscale('log')
            plt.yscale('log')
            plt.xlim(1,(self.distance + 1) * np.sqrt(2))
            plt.ylim(z1[-1],z1[1]+5 ) 

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

    
    # ------------------------------------------------------------------------------------------------
    # FUNCTION FOR MAP IN DBV AND PPV
    def map_vibration(self):

        def groundvibration_function_dbv(self,blast):

            blast_radio = 10 * np.log10((((((blast/(self.charge**(1/2)))**self.bsite) * self.kground)/(0.000001))**2))
            return  blast_radio

        def groundvibration_function_ppv(self,blast):

            blast_radio = ((blast/(self.charge**(1/2)))**self.bsite) * self.kground
            return  blast_radio

        
        r1 = [self.receivor1_x, self.receivor1_y]
        r2 = [self.receivor2_x, self.receivor2_y]
        r3 = [self.receivor3_x, self.receivor3_y]
        r4 = [self.receivor4_x, self.receivor4_y]
        r5 = [self.receivor5_x, self.receivor5_y]

        z1 = [np.round(10 * np.log10((((((i/(self.charge**(1/2)))**self.bsite) * self.kground)/(0.000001))**2)),0) 
                       for i in np.arange(1,(self.distance + 1) * np.sqrt(3)) ]

        N = self.distance
        steps = (2*N)//self.grid_size
        x = np.linspace(-N, N, steps+1)
        y = np.linspace(-N, N, steps+1)
        X,Y = np.meshgrid(x,y)

        p = [self.charge_PX_1, self.charge_PY_1]
        R = np.sqrt((((p[0]-X)**2)+((p[1]-Y)**2)))

        if (self.var_ground_ == "dBV"):

            z = 10 * np.log10((((((R/(self.charge**(1/2)))**self.bsite) * self.kground)/(0.000001))**2))
            Z= np.array(z).reshape(len(y),len(x))
            figure_map_vibration = plt.figure(figsize = (5,4), dpi = 110)
            self.figure_map_vibration = figure_map_vibration
            noisemap = figure_map_vibration.add_subplot(111)

            c = noisemap.contourf(X,Y,Z,levels=np.round(np.linspace(40,200,self.color_level+1),1),cmap=cm.jet)
            
            blast_radio_1 = groundvibration_function_dbv(self,self.blast_radio_1)
            blast_radio_2 = groundvibration_function_dbv(self,self.blast_radio_2)
            blast_radio_3 = groundvibration_function_dbv(self,self.blast_radio_3)

            levls = np.array([blast_radio_3,blast_radio_2,blast_radio_1])
            cs_1 = noisemap.contour(X,Y,Z,levels = levls,colors='k',linestyles=('-','-.','--'))
            
            figure_map_vibration.colorbar(c,ax=noisemap).ax.set_title('dBV')

            plt.plot( levls[2],'k--',label=str(np.round(blast_radio_1,0))+' dBV')
            plt.plot( levls[1],'k-.',label=str(np.round(blast_radio_2,0))+' dBV')
            plt.plot( levls[0],'k-',label=str(np.round(blast_radio_3,0))+' dBV')

        elif (self.var_ground_ == "PPV"):

            z = (( R/ (self.charge**(1 / 2)) )**self.bsite) * self.kground
            Z= np.array(z).reshape(len(y),len(x))
            
            levs_1 = [10**n for n in np.arange(np.log10(0.0002), np.log10(20000)+1,9/(self.color_level+1))]

            blast_radio_1 = groundvibration_function_ppv(self,self.blast_radio_1)
            blast_radio_2 = groundvibration_function_ppv(self,self.blast_radio_2)
            blast_radio_3 = groundvibration_function_ppv(self,self.blast_radio_3)
            
            levls_ranges = np.array([blast_radio_3,blast_radio_2,blast_radio_1])

            figure_map_vibration = plt.figure(figsize = (5,4), dpi = 110)
            self.figure_map_vibration = figure_map_vibration
            noisemap = figure_map_vibration.add_subplot(111)
           
            c = noisemap.contourf(X,Y,Z,levels=levs_1,norm=LogNorm(),cmap=cm.jet)
            cs_1 = noisemap.contour(X,Y,Z,levels = levls_ranges,colors='k',linestyles=('-','-.','--'))

            figure_map_vibration.colorbar(c,ax=noisemap,ticks=[0.001, 0.01, 0.1 , 1, 10, 100, 1000, 10000]).ax.set_title('mm/s')
    
            plt.plot(levls_ranges[2],'k--',label=str(np.round(blast_radio_1,1))+' mm/s')
            plt.plot(levls_ranges[1],'k-.',label=str(np.round(blast_radio_2,1))+' mm/s')
            plt.plot(levls_ranges[0],'k-',label=str(np.round(blast_radio_3,1))+' mm/s')
            
        Xflat, Yflat, Zflat = X.flatten(), Y.flatten(), Z.flatten()

        def fmt(x, y):

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
        plt.xlabel('Distance (m)')
        plt.ylabel('Distance (m)',labelpad=0)
        plt.title('Vibration Map')
        plt.scatter(r1[0], r1[1],c='w')
        plt.scatter(r2[0], r2[1],c='w')
        plt.scatter(r3[0], r3[1],c='w')
        plt.scatter(r4[0], r4[1],c='w')
        plt.scatter(r5[0], r5[1],c='w')
        fontP = FontProperties()
        fontP.set_size('x-small')
        plt.legend(loc='upper right', prop=fontP)
        plt.xlim(-N,N)
        plt.ylim(-N,N)
        plt.tick_params(axis='x', labelsize=8)
        plt.tick_params(axis='y', labelsize=8)
        plt.grid(True, which="both", ls="-")
    
        return None
    

    # # FUNCTIONs FOR PLOT GRAPH AND MAP VALUES
    def plot_graph_pressure(self):
        self.graph_pressure()
        self.frame_graph_pressure.destroy()
        frame_graph_pressure=Frame(self.airblast_graph_frame)
        frame_graph_pressure.pack()
        self.frame_graph_pressure=frame_graph_pressure
        chart_graph_pressure = FigureCanvasTkAgg(self.figure_graph_pressure,self.frame_graph_pressure)
        chart_graph_pressure.get_tk_widget().pack()
        toolbar_graph_pressure = NavigationToolbar2Tk(chart_graph_pressure,self.frame_graph_pressure)
        toolbar_graph_pressure.update()
    
        return None
    
   
    def plot_map_pressure(self):
        self.map_pressure()
        self.frame_map_pressure.destroy()
        frame_map_pressure=Frame(self.airblast_map_frame)
        frame_map_pressure.pack()
        self.frame_map_pressure=frame_map_pressure
        chart_map_pressure = FigureCanvasTkAgg(self.figure_map_pressure,self.frame_map_pressure)
        chart_map_pressure.get_tk_widget().pack()
        toolbar_map_pressure = NavigationToolbar2Tk(chart_map_pressure,self.frame_map_pressure)
        toolbar_map_pressure.update()
        chart_map_pressure.get_tk_widget().pack()

        return None

    def plot_graph_vibration(self):
        self.graph_vibration()
        self.frame_graph_vibration.destroy()
        frame_graph_vibration=Frame(self.ground_graph_frame)
        frame_graph_vibration.pack()
        self.frame_graph_vibration=frame_graph_vibration
        chart_graph_vibration = FigureCanvasTkAgg(self.figure_graph_vibration,self.frame_graph_vibration)
        chart_graph_vibration.get_tk_widget().pack()
        toolbar_graph_vibration = NavigationToolbar2Tk(chart_graph_vibration,self.frame_graph_vibration)
        toolbar_graph_vibration.update()
       
        return None

   
    
    def plot_map_vibration(self):
        self.map_vibration()
        self.frame_map_vibration.destroy()
        frame_map_vibration=Frame(self.ground_map_frame)
        frame_map_vibration.pack()
        self.frame_map_vibration=frame_map_vibration
        chart_map_vibration = FigureCanvasTkAgg(self.figure_map_vibration,self.frame_map_vibration)
        chart_map_vibration.get_tk_widget().pack()
        toolbar_map_vibration = NavigationToolbar2Tk(chart_map_vibration,self.frame_map_vibration)
        toolbar_map_vibration.update()
        chart_map_vibration.get_tk_widget().pack()

        return None

    pass
    
main()



