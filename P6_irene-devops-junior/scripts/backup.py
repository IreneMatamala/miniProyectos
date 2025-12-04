#!/usr/bin/env python3

import os
import shutil
import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def backup_app():
    """Crea una copia de la app"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    backup_name = f"backup_app_{timestamp}"
    
    # Crear directorio de backup
    os.makedirs(f"backups/{backup_name}", exist_ok=True)
    
    # Copiar archivos importantes
    shutil.copy("app/app.py", f"backups/{backup_name}/")
    shutil.copy("app/requirements.txt", f"backups/{backup_name}/")
    
    # Comprimir
    shutil.make_archive(f"backups/{backup_name}", 'zip', f"backups/{backup_name}")
    
    logger.info(f"Backup creado: backups/{backup_name}.zip")
    return f"backups/{backup_name}.zip"

if __name__ == "__main__":
    backup_app()
