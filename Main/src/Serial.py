import serial
import crudSqlite as crud
import tkinter as tk
from tkinter import ttk
import threading

# Eliminamos la configuración del puerto COM2
puerto_com2 = serial.Serial('COM7', baudrate=9600, timeout=1)

# Variable de estado para verificar si la ventana ha sido cerrada
ventana_cerrada = False
# Variable de estado para verificar el modo puerto o modo terminal
estado_booleano = False

# Variables para la obtencion de datos
tempDHT1_global = 0.0
hum1_global = 0.0
tempDHT2_global = 0.0
hum2_global = 0.0
tempDHT3_global = 0.0
hum3_global = 0.0
lm75_global = 0.0

# Función para manejar el cierre de la ventana
def cerrar_ventana():
    global ventana_cerrada
    ventana_cerrada = True
    root.destroy()

# Función para enviar un mensaje con una nueva línea
def enviar_mensaje(event=None):
    mensaje = entrada_texto.get()
    
    if estado_booleano == True:
        puerto_com2.write(mensaje.encode())
    
    if mensaje.lower() == 'cls':
        limpiar_terminal()
    elif mensaje.lower() == 'send':
        cargar_datos()
    elif mensaje.lower() == 'update':
        actualizar_datos()
    elif mensaje.lower() == 'mode':
        cambiar_estado_booleano()
    elif mensaje.lower() == 'drop':
        eliminar_registro()
    else:
        # Muestra el mensaje en la terminal
        texto_terminal.config(state=tk.NORMAL)
        texto_terminal.insert(tk.END, f"{mensaje}\n")
        texto_terminal.config(state=tk.DISABLED)
        texto_terminal.see(tk.END)
    
    # Limpiar la caja de entrada después de enviar el mensaje
    entrada_texto.delete(0, tk.END)

    
# Función para limpiar la terminal
def limpiar_terminal(event=None):  # La función puede ser llamada directamente o como respuesta a un evento
    texto_terminal.config(state=tk.NORMAL)
    texto_terminal.delete("1.0", tk.END)
    texto_terminal.config(state=tk.DISABLED)
    
#Funcion para enviar los datos a la base de datos 
def cargar_datos():
    
    if crud.hasRecords():
        mensaje = "Ya existen los datos"
    else:
        crud.insertData(1,tempDHT1_global, hum1_global, tempDHT2_global, hum2_global, tempDHT3_global, hum3_global, lm75_global)
        mensaje = "Se cargaron los datos"
    texto_terminal.config(state=tk.NORMAL)
    texto_terminal.insert(tk.END,f"{mensaje}\n")
    texto_terminal.config(state=tk.DISABLED)
    texto_terminal.see(tk.END)
    
def actualizar_datos():
    crud.updateData(1,tempDHT1_global, hum1_global, tempDHT2_global, hum2_global, tempDHT3_global, hum3_global, lm75_global)
    mensaje = "Se actualizaron los datos"
    texto_terminal.config(state=tk.NORMAL)
    texto_terminal.insert(tk.END,f"{mensaje}\n")
    texto_terminal.config(state=tk.DISABLED)
    texto_terminal.see(tk.END)

def eliminar_registro():
    crud.cleanData()
    mensaje = "Se eliminaron los datos"
    texto_terminal.config(state=tk.NORMAL)
    texto_terminal.insert(tk.END,f"{mensaje}\n")
    texto_terminal.config(state=tk.DISABLED)
    texto_terminal.see(tk.END)

def cambiar_estado_booleano():
    global estado_booleano
    estado_booleano = not estado_booleano  # Cambia el valor a su opuesto

    mensaje = f"El estado booleano ahora es: {estado_booleano}"
    texto_terminal.config(state=tk.NORMAL)
    texto_terminal.insert(tk.END, f"{mensaje}\n")
    texto_terminal.config(state=tk.DISABLED)
    texto_terminal.see(tk.END)
    
    
    
# Función para leer datos y mostrarlos en la interfaz
def leer_datos():
    global ventana_cerrada
    # Creamos una variable lista para almacenar valores de las temperaturas
    datos = []
    # Inicializamos las variables en global
    global tempDHT1_global, hum1_global, tempDHT2_global, hum2_global, tempDHT3_global, hum3_global, lm75_global
    while not ventana_cerrada:
        # Simulamos la lectura de datos del COM1 (puedes adaptar esta parte según tus necesidades)
        if estado_booleano:
            respuesta = puerto_com2.readline().decode().strip()
            datos = respuesta.split(",")
            if len(datos) == 7:
                tempDHT1_global = float(datos[0])
                hum1_global = float(datos[1])
                tempDHT2_global = float(datos[2])
                hum2_global = float(datos[3])
                tempDHT3_global = float(datos[4])
                hum3_global = float(datos[5])
                lm75_global = float(datos[6])
                
                # Poner un espaciado antes de mostrar las temperaturas
                limpiar_terminal()
                
                for i, dato in enumerate(datos):
                    if i % 2 == 0:
                        tipo_sensor = "Temperatura"
                    else:
                        tipo_sensor = "Humedad"
                    
                    unidad = "ºC" if i % 2 == 0 else "%"
                    
                    texto = f"{tipo_sensor} DHT11: {dato} {unidad}" if i != 6 else f"Temperatura LM75: {dato} ºC"
                    
                    texto_terminal.config(state=tk.NORMAL)
                    texto_terminal.insert(tk.END, f"{texto}\n")
                    texto_terminal.config(state=tk.DISABLED)
                    texto_terminal.see(tk.END) 
                    crud.updateData(1,tempDHT1_global, hum1_global, tempDHT2_global, hum2_global, tempDHT3_global, hum3_global, lm75_global)
            
            else:
                # Caso para otros tipos de mensajese
                texto_terminal.config(state=tk.NORMAL)
                texto_terminal.insert(tk.END, f"{respuesta}")
                texto_terminal.config(state=tk.DISABLED)
                texto_terminal.see(tk.END)
                
        root.update()
        
# Función que inicia el hilo para leer datos
def iniciar_lectura():
    hilo_lectura = threading.Thread(target=leer_datos)
    hilo_lectura.start()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Terminal Virtual")

# Configura la función para manejar el cierre de la ventana
root.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Área de texto para mostrar los mensajes
texto_terminal = tk.Text(root, height=15, width=60, state=tk.DISABLED)
texto_terminal.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Caja de entrada de texto
entrada_texto = ttk.Entry(root, width=80)
entrada_texto.grid(row=1, column=0, padx=10, pady=10)
#Al presionar return(Enter) se ejecuta la funcion enviar_mensaje
entrada_texto.bind('<Return>', enviar_mensaje)
#apuntar el cusor a la entrada de texto
entrada_texto.focus_set()


# Botón para enviar mensajes
# boton_enviar = ttk.Button(root, text="Enviar", command=enviar_mensaje)
# boton_enviar.grid(row=1, column=1, padx=10, pady=10)

# Inicia el hilo de lectura automáticamente
iniciar_lectura()


# Inicia el bucle principal de la interfaz gráfica
root.mainloop()
