import tkinter as tk      #Importar la biblioteca tkinter para la interfaz gráfica
import random             #Importar random para generar números aleatorios

#Alvarez David _ Tarea 02

# Crear una que permita al usuario adivinar un número aleatorio generado por la aplicación. 
# El usuario tendrá un número limitado de intentos para adivinar correctamente el número, y la aplicación proporcionará 
# retroalimentación en cada intento (si el número es mayor o menor que el número a adivinar).

intentos = 7  #Inicializar intentos
num_aleatorio = random.randint(1, 100)  #Generar un número aleatorio

#Lógica del juego

def verificar_num():  #Función verificar número
    global intentos, num_aleatorio  #Hacer las variables globales
    try:
        num = int(entrada_num.get())  #Obtener el número del campo de entrada
        
        if num < 1 or num > 100:  #Verificar si el número está dentro del rango
            mensaje = "El número debe estar entre 1 y 100\n\n"
        elif num == num_aleatorio:
            mensaje = f"¡Correcto! Has adivinado el número"
            boton_salir.pack(pady=10)
        elif num < num_aleatorio:
            intentos -= 1
            mensaje = f"Demasiado bajo. Intenta con un número más alto\n\n"
        else:
            intentos -= 1
            mensaje = f"Demasiado alto. Intenta con un número más bajo\n\n"

        if intentos == 0:
            mensaje += f" Has agotado tus intentos\n\n El número era {num_aleatorio}"
            boton_validar.config(state=tk.DISABLED, bg="red")  #Desactivar el botón de verificar cuando se agoten los intentos
            boton_reiniciar.pack(pady=10)
        elif num != num_aleatorio:
            mensaje += f" Intentos restantes: {intentos}"

    except ValueError:
        mensaje = "Por favor, ingrese un número"

    #Mostrar mensaje de resultado en la ventana
    resultado.config(text=mensaje)

def reiniciar_juego():      #Reiniciar el juego
    global intentos, num_aleatorio
    intentos = 7
    num_aleatorio = random.randint(1, 100)
    resultado.config(text=f"¡Juego reiniciado!. Tienes {intentos} intentos")
    boton_validar.config(state=tk.NORMAL, bg="green2")  #Volver a activar el botón de verificar
    entrada_num.delete(0, tk.END)  #Limpiar la entrada de número
    boton_reiniciar.pack_forget()  #Ocultar el botón de reiniciar



#Ventana principal número aleatorio

ventana_num = tk.Tk()
ventana_num.title("Adivinar Número Aleatorio")
ventana_num.geometry("501x400")

#Instrucciones
actividad = tk.Label(ventana_num, text="Adivina el número entre 1 y 100", font=("Arial", 14, "bold"))
actividad.pack(pady=10)

etiqueta_instrucciones = tk.Label(ventana_num, text="Ingrese un número:", font=("Arial", 12))
etiqueta_instrucciones.pack(pady=10)

#Entrada para el número
entrada_num = tk.Entry(ventana_num, font=("Arial", 12), width=7)
entrada_num.pack(pady=10)

#Botón verificar número
boton_validar = tk.Button(ventana_num, text="Verificar", command=verificar_num, font=("Arial", 12, "bold"), bg="green2")
boton_validar.pack(pady=10)

#Mostrar el resultado
resultado = tk.Label(ventana_num, text=f"¡Juego iniciado!. Tienes {intentos} intentos", font=("Arial", 12))
resultado.pack(pady=20)

#Botón de reiniciar el juego
boton_reiniciar = tk.Button(ventana_num, text="Reiniciar", command=reiniciar_juego, font=("Arial", 12, "bold"), bg="orange")

#Botón de reiniciar el juego
boton_salir = tk.Button(ventana_num, text="Salir", command=ventana_num.destroy, font=("Arial", 12, "bold"), bg="orange")

ventana_num.mainloop()  # Llamada a mainloop para que la ventana se mantenga activa
