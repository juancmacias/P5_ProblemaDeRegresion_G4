import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
LOG_PATH = os.path.join(os.path.dirname(__file__),  "/app/"+os.getenv("LOG_TXT", "log.txt"))
def leer_archivo():
    try:
        with open(LOG_PATH, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        #contenido_html = "<br>".join(line.strip() for line in contenido)
        # Retornar el contenido dentro de un HTML básico
        contenido_invertido = "".join(lineas[::-1])
        return contenido_invertido
    except FileNotFoundError:
        return ("Error: Archivo no encontrado\n")
    except Exception as e:
        return (f"Error: {e}")
    
def write_log(text):
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] {text}\n")