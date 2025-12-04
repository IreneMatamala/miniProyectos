#!/usr/bin/env python3
"""
Script para limpiar logs antiguos.
Lee configuración desde config.yaml.
"""

import os
import time
import logging
import yaml
from datetime import datetime, timedelta

def load_config(config_path):
    """Carga la configuración desde un archivo YAML."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def setup_logging(log_file):
    """Configura el logging del script."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def cleanup_logs(log_dir, days_to_keep, max_size_mb=None):
    """
    Elimina archivos de log más antiguos que `days_to_keep` días.
    Si se especifica `max_size_mb`, también elimina archivos que superen ese tamaño.
    """
    now = time.time()
    cutoff = now - (days_to_keep * 86400)
    deleted_count = 0
    freed_space = 0  # en bytes

    for filename in os.listdir(log_dir):
        filepath = os.path.join(log_dir, filename)
        if not os.path.isfile(filepath):
            continue

        # Verificar antigüedad
        file_mtime = os.path.getmtime(filepath)
        if file_mtime < cutoff:
            try:
                file_size = os.path.getsize(filepath)
                os.remove(filepath)
                deleted_count += 1
                freed_space += file_size
                logging.info(f"Eliminado por antigüedad: {filename}")
            except Exception as e:
                logging.error(f"No se pudo eliminar {filename}: {e}")
        # Verificar tamaño si se especificó max_size_mb
        elif max_size_mb is not None:
            file_size = os.path.getsize(filepath)
            if file_size > max_size_mb * 1024 * 1024:
                try:
                    os.remove(filepath)
                    deleted_count += 1
                    freed_space += file_size
                    logging.info(f"Eliminado por tamaño: {filename}")
                except Exception as e:
                    logging.error(f"No se pudo eliminar {filename}: {e}")

    return deleted_count, freed_space

def main():
    # Cargar configuración
    config = load_config('config.yaml')
    log_dir = config['log_directory']
    days_to_keep = config['days_to_keep']
    max_size_mb = config.get('max_size_mb')
    log_file = config['log_file']

    # Configurar logging
    setup_logging(log_file)

    # Verificar que el directorio existe
    if not os.path.isdir(log_dir):
        logging.error(f"El directorio {log_dir} no existe.")
        return

    logging.info("Iniciando limpieza de logs...")
    deleted, freed = cleanup_logs(log_dir, days_to_keep, max_size_mb)
    logging.info(f"Limpieza completada. Archivos eliminados: {deleted}. Espacio liberado: {freed / (1024*1024):.2f} MB")

if __name__ == "__main__":
    main()
