#!/bin/bash

# Script para restaurar una base de datos desde un backup comprimido

if [ $# -ne 2 ]; then
    echo "Uso: $0 <archivo_backup.sql.gz> <nombre_base_datos>"
    exit 1
fi

BACKUP_FILE=$1
DATABASE=$2

# Cargar configuración (para obtener credenciales)
CONFIG_FILE="config.conf"
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
else
    echo "Advertencia: No se encuentra config.conf, usando valores por defecto."
    MYSQL_HOST="localhost"
    MYSQL_USER="root"
    MYSQL_PASSWORD=""
fi

echo "Restaurando $BACKUP_FILE en la base de datos $DATABASE..."
gunzip < "$BACKUP_FILE" | mysql --user="$MYSQL_USER" --password="$MYSQL_PASSWORD" --host="$MYSQL_HOST" "$DATABASE"

if [ $? -eq 0 ]; then
    echo "Restauración completada."
else
    echo "Error durante la restauración."
fi
