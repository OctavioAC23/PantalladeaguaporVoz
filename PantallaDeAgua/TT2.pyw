import tkinter as tk
import serial
import time
import sys
import threading
import speech_recognition as sr
# Diccionario de palabras a números
numeros = {
    "cero": 0,
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
}

# Tu función para enviar la matriz a_shape al Arduino
def enviar_matriz(letra):
    try:
        # Importa todas las letras o números desde BANCO
        from BANCO import letras,numeros

        # Busca la letra o número en el diccionario
        if letra in letras:
            data = letras[letra]
            print(f'ENVIANDO"{letra}".')
            for fila in data:
                secuencia = ''.join(map(str, fila))  # Convierte la fila en una cadena binaria de 8 bits
                ser.write(secuencia.encode())
                time.sleep(0.05) 
        elif letra in numeros:
            data = numeros[letra]
            print(f'ENVIANDO"{letra}".')
            for fila in data:
                secuencia = ''.join(map(str, fila))  # Convierte la fila en una cadena binaria de 8 bits
                ser.write(secuencia.encode())
                time.sleep(0.05) 
        else:
            print(f'La letra o número "{letra}" no se encuentra en el archivo BANCO.')
    except ImportError:
        print(f'No se pudo importar el archivo BANCO.')

# Tu función para realizar acciones basadas en el texto capturado
def realizar_acciones(text):
    parts = text.split(" ")  # Dividir el texto en partes usando un espacio en blanco como separador

    if len(parts) >= 2:
        Peticion = parts[0]
        imp = parts[1]
        if len(parts)>2:
            imp = imp.replace("las",parts[2])
            imp = imp.replace("los",parts[2])
            imp = imp.replace("el",parts[2])
            imp = imp.replace("la",parts[2])
        print(f'Peticion: {Peticion}, imp: {imp}')
        if Peticion == 'muestrame' or Peticion == 'enseñame' or Peticion =='Muéstrame' or Peticion =='Dime' or Peticion =='dime':
            if imp == 'vocales':
                letras = ['a', 'e', 'i', 'o', 'u']
                for letra in letras:
                    time.sleep(1) 
                    enviar_matriz(letra)
            if imp == 'numeros' or imp == 'números' or Peticion =='Dime' or Peticion =='dime':
                letras = [0,1,2,3,4,5,6,7,8,9]
                for letra in letras:
                    time.sleep(1) 
                    enviar_matriz(letra)
            if imp == 'alfabeto':
                letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                for letra in letras:
                    time.sleep(1) 
                    enviar_matriz(letra)
        elif Peticion == 'suma' or Peticion == 'Suma':
            Primernumero = int(parts[1])
            SegundoNumero = int(parts[3])
            resultado = Primernumero + SegundoNumero
            if resultado < 10:
                letras=[Primernumero,'+',SegundoNumero,'=',resultado]
            else:
                primero = resultado // 10
                segundo = resultado % 10
                letras=[Primernumero,'+',SegundoNumero,'=',primero,segundo]    
            for letra in letras:
                    time.sleep(1) 
                    enviar_matriz(letra)
        elif Peticion == 'Cuenta' or Peticion == 'cuenta' or Peticion == 'cuentame' or Peticion == 'Cuentame' or Peticion == 'Cuéntame' or Peticion == 'cuéntame':
            primerTexto = parts[2]
            Segundotexto= parts[4]

            if primerTexto.isdigit():
                 Primernumero = int(parts[2])
            else:
                if primerTexto in numeros:
                    Primernumero = numeros[primerTexto]

            if Segundotexto.isdigit():
                 SegundoNumero = int(parts[4])
            else:    
                if Segundotexto in numeros:
                    SegundoNumero = numeros[Segundotexto]

            # Suponiendo que ya tienes definidos los valores de Primernumero y SegundoNumero

            if SegundoNumero > Primernumero:
                contador = 0
                for i in range(Primernumero, SegundoNumero + 1):
                    contador += 1
                    time.sleep(1) 
                    enviar_matriz(i)
            else:
                print("Favor de intentar de nuevo con otros números.")

            
        elif Peticion == 'resta' or Peticion == 'Resta':
            Primernumero = int(parts[1])
            SegundoNumero = int(parts[3])
            resultado = Primernumero - SegundoNumero
            if resultado >= 0:
                letras=[Primernumero,'-',SegundoNumero,'=',resultado]
                for letra in letras:
                    time.sleep(1) 
                    enviar_matriz(letra)
            else:
                print("Prueba con otros numeros")
        elif Peticion in ['Deletrea', 'deletrea', 'deletreame', 'Deletreame']:
            CadenaNew = parts[1:]
            if len(CadenaNew) > 2:
                letras = list(CadenaNew[2])
                print(letras)
                for letra in letras:
                    if letra.isupper():  # Verifica si la letra es mayúscula
                        letra = letra.lower()  # Convierte la letra a minúscula
                    time.sleep(1) 
                    enviar_matriz(letra)
            else:
                letras = list(CadenaNew[0])
                print(letras)
                for letra in letras:
                    if letra.isupper():  # Verifica si la letra es mayúscula
                        letra = letra.lower()  # Convierte la letra a minúscula
                    time.sleep(1) 
                    enviar_matriz(letra)
    else:
        print("No se proporcionaron suficientes argumentos")

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()

    def initUI(self):
    # Crear los labels y colocarlos usando pack
        self.instrucciones = tk.Label(self.master, text='INSTRUCCIONES.', bg='#0000ff', fg='white')
        

        self.deletro = tk.Label(self.master, text='Puedes obtener el deletreo de cualquier palabra diciendo simplemente "Deletra", seguido de la palabra que quieras.', bg='#d0d0d0')
        self.muestra = tk.Label(self.master, text='Puedes solicitar la visualización de vocales, el alfabeto o números diciendo simplemente "Muestra", seguido de lo que desees ver.', bg='#d0d0d0')
        self.aritmetica = tk.Label(self.master, text='Puedes solicitar operaciones de suma o resta con números menores a 10. Simplemente indica "Suma" o "Resta", seguido de los números que prefieras.', bg='#d0d0d0')
        self.cuenta = tk.Label(self.master, text='Puedes solicitar conteos de números simplemente diciendo "cuenta", seguido de los números que te gustaría que sean contados', bg='#d0d0d0') 
        self.label = tk.Label(self.master, text='Presiona el botón para hablar', bg='#0000ff', fg='white')

        self.instrucciones.pack(fill='x')  # Para que la etiqueta ocupe todo el ancho
        self.deletro.pack()
        self.muestra.pack()
        self.aritmetica.pack()
        self.cuenta.pack()

        # Crear el botón con el tamaño deseado
        self.btn = tk.Button(self.master, text='Hablar', command=self.on_click, width=20, height=5, font=("Arial", 10))

        # Colocar el botón en el centro
        self.btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Colocar la etiqueta en la parte inferior de la ventana
        self.label.pack(side=tk.BOTTOM, fill='x')



    def on_click(self):
        self.btn.config(text='Escuchando...')
        t = threading.Thread(target=self.recognize_speech)
        t.start()

    def recognize_speech(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='es-ES')
            self.label.config(text=f'Texto: {text}')
            realizar_acciones(text)  # Llamar a tu función personalizada para realizar acciones
            
        except sr.UnknownValueError:
            self.label.config(text='No se pudo entender lo que dijiste')
        except sr.RequestError as e:
            self.label.config(text=f'Error al conectarse con el servidor de reconocimiento: {e}')
        
        self.btn.config(text='Hablar')

# Inicializar la conexión serial (reemplaza 'COMX' con el nombre de tu puerto)
ser = serial.Serial('COM4', 9600)
time.sleep(2)
# Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title('GamiFuente')
ventana.iconbitmap("GAMIFUENTE.ico")
ventana.geometry('800x350')
ventana.config(bg="#d0d0d0")  # Esto establecerá un tono de gris claro como fondo

# Crear una instancia de la clase MainWindow
main_window = MainWindow(master=ventana)

# Ejecutar la aplicación
ventana.mainloop()
