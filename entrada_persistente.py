#By Hug0Albert0
#pip3 install pysimplegui
import PySimpleGUI as gui
gui.theme("DarkAmber") #Tema para Look & Feel. Lista completa => gui.theme_list().
layout = [
   [gui.Text("Ingresa un numero")],
   [gui.Input(key = "entrada_numero")], #Identificador para el valor del input.
   [gui.Button("Leer"), gui.Exit("Salir")] #Declaracion de botones y el nombre de sus eventos.
]
ventana = gui.Window("Ventana persistente", layout) #Creamos una ventana con un titulo y un layout

#Esta parte indica el bucle del comportamiento de la ventana.
while True:
   evento, valores = ventana.read() #Asignamos eventos y valores como la respuesta de lectura
   if evento in [None, "Salir"]: #Si el evento es "Salir", termina la ejecución con break
      break
   valor_ingresado = valores["entrada_numero"]
   if valor_ingresado.isnumeric():
      gui.popup(f"""
         El número registrado es {valor_ingresado}. Gracias por darme un número válido"""
      )
      break
   else:
      gui.popup("Ingresa un número válido")
ventana.close()