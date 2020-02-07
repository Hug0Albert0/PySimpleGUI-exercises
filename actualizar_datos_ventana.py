import PySimpleGUI as gui
gui.theme("BluePurple")
layout = [
   [gui.Text("Ingresa texto: ")],
   [gui.Input(key = "captura_texto")],
   [gui.Text(size=(50,1), key = "texto_ingresado")],
   [gui.Button("Mostrar"), gui.Button("Salir")]
]
ventana = gui.Window("Actualizacion de datos", layout)
while True:
   evento, valores = ventana.read()
   if evento in [None, "Salir"]:
      break
   if evento == "Mostrar":
      texto = valores["captura_texto"]
      mensaje = f"El texto ingresado fue: {texto}"
      ventana["texto_ingresado"].update(mensaje)
ventana.close()