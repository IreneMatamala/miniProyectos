# Script de Backup para MySQL

Este script realiza backups de bases de datos MySQL/MariaDB y los comprime, con opción de enviarlos a un servidor remoto vía SCP o AWS S3. Incluye rotación de backups antiguos.

## Características
- Backup de una o varias bases de datos.
- Compresión con gzip.
- Rotación automática: elimina backups más antiguos de X días.
- Posibilidad de subir a un servidor remoto o a AWS S3.
- Restauración sencilla desde un backup.

## Requisitos
- mysqldump instalado.
- gzip para compresión.
- (Opcional) cliente SCP o AWS CLI para subida remota.

## Configuración
Copiar `config.conf.example` a `config.conf` y ajustar las variables:
- Directorio de backup, credenciales de MySQL, bases de datos, etc.

## Uso
1. Hacer ejecutable el script: `chmod +x backup.sh`
2. Ejecutar: `./backup.sh`

## Programar con cron
Para ejecutar diariamente a las 3 AM:

`0 3 * * * /ruta/a/mysql-backup/backup.sh`

## Restauración
Usar el script `restore.sh` indicando el archivo de backup.

## Mejoras futuras
- Añadir cifrado de los backups.
- Soporte para más destinos (Google Cloud Storage, Azure Blob).
- Notificaciones en caso de fallo.
