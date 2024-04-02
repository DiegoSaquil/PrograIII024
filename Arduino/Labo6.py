import tkinter as tk
import serial
import threading

# Inicializar la comunicación serial con Arduino
arduino = serial.Serial('COM3', 9600)  # Reemplaza 'puerto_serial_de_arduino' con el puerto correcto

# Función para procesar los datos recibidos de Arduino
def procesar_datos(datos):
    print("Datos recibidos desde Arduino:", datos.decode().strip())

# Función para enviar comandos a Arduino
def enviar_comando(comando):
    arduino.write(comando.encode())

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Dashboard Creativo")
ventana.geometry("600x400")  # Tamaño personalizado de la ventana
ventana.configure(bg='#1e212d')  # Color de fondo gris oscuro

# Estilo para los botones
estilo_boton = {
    'font': ('Arial', 14),
    'width': 15,
    'height': 2,
    'bg': '#ff6b6b',  # Color de fondo rojo claro
    'fg': 'white',  # Color del texto
    'activebackground': '#d63031',  # Color de fondo cuando se presiona rojo oscuro
    'activeforeground': 'white',  # Color del texto cuando se presiona
    'bd': 0,  # Grosor del borde
    'highlightthickness': 0,  # Grosor del resaltado
}

# Creación de widgets personalizados
titulo_label = tk.Label(ventana, text="Control de LEDs", font=('Arial', 24), fg='#f9ca24', bg='#1e212d')
titulo_label.pack(pady=20)

# Contenedor para los botones de encendido
frame_encendido = tk.Frame(ventana, bg='#1e212d')
frame_encendido.pack(pady=10)

# Contenedor para los botones de apagado
frame_apagado = tk.Frame(ventana, bg='#1e212d')
frame_apagado.pack(pady=10)

# Ejemplo de creación de botones con el estilo aplicado y empaquetado horizontalmente
boton_A = tk.Button(frame_encendido, text="Encender grupo 1", command=lambda: enviar_comando('A'), **estilo_boton)
boton_A.pack(side=tk.LEFT, padx=10)

boton_B = tk.Button(frame_encendido, text="Encender grupo 2", command=lambda: enviar_comando('B'), **estilo_boton)
boton_B.pack(side=tk.LEFT, padx=10)

boton_C = tk.Button(frame_encendido, text="Encender grupo 3", command=lambda: enviar_comando('C'), **estilo_boton)
boton_C.pack(side=tk.LEFT, padx=10)

boton_D = tk.Button(frame_encendido, text="Encender grupo 4", command=lambda: enviar_comando('D'), **estilo_boton)
boton_D.pack(side=tk.LEFT, padx=10)

boton_E = tk.Button(frame_apagado, text="Apagar grupo 1", command=lambda: enviar_comando('E'), **estilo_boton)
boton_E.pack(side=tk.LEFT, padx=10)

boton_F = tk.Button(frame_apagado, text="Apagar grupo 2", command=lambda: enviar_comando('F'), **estilo_boton)
boton_F.pack(side=tk.LEFT, padx=10)

boton_G = tk.Button(frame_apagado, text="Apagar grupo 3", command=lambda: enviar_comando('G'), **estilo_boton)
boton_G.pack(side=tk.LEFT, padx=10)

boton_H = tk.Button(frame_apagado, text="Apagar grupo 4", command=lambda: enviar_comando('H'), **estilo_boton)
boton_H.pack(side=tk.LEFT, padx=10)

# Bucle principal para recibir y procesar datos de Arduino
def leer_datos_desde_arduino():
    while True:
        datos = arduino.readline()
        if datos:
            procesar_datos(datos)

# Crear un hilo para leer datos de Arduino en segundo plano
thread_arduino = threading.Thread(target=leer_datos_desde_arduino)
thread_arduino.start()

# Iniciar el bucle de la interfaz de usuario
ventana.mainloop()
