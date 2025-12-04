#!/bin/bash

# Cargar configuración
CONFIG_FILE="config.conf"
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
else
    echo "Error: No se encuentra el archivo de configuración $CONFIG_FILE"
    exit 1
fi

# Crear directorio de backups si no existe
mkdir -p "$BACKUP_DIR"

# Obtener fecha para el nombre del archivo
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/backup_$DATE.sql.gz"

# Función para loguear mensajes
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

# Realizar backup de cada base de datos
for DB in $DATABASES; do
    log "Realizando backup de la base de datos: $DB"
    mysqldump --user="$MYSQL_USER" --password="$MYSQL_PASSWORD" --host="$MYSQL_HOST" "$DB" | gzip > "$BACKUP_FILE"
    if [ ${PIPESTATUS[0]} -ne 0 ]; then
        log "Error al hacer backup de $DB"
        exit 1
    fi
done

log "Backup completado: $BACKUP_FILE"

# Rotación: eliminar backups más antiguos de X días
if [ -n "$DAYS_TO_KEEP" ]; then
    find "$BACKUP_DIR" -name "backup_*.sql.gz" -mtime +"$DAYS_TO_KEEP" -exec rm {} \;
    log "Rotación completada (eliminados backups de más de $DAYS_TO_KEEP días)"
fi

# Subida remota si está configurada
if [ "$UPLOAD_REMOTE" = true ]; then
    log "Subiendo backup a servidor remoto..."
    scp "$BACKUP_FILE" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR"
    if [ $? -eq 0 ]; then
        log "Subida remota completada."
    else
        log "Error en la subida remota."
    fi
fi

# Subida a AWS S3 si está configurada
if [ "$UPLOAD_S3" = true ]; then
    log "Subiendo backup a AWS S3..."
    aws s3 cp "$BACKUP_FILE" "s3://$S3_BUCKET/"
    if [ $? -eq 0 ]; then
        log "Subida a S3 completada."
    else
        log "Error en la subida a S3."
    fi
fi

log "Proceso de backup finalizado."
