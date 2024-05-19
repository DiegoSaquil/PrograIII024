import serial
import tkinter as tk
from tkinter import PhotoImage

# Configurar la conexión serial
ser = serial.Serial('COM3', 9600)

# Configurar la ventana principal
root = tk.Tk()
root.title("Creative Control Dashboard")
root.configure(bg='black')

# Configurar el tamaño y la posición de la ventana
ancho_ventana = 400
alto_ventana = 400
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = (alto_pantalla - alto_ventana) // 2
root.geometry(f'{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}')

# Etiqueta de título con fuente personalizada y estilo
titulo_label = tk.Label(root, text="Control de Dispositivos", bg='black', fg='cyan', font=('Helvetica', 18, 'bold'))
titulo_label.pack(pady=20)

# Crear un marco para los botones con un diseño circular
frame_botones = tk.Frame(root, bg='black')
frame_botones.pack(expand=True)

# Función para enviar comandos a través de la conexión serial
def enviar_comando(comando):
    ser.write(comando.encode())

# Función para manejar el evento de presionar un botón
def boton_presionado(comando):
    enviar_comando(comando)

# Crear y configurar los botones con estilos personalizados
botonStepper = tk.Button(frame_botones, text="Iniciar Stepper", command=lambda: boton_presionado('1'), bg='blue', fg='white', font=('Helvetica', 12, 'bold'), padx=20, pady=10)
botonStepper.grid(row=0, column=0, padx=50, pady=20)

botonServo = tk.Button(frame_botones, text="Iniciar Servo", command=lambda: boton_presionado('2'), bg='green', fg='white', font=('Helvetica', 12, 'bold'), padx=20, pady=10)
botonServo.grid(row=0, column=1, padx=50, pady=20)

# Texto explicativo debajo de los botones
texto_explicativo = tk.Label(root, text="Haz clic en un botón para iniciar el dispositivo", bg='black', fg='white', font=('Helvetica', 10, 'italic'))
texto_explicativo.pack(side=tk.BOTTOM, pady=20)

# Iniciar el bucle principal de la aplicación
root.mainloop()
