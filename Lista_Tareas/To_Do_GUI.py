import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import messagebox

class Lista_de_Tareas:

    tareas = []

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista de Tareas")
        self.ventana.geometry("400x350")
        self.ventana.configure(bg='LightSkyBlue')

        self.menu_principal()


    def menu_principal(self):
        fuente_personalizada = tkfont.Font(family="Arial", size=16, weight="bold")

        title = tk.Label(self.ventana,text="Lista de Tareas",font=fuente_personalizada,background='LightSkyBlue')
        tarea_entrada = tk.Entry(self.ventana,width=60)
        btt_agregar  = tk.Button(self.ventana,text="Agregar Una Tarea",background='SlateBlue',width=18,command=lambda: self.agregar(tarea_entrada))
        btt_completar = tk.Button(self.ventana,text="Completar Una Tarea",background='SlateBlue',width=18,command= self.completar)
        btt_eliminar = tk.Button(self.ventana,text="Eliminar Una Tarea",background='SlateBlue',width=18,command=self.eliminar)
        btt_mostrar = tk.Button(self.ventana,text="Mostrar Tareas",background='SlateBlue',width=18,command=self.mostrar)

        title.place(x=120,y=50)
        tarea_entrada.place(x=20,y=90)
        btt_agregar.place(x=140,y=150)
        btt_completar.place(x=140,y=190)
        btt_eliminar.place(x=140,y=230)
        btt_mostrar.place(x=140,y=270)

    def agregar(self,tarea):
        self.tareas.append({'Desc': tarea.get(), 'Estado': False})
        tarea.delete(0, tk.END)
        messagebox.showinfo("Alerta", "Tarea Ingresada con éxito.")

    def completar(self):
        self.ventana.withdraw()
        ventana_2 = tk.Toplevel()
        ventana_2.title("Lista de Tareas")
        ventana_2.geometry("400x350")
        ventana_2.configure(bg='LightSkyBlue')

        if not self.tareas :
            messagebox.showerror("Error", "No hay Tareas por Mostrar")
            ventana_2.withdraw()
            self.ventana.deiconify()
        else:
            fuente_personalizada = tkfont.Font(family="Arial", size=16, weight="bold")

            title = tk.Label(ventana_2,text="Lista de Tareas",font=fuente_personalizada,background='LightSkyBlue')
            self.combo_tareas = ttk.Combobox(ventana_2,values=self.Buscar_tareas(False),width=55,state='readonly')
            btn_completar = tk.Button(ventana_2,text='Completar Tarea',background='SlateBlue',width=18,command=lambda: self.completar_1())
            btn_volver = tk.Button(ventana_2,text='Volver',background='SlateBlue',width=18,command=lambda: self.volver(ventana_2))


            title .place(x=120,y=50)
            self.combo_tareas.place(x=20,y=90)
            btn_completar.place(x=140,y=130)
            btn_volver.place(x=140,y=170)
    
    def completar_1(self):
        for tarea in self.tareas:
            if tarea['Desc'] == self.combo_tareas.get():
                tarea['Estado'] = True
        messagebox.showinfo("Alerta", "Tarea Completada con éxito.") 
    
    def volver(self,ventana_2):
        ventana_2.withdraw()
        ventana_2.destroy()
        self.ventana.deiconify()

    def Buscar_tareas(self,estado):
        a = []
        for tarea in self.tareas:
            if tarea['Estado'] == estado:
                a.append(tarea['Desc'])
        return a
    
    def eliminar(self):

        self.ventana.withdraw()
        ventana_2 = tk.Toplevel()
        ventana_2.title("Lista de Tareas")
        ventana_2.geometry("400x350")
        ventana_2.configure(bg='LightSkyBlue')

        if not self.tareas :
            messagebox.showerror("Error", "No hay Tareas por Mostrar")
            ventana_2.withdraw()
            self.ventana.deiconify()
        else:

            fuente_personalizada = tkfont.Font(family="Arial", size=16, weight="bold")

            title = tk.Label(ventana_2,text="Lista de Tareas",font=fuente_personalizada,background='LightSkyBlue')
            combo_tareas = ttk.Combobox(ventana_2,values=self.Mostrar_tareas(),width=55,state='readonly')
            btn_completar = tk.Button(ventana_2,text='Eliminar Tarea',background='SlateBlue',width=18,command=lambda: self.eliminar_1(combo_tareas))
            btn_volver = tk.Button(ventana_2,text='Volver',background='SlateBlue',width=18,command=lambda: self.volver(ventana_2))


            title .place(x=120,y=50)
            combo_tareas.place(x=20,y=90)
            btn_completar.place(x=140,y=130)
            btn_volver.place(x=140,y=170)
    
    def eliminar_1(self,tarea):
        a = tarea.get().split()
        a.pop(len(a)-1)
        a = ' '.join(a) 
        for pos,x in enumerate(self.tareas):
            if x['Desc'] == a:
                self.tareas.pop(pos) 
                messagebox.showinfo("Alerta", "Tarea Eliminada con éxito.")     

    def mostrar(self):
        self.ventana.withdraw()
        ventana_2 = tk.Toplevel()
        ventana_2.title("Lista de Tareas")
        ventana_2.geometry("400x350")
        ventana_2.configure(bg='LightSkyBlue')

        if not self.tareas :
            messagebox.showerror("Error", "No hay Tareas por Mostrar")
            ventana_2.withdraw()
            self.ventana.deiconify()
        else:
            fuente_personalizada = tkfont.Font(family="Arial", size=16, weight="bold")

            title = tk.Label(ventana_2,text="Lista de Tareas",font=fuente_personalizada,background='LightSkyBlue')
            text_widget = tk.Text(ventana_2, width=30, height=7)
            btn_mostrar = tk.Button(ventana_2,text='Mostrar Lista',background='SlateBlue',width=18,command=lambda: self.Mostrar_tareas_2(text_widget))
            btn_volver = tk.Button(ventana_2,text='Volver',background='SlateBlue',width=18,command=lambda: self.volver(ventana_2))


            title .place(x=120,y=50)
            
            text_widget.place(x=80,y=90)
            btn_mostrar.place(x=140,y=220)
            btn_volver.place(x=140,y=260)
    
    def Mostrar_tareas(self):
        a = []
        str_out = ''
        for b in self.tareas:
            desc = b['Desc']
            if b['Estado'] == False:
                str_out=f'{desc}  Pendiente'
                a.append(str_out)
            else:
                str_out=f'{desc}  Completada'
                a.append(str_out)

        return a    

    def Mostrar_tareas_2(self,text_widget):
        
        text_widget.delete('1.0', 'end')

        a = []
        str_out = ''
        for b in self.tareas:
            desc = b['Desc']
            if b['Estado'] == False:
                str_out=f'{desc}  Pendiente \n'
                text_widget.insert('end', str_out)
            else:
                str_out=f'{desc}  Completada\n'
                text_widget.insert('end', str_out)

            
    
if __name__ == "__main__":
    ventana = tk.Tk()
    app = Lista_de_Tareas(ventana)
    ventana.mainloop()
