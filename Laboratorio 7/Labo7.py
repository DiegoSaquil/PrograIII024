import serial
import tkinter as tk
import threading

# Configuración del puerto serial, cambia el puerto y la velocidad según tu configuración de Arduino
ser = serial.Serial('COM3', 9600)

# Variable global para el texto del potenciómetro
pot_label_text = None
pot_value_text = None

# Función para leer datos del puerto serie en un hilo separado
def serial_reader():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if data:
                handle_code(data)

# Función para encender un círculo
def turn_on_circle(circle, color):
    canvas.itemconfig(circle, fill=color)

# Función para apagar un círculo
def turn_off_circle(circle):
    canvas.itemconfig(circle, fill="linen")

# Función para manejar los datos recibidos del puerto serie
def handle_code(code):
    try:
        digit = int(code)
        print("Arduino:", digit)
        # Apagar todos los círculos primero
        for circle in circles:
            turn_off_circle(circle)

        # Encender el círculo correspondiente al código recibido
        if digit == 2:
            turn_on_circle(circles[0], "green")
        elif digit == 4:
            turn_on_circle(circles[1], "yellow")
        elif digit == 6:
            turn_on_circle(circles[2], "red")
        # Actualizar el valor de la barra de potenciómetro
        update_bar_graph(digit)
    except ValueError:
        print("Arduino:", code)

# Función para actualizar la barra de potenciómetro
def update_bar_graph(value):
    # Normalizar el valor para que esté en el rango de 0 a 1 (Tkinter no acepta valores fuera de este rango)
    normalized_value = value / 1023
    # Calcular las coordenadas de la barra
    x0 = 50
    y0 = 450 - normalized_value * 400  # Aumentar la altura de la barra
    x1 = 100
    y1 = 450
    # Actualizar las coordenadas y el color de la barra
    canvas.coords(bar, x0, y0, x1, y1)
    # Actualizar el texto del potenciómetro
    canvas.itemconfig(pot_value_text, text=f"{value}")
    # Mover el texto a la izquierda de la barra sin cambiar su posición vertical
    canvas.coords(pot_value_text, 75, 460)  # Ajustar posición debajo de la barra

# Configuración de la ventana de Tkinter con un tamaño más grande
root = tk.Tk()
root.title("Dashboard segundo parcial")
root.geometry("700x600")  # Disminuir el tamaño del dashboard

# Configuración de la gráfica de barras con fondo bisque y tamaño más grande
canvas = tk.Canvas(root, width=500, height=500, bg='bisque')  # Cambio de color de fondo y disminución del tamaño del lienzo
canvas.pack()
bar = canvas.create_rectangle(30, 50, 80, 450, fill='orange')  # Rectángulo que representa la barra de potenciómetro

# Rectángulo dorado alrededor de la palabra "Potenciómetro"
pot_label_rect = canvas.create_rectangle(10, 10, 120, 40, fill='gold')
canvas.tag_lower(pot_label_rect)  # Mover el rectángulo detrás del texto

# Texto del potenciómetro
pot_label_text = canvas.create_text(65, 25, text="Potenciómetro", font=("Comic Sans MS", 12, "bold"), anchor=tk.CENTER)
pot_value_text = canvas.create_text(75, 460, text="0", font=("Comic Sans MS", 10, "bold"), anchor=tk.CENTER)

# Mover los círculos hacia la derecha
circle_start_x = 200
circle_spacing = 100

circles = []
for i in range(3):
    circle = canvas.create_oval(circle_start_x + i * circle_spacing, 200, circle_start_x + 50 + i * circle_spacing, 250, outline="black", width=2)  # Ajustar la posición de los círculos
    canvas.create_text(circle_start_x + 25 + i * circle_spacing, 275, text=str(i+1), font=("Comic Sans MS", 12, "bold"))  # Ajustar la posición del texto
    circles.append(circle)

# Crear y colocar rectángulos dark turquoise alrededor de las palabras "PreOrden", "InOrden" y "PostOrden"
rect_width = 100
rect_height = 20
rect_spacing = 100
rect_start_y = 310

preorder_rect = canvas.create_rectangle(circle_start_x - 25, rect_start_y, circle_start_x + rect_width - 25, rect_start_y + rect_height, fill='dark turquoise')
inorder_rect = canvas.create_rectangle(circle_start_x + rect_spacing - 25, rect_start_y, circle_start_x + rect_spacing + rect_width - 25, rect_start_y + rect_height, fill='dark turquoise')
postorder_rect = canvas.create_rectangle(circle_start_x + 2 * rect_spacing - 25, rect_start_y, circle_start_x + 2 * rect_spacing + rect_width - 25, rect_start_y + rect_height, fill='dark turquoise')

# Texto "PreOrden", "InOrden" y "PostOrden" dentro de los rectángulos
canvas.create_text(circle_start_x + rect_width / 2 - 25, rect_start_y + rect_height / 2, text="PreOrden", font=("Comic Sans MS", 10, "bold"), fill="white")
canvas.create_text(circle_start_x + rect_spacing + rect_width / 2 - 25, rect_start_y + rect_height / 2, text="InOrden", font=("Comic Sans MS", 10, "bold"), fill="white")
canvas.create_text(circle_start_x + 2 * rect_spacing + rect_width / 2 - 25, rect_start_y + rect_height / 2, text="PostOrden", font=("Comic Sans MS", 10, "bold"), fill="white")

# Crear y ejecutar el hilo para leer datos del puerto serie
serial_thread = threading.Thread(target=serial_reader)
serial_thread.daemon = True
serial_thread.start()

# Ejecutar la aplicación Tkinter
root.mainloop()