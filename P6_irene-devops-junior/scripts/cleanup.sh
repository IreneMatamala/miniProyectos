#!/bin/bash
# Script de limpieza

echo "=== Limpieza de contenedores viejos ==="

# Eliminar contenedores detenidos
docker container prune -f

# Eliminar imágenes sin usar
docker image prune -af

# Limpiar volumenes no usados
docker volume prune -f

echo "Limpieza completada"
