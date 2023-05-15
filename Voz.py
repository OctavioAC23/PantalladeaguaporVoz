import sys
import threading
import speech_recognition as sr
import tkinter as tk
import subprocess



class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()

    def initUI(self):
        self.label = tk.Label(self.master, text='Presiona el botón para hablar')
        self.btn = tk.Button(self.master, text='Hablar', command=self.on_click)

        self.label.pack()
        self.btn.pack()

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
            if 'muestra' in text.lower() or 'muestrame' in text.lower() or 'dime' in text.lower() or 'Muestrame' in text.lower() :
                if 'vocales' in text.lower():
                    PA_Vocales()
                elif 'alfabeto' in text.lower():
                    PA_Alfabeto()
                elif 'suma' in text.lower():
                     palabra = text.replace("suma", "")
                     if palabra == "":
                       self.label.config(text='No se pudo entender lo que dijiste, Favor de Repetirlo')
                     else:
                        PA_Suma(palabra)
                elif 'resta' in text.lower():
                    palabra = text.replace("resta", "")
                    if palabra == "":
                        self.label.config(text='No se pudo entender lo que dijiste, Favor de Repetirlo')
                    else:
                        PA_Resta(palabra)
            elif 'deletrea' in text.lower() or 'deletreame' in text.lower():
                palabra = text.replace("deletrea ", "")
                if palabra == "":
                       self.label.config(text='No se pudo entender lo que dijiste, Favor de Repetirlo')
                else:              
                    PA_Deletrea(palabra)
            elif 'suma' in text.lower():
                palabra = text.replace("suma", "")
                if palabra == "":
                    self.label.config(text='No se pudo entender lo que dijiste, Favor de Repetirlo')
                else:
                    PA_Suma(palabra)
            elif 'resta' in text.lower():
                palabra = text.replace("resta", "")
                if palabra == "":
                    self.label.config(text='No se pudo entender lo que dijiste, Favor de Repetirlo')
                else:
                    PA_Resta(palabra)

        except sr.UnknownValueError:
            self.label.config(text='No se pudo entender lo que dijiste')
        except sr.RequestError as e:
            self.label.config(text=f'Error al conectarse con el servidor de reconocimiento: {e}')
        
        self.btn.config(text='Hablar')

def PA_Vocales():
    print('Se muestra las vocales')
    subprocess.run(['python', 'pantalla.py', 'vocales',' '])
def PA_Alfabeto():
    print('Se muestra el alfabeto')
    subprocess.run(['python', 'pantalla.py', 'alfabeto',' '])
def PA_Suma(palabra):
    print('Se muestra el resultado de la "Suma"')
    subprocess.run(['python', 'pantalla.py', 'suma',palabra])
def PA_Resta(palabra):
    print('Se muestra el resultado de la "Resta"')
    subprocess.run(['python', 'pantalla.py', 'resta',palabra])
def PA_Deletrea(palabra):
    print('Se envia la palabra '+palabra)
    subprocess.run(['python', 'pantalla.py', 'deletrea',palabra])
    

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Reconocimiento de voz')
    root.geometry('500x150')

    window = MainWindow(master=root)
    window.mainloop()
