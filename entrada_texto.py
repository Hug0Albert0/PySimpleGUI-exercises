import PySimpleGUI as simple_gui

simple_gui.theme("DarkBlue1")

layout = [
   [simple_gui.Text("Entrada de Texto.")],
   [simple_gui.InputText()],
   [simple_gui.Submit(), simple_gui.Cancel()]
]

ventana = simple_gui.Window("Mi ventana", layout)

evento, valores = ventana.read()

ventana.close()

texto_ingresado = valores[0]

simple_gui.popup("Texto ingresado: ", texto_ingresado)