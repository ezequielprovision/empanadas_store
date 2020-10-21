from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title('Empanadas "LA CUARENTENA"')
        self.state('zoomed') #inicia maximizado
        self.minsize(1920, 1080)

        self.dicc_gustos = {'Carne':0, 'Jamón y Queso':0, 'Verdura':0, 'Humita':0, 'Roquefort':0}

        self.set_background_img()
        self.create_menu()
        self.create_combo()


        self.carrito = ttk.Label(self,width=22, text='Carrito: ')
        self.carrito.place(relx=0.161, rely=0.1)
        self.carrito.config(font=('Calibri', 20, 'bold'), background='#26734d',foreground='#f0f0f0')
        
        self.listado_gustos = ttk.Label(self, width=21, text='Carne\nJamón y Queso\nVerdura\nHumita\nRoquefort' )
        
        self.listado_cantidades = ttk.Label(self, width=2,text='{:2}\n{:2}\n{:2}\n{:2}\n{:2}'.format(
            self.dicc_gustos['Carne'], self.dicc_gustos['Jamón y Queso'], 
            self.dicc_gustos['Verdura'], self.dicc_gustos['Humita'], 
            self.dicc_gustos['Roquefort']
        ))
        
        self.listado_gustos.place(relx=0.161, rely=0.135)
        self.listado_gustos.config(font=('Calibri', 20, 'bold'), background='#ccffff',foreground='#0f0f0f')
        self.listado_cantidades.place(relx=0.306, rely=0.135)
        self.listado_cantidades.config(font=('Calibri', 20, 'bold'), background='#0f0f0f',foreground='#f0f0f0')

        self.pedir_datos()

    """
    STYLE ###################################################
    """

    def set_background_img(self):
        bg_img = Canvas(self)
        bg_img.pack(expand=YES, fill=BOTH)

        img = Image.open('emp_bg.jpg')
        bg_img.image = ImageTk.PhotoImage(img)
        bg_img.create_image(0, 0, image=bg_img.image, anchor='nw')
        bg_img.pack()


    def create_combo(self):
        self.eleccion = StringVar()
        self.opciones = ttk.Combobox(self, width=22, textvariable=self.eleccion)
        self.opciones['values'] = ('Carne', 'Jamón y Queso', 'Verdura', 'Humita', 'Roquefort')
        self.opciones.place(relx=0.19, rely=0.43)

        self.accion_label = ttk.Label(self, width=15, text='Añade a tu pedido')
        self.accion_label.place(relx=0.19, rely=0.4)
        self.accion_label.config(font=('Calibri', 14, 'normal'), background='#26734d',foreground='#f0f0f0')
        

        self.boton_agregar = ttk.Button(self, width=24 ,text='Agregar', command= self.agregar)
        self.boton_agregar.place(relx=0.19, rely=0.45)
        
        self.boton_quitar = ttk.Button(self, width=24 ,text='Quitar', command= self.quitar)
        self.boton_quitar.place(relx=0.19, rely=0.48)

        self.boton_finalizar = ttk.Button(self, width=50, text= 'Confirmar Pedido', command= self.finalizar_pedido)
        self.boton_finalizar.place(relx=0.161, rely=0.31)
        #self.boton_agregar.configure()


    def pedir_datos(self):

        self.nombre = StringVar()        
        self.direccion = StringVar()
        self.telefono = StringVar()

        """
        nombre:
        """

        self.nombre_titulo = ttk.Label(self, text='Nombre')
        self.nombre_titulo.place(relx=0.8, rely=0.1)
        """
        self.box_nombre = ttk.Entry(self, width=20, textvariable= self.nombre)
        self.box_nombre.grid(column= 0, row= 1)
        self.box_nombre.focus() #donde comienza el cursor

        self.boton_confirmar1 = ttk.Button(self, text='Confirmar')
        self.boton_confirmar1.grid(column= 0, row= 2)

        
        direccion:
        
        self.direccion_titulo = ttk.Label(self, text='Dirección')
        self.direccion_titulo.grid(column= 0, row= 4)

        self.box_direccion = ttk.Entry(self, width=20, textvariable= self.direccion)
        self.box_direccion.grid(column= 0, row= 5)
        
        self.boton_confirmar2 = ttk.Button(self, text='Confirmar', command = self.click_me)
        self.boton_confirmar2.grid(column= 0, row= 6)


        
        telefono
        
        self.tel_titulo = ttk.Label(self, text='Teléfono')
        self.tel_titulo.grid(column= 0, row= 8)

        self.box_tel = ttk.Entry(self, width=20, textvariable= self.nombre)
        self.box_tel.grid(column= 0, row= 9)
        self.box_tel.focus() #donde comienza el cursor

        self.boton_confirmar3 = ttk.Button(self, text='Confirmar', command = self.click_me)
        self.boton_confirmar3.grid(column= 0, row= 10)
        """


    def create_menu(self):
        menuBar = Menu(self)
        self.config(menu = menuBar)

        file_menu = Menu(menuBar, tearoff=0)                
        menuBar.add_cascade(label= 'Archivo', menu= file_menu) 
        file_menu.add_command(label = 'Abrir')
        file_menu.add_command(label= 'Guardar')
        file_menu.add_separator()                                  
        file_menu.add_command(label= 'Salir', command= self.window_close)


    """
    COMMANDS ####################################################
    """

    def agregar(self):
        self.dicc_gustos[self.eleccion.get()] += 1
        self.listado_cantidades.configure(text='{:2}\n{:2}\n{:2}\n{:2}\n{:2}'.format(
            self.dicc_gustos['Carne'], self.dicc_gustos['Jamón y Queso'], 
            self.dicc_gustos['Verdura'], self.dicc_gustos['Humita'], 
            self.dicc_gustos['Roquefort']
        ))

    def quitar(self):
        resta = self.eleccion.get()
        if self.dicc_gustos[resta] > 0:
            self.dicc_gustos[resta] -= 1
            self.listado_cantidades.configure(text='{:2}\n{:2}\n{:2}\n{:2}\n{:2}'.format(
                self.dicc_gustos['Carne'], self.dicc_gustos['Jamón y Queso'], 
                self.dicc_gustos['Verdura'], self.dicc_gustos['Humita'], 
                self.dicc_gustos['Roquefort']
            ))
    
    def finalizar_pedido(self):
        self.confirmar_wn = Tk()
        self.confirmar_wn.minsize(500, 400)
        self.confirmar_wn.title('Complete los siguientes Datos')


    def window_close(self):
        self.quit()
        self.destroy()
        exit()



class ConfirmarDatos(Tk):
    def __init__(self):
        super(ConfirmarDatos, self).__init__()

        self.title('Complete los siguientes datos')
        self.minsize(500, 400)

    def pedir_datos(self):

        self.nombre = StringVar()        
        self.direccion = StringVar()
        self.telefono = StringVar()

        """
        nombre:
        """

        self.nombre_titulo = ttk.Label(self, text='Nombre')
        self.nombre_titulo.grid(column= 0, row= 0)

        self.box_nombre = ttk.Entry(self, width=20, textvariable= self.nombre)
        self.box_nombre.grid(column= 0, row= 1)
        self.box_nombre.focus() #donde comienza el cursor

        self.boton_confirmar1 = ttk.Button(self, text='Confirmar')
        self.boton_confirmar1.grid(column= 0, row= 2)

        """
        direccion:
        """
        self.direccion_titulo = ttk.Label(self, text='Dirección')
        self.direccion_titulo.grid(column= 0, row= 4)

        self.box_direccion = ttk.Entry(self, width=20, textvariable= self.direccion)
        self.box_direccion.grid(column= 0, row= 5)
        
        self.boton_confirmar2 = ttk.Button(self, text='Confirmar', command = self.click_me)
        self.boton_confirmar2.grid(column= 0, row= 6)


        """
        telefono
        """
        self.tel_titulo = ttk.Label(self, text='Teléfono')
        self.tel_titulo.grid(column= 0, row= 8)

        self.box_tel = ttk.Entry(self, width=20, textvariable= self.nombre)
        self.box_tel.grid(column= 0, row= 9)
        self.box_tel.focus() #donde comienza el cursor

        self.boton_confirmar3 = ttk.Button(self, text='Confirmar', command = self.click_me)
        self.boton_confirmar3.grid(column= 0, row= 10)




wn = Window()
wn.mainloop()

