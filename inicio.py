import tkinter as Ventana 

class Formulario:


 def __init__(self): 
    self.ventana_formulario = Ventana.Tk() 
    self.label_nombre  = Ventana.Label(self.ventana_formulario, text="digite el nombre: ") 
    self.entry_nombre = Ventana.Entry(self.ventana_formulario) 
    self.boton_enviar  = Ventana.Button(self.ventana_formulario, text="Guardar Cliente", command=self.tomar_datos()) 
    self.boton_limpiar = Ventana.Button(self.ventana_formulario, text="limpiar", command =lambda: self.evento_borrar()) 
    self.label_nombre.grid(row=0 , column=0) 
    self.entry_nombre.grid(row=0 , column=1) 
    self.boton_enviar.grid(row=0 , column=2) 
    self.boton_limpiar.pack(row=0 , colum = 3) 
    self.ventana_formulario.mainloop()



def tomar_datos (self): 
   print("se tomaron los datos") 


def evento_borrar(self): 
  self.entry_nombre.delete(0, 'end') 
  print("campos borrados...") 




obj_formulario = Formulario()  