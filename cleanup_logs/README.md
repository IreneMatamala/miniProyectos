# Limpieza de Logs Antiguos

Este script en Python automatiza la eliminación de archivos de log que superen una antigüedad o un tamaño determinado. Es útil para mantener bajo control el espacio en disco en servidores de aplicaciones.

## Características
- Elimina archivos de log más antiguos de X días.
- Opcionalmente, elimina archivos que superen un tamaño máximo.
- Registra sus propias operaciones en un log.
- Configurable mediante archivo YAML.

## Requisitos
- Python 3.6 o superior.
- Módulos PyYAML (ver requirements.txt).

## Configuración
El archivo `config.yaml` permite definir:
- `log_directory`: Directorio a limpiar.
- `days_to_keep`: Número de días a conservar.
- `max_size_mb`: Tamaño máximo en MB (opcional).
- `log_file`: Ruta al archivo de log del script.

## Uso
1. Instala las dependencias: `pip install -r requirements.txt`
2. Ajusta `config.yaml` según tus necesidades.
3. Ejecuta: `python cleanup_logs.py`

## Programar ejecución periódica
Se puede añadir una entrada en crontab para ejecutar el script diariamente:

`0 2 * * * /usr/bin/python3 /ruta/al/script/cleanup_logs.py`

## Mejoras futuras
- Añadir compresión de logs antes de eliminarlos.
- Enviar notificaciones por email o Slack en caso de error.
- Soporte para patrones de nombre de archivo personalizados.
