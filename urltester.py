import requests
import urllib3

# Desactivar advertencias de SSL no verificado (para entornos de laboratorio)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def comprobar_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            # Leemos las líneas y quitamos espacios/saltos de línea
            urls = [linea.strip() for linea in archivo if linea.strip()]
        
        print(f"{'URL':<40} | {'ESTADO'}")
        print("-" * 55)

        for url in urls:
            # Aseguramos que la URL tenga protocolo http si no lo tiene
            target = url if url.startswith("http") else f"http://{url}"
            
            try:
                respuesta = requests.get(target, timeout=5, verify=False)
                if respuesta.status_code == 200:
                    print(f"{target:<40} | ✅ Responde")
                else:
                    print(f"{target:<40} | ⚠️ Código: {respuesta.status_code}")
            except Exception:
                print(f"{target:<40} | ❌ No responde")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")

if __name__ == "__main__":
    comprobar_desde_archivo("urls.txt")
