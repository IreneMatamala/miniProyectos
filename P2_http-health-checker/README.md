# Verificador de Salud HTTP

Este programa en Go comprueba periódicamente el estado de una lista de servicios HTTP/HTTPS. Puede utilizarse para monitorizar endpoints críticos y enviar alertas si algún servicio no responde correctamente.

## Características
- Comprueba múltiples URLs con intervalos configurables.
- Soporta métodos HTTP personalizados y encabezados.
- Define tiempos de espera para evitar bloqueos.
- Registra los resultados en un archivo de log.
- Posibilidad de enviar alertas por email (pendiente de implementar).

## Requisitos
- Go 1.16 o superior.

## Configuración
El archivo `config.json` contiene:
- `services`: Lista de servicios a comprobar.
- `check_interval_seconds`: Intervalo entre comprobaciones.
- `timeout_seconds`: Tiempo de espera para cada petición.

## Compilación y ejecución
1. Compila el programa: `go build -o health-checker main.go`
2. Ajusta `config.json` según tus necesidades.
3. Ejecuta: `./health-checker`

## Ejecutar como servicio
Puedes crear un servicio systemd para ejecutar el verificador en segundo plano.

## Mejoras futuras
- Implementar notificaciones por email, Slack o Telegram.
- Añadir métricas para exportar a Prometheus.
- Crear un dashboard web sencillo con el estado de los servicios.
