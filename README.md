# **Windows Maintenance Script**
---
Este programa automatiza tareas básicas de mantenimiento en Windows.

## ¿Qué hace este programa?
1. Limpia archivos temporales del sistema.
2. Inicia un examen rápido con Windows Defender.
3. Verifica si hay actualizaciones de Windows disponibles.
4. Instala las actualizaciones automáticamente si existen.
5. Muestra notificaciones en pantalla durante todo el proceso.

## Requisitos antes de empezar
* Tener Python instalado en tu computadora.
* Usar Windows 10 u 11.
* Tener PowerShell instalado (viene por defecto).
* Instalar el módulo de PowerShell `BurntToast` para notificaciones.

## Instrucciones paso a paso
### 1) Descarga el programa:
#### Opción 1: Copiar y crear el archivo manualmente
* Abre un editor de texto (como Bloc de notas o VS Code)
* Copia el código del archivo `main.py` del repositorio
* Guarda el archivo con el nombre `main.py`

#### Opción 2: Descargar desde el botón "Code"
* Ve al repositorio en GitHub
* Haz clic en el botón verde "Code"
* Selecciona "Download ZIP"
* Descomprime el archivo ZIP descargado

#### Opción 3: Descargar desde Releases
* Ve a la sección "Releases" del repositorio en GitHub
* Encuentra la última versión
* Haz clic en "Source code (zip)"
* Descomprime el archivo ZIP descargado

### 2) Instala el módulo BurntToast (solo la primera vez):
1. Abre PowerShell **como administrador**
2. Escribe el siguiente comando y presiona Enter:
   ```
   Install-Module -Name BurntToast -Force
   ```
3. Si se solicita, confirma escribiendo `Y` y luego Enter.

### 3) Instala Python (si no lo tienes ya):
1. Ve a [python.org](https://www.python.org/downloads/)
2. Descarga e instala la última versión para Windows
3. Durante la instalación, **marca la casilla "Add Python to PATH"**

### 4) Ejecuta el programa:
#### En Windows (usando PowerShell):
1. Abre la carpeta donde guardaste `main.py`
2. Mantén presionada la tecla **Shift** y haz clic derecho en un espacio vacío
3. Selecciona **"Abrir ventana de PowerShell aquí"**
4. Escribe `python main.py` y presiona Enter

#### En Visual Studio Code:
1. Abre la carpeta del proyecto en VS Code
2. Instala la extensión de Python si aún no lo has hecho
3. Abre `main.py` y haz clic en el botón de **reproducción ▶️** en la esquina superior derecha

## ¿Qué deberías ver?
* Notificaciones emergentes en la esquina inferior derecha.
* Limpieza de archivos temporales.
* Inicio del análisis rápido con Windows Defender.
* Verificación e instalación de actualizaciones si existen.

## Solución de problemas comunes
* **No se muestran notificaciones**: Asegúrate de haber instalado correctamente el módulo `BurntToast`.
* **Python no es reconocido**: Reinstala Python y asegúrate de marcar la opción “Add to PATH”.
* **Errores al borrar archivos**: Algunos archivos temporales no se pueden eliminar si están en uso, esto es normal y el programa los ignora.

---
## Nota importante
Este programa no recopila ni comparte ninguna información personal. Todo se ejecuta localmente en tu equipo.
