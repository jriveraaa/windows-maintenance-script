import os
import shutil
import tempfile
import ctypes
import subprocess
import time

import subprocess

def mostrar_notificacion(titulo, mensaje):
    comando = f'''
    Import-Module BurntToast;
    New-BurntToastNotification -Text "{titulo}", "{mensaje}";
    '''
    try:
        subprocess.run(["powershell", "-Command", comando], check=True)
    except Exception as e:
        print(f"Error mostrando notificación: {e}")

def eliminar_archivos_temp():
    try:
        temp_dir = tempfile.gettempdir()

        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)

            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):

                    try:
                        os.unlink(item_path)
                    except PermissionError as e:
                        if e.winerror == 32:
                            pass
                        else:
                            raise

                elif os.path.isdir(item_path):

                    try:
                        shutil.rmtree(item_path)
                    except PermissionError as e:
                        if e.winerror == 32:
                            pass
                        else:
                            raise

            except Exception as e:
                print(f"Error eliminando {item}: {e}")

        return True
    
    except Exception as e:
        return False
    
def examen_antivirus():
    try:        
        mostrar_notificacion("Seguridad", "Iniciando examen rápido con Windows Security")
        comando = 'Start-MpScan -ScanType QuickScan'
        
        subprocess.Popen(
            ["powershell", "-Command", comando],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
        )
        
        time.sleep(3)
        
        return True
    
    except Exception as e:
        return False

def verificar_actualizaciones():
    try:
        comando = '(New-Object -ComObject Microsoft.Update.Session).CreateUpdateSearcher().Search("IsInstalled=0").Updates.Count'
        resultado = subprocess.run(
            ["powershell", "-Command", comando],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        actualizaciones = int(resultado.stdout.strip()) if resultado.stdout.strip() else 0

        mostrar_notificacion("Actualizaciones", "Actualizaciones pendientes encontradas")
        return actualizaciones > 0
    except Exception as e:
        mostrar_notificacion("Actualizaciones", "Error verificando actualizaciones")
        return False
    
def instalar_actualizaciones():
    try:
        comando = (
            '$Session = New-Object -ComObject Microsoft.Update.Session; '
            '$Searcher = $Session.CreateUpdateSearcher(); '
            '$Updates = $Searcher.Search("IsInstalled=0").Updates; '
            '$Downloader = $Session.CreateUpdateDownloader(); '
            '$Downloader.Updates = $Updates; '
            '$Downloader.Download(); '
            '$Installer = $Session.CreateUpdateInstaller(); '
            '$Installer.Updates = $Updates; '
            '$Installer.Install();'
        )
        
        proceso = subprocess.Popen(
            ["powershell", "-Command", comando],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
        
        return True
    except Exception as e:
        mostrar_notificacion("Actualizaciones", "Error actualizando")
        return False

def main():
    mostrar_notificacion("Mantenimiento", "Iniciando proceso de mantenimiento")
        
    if eliminar_archivos_temp():
        mostrar_notificacion("Limpieza", "Limpieza de archivos temporales completada")

    if examen_antivirus():
        mostrar_notificacion("Seguridad", "Examen de seguridad finalizado")
    
    if verificar_actualizaciones():
        mostrar_notificacion("Actualizaciones", "Se ha verificado si hay actualizaciones disponibles")
        if instalar_actualizaciones():
            mostrar_notificacion("Actualizaciones", "Actualizaciones instaladas - Verificar si se requiere reinicio")
    
    mostrar_notificacion("Mantenimiento", "Proceso de mantenimiento completado")

if __name__ == "__main__":
    main()
