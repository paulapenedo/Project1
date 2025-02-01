# Proyecto PC1

## Estructura del proyecto
```markdown
    Proyecto/
    ├── data/
    ├── src/utils.py
    ├── main.py
    ├── requirements.txt
    ├── README.md
```

---

## Primeros pasos
1. Creamos un entorno de anaconda
    
    `conda create -n [NombreEntorno] python=[VersionPython]`


2. `conda activate PC1`
3. `cd <ruta_carpeta_lproyecto>`
4. `pip install -r requirements.txt`
5. Descargar chromedriver.exe (url) y meterlo en la carpeta del proyecto
6. Cambiar las rutas necesarias de descarga en el archivo .env para ejecutar el proyecto

---

#### Main.ipynb

1. Importamos paquetes necesarios

2. Creamos carpeta data

3. Llamamos funciones para descargar, mover y descomprimir excels
    - Estas funciones están en `utils.py`

    