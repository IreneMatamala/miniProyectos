# Políticas de Red en Kubernetes

Este proyecto demuestra cómo usar Network Policies para aislar tráfico entre pods en un clúster de Kubernetes. Se crean dos aplicaciones (frontend y backend) y se restringe el tráfico para que solo el frontend pueda comunicarse con el backend.

## Objetivo
Mostrar el uso de Network Policies para mejorar la seguridad en un clúster Kubernetes, permitiendo solo el tráfico necesario entre servicios.

## Requisitos
- Un clúster de Kubernetes con un CNI que soporte Network Policies (Calico, Cilium, etc.)
- kubectl configurado para acceder al clúster.

## Pasos
1. Crear un namespace: `kubectl apply -f namespace.yaml`
2. Desplegar los pods de frontend y backend: `kubectl apply -f frontend-pod.yaml -f backend-pod.yaml`
3. Aplicar la política de red: `kubectl apply -f network-policy.yaml`
4. Probar la conectividad con un pod de prueba: `kubectl apply -f test-pod.yaml`

## Verificación
- Ejecutar `kubectl exec` en el pod de frontend para probar conectividad con el backend (debería funcionar).
- Ejecutar `kubectl exec` en el pod de prueba para intentar conectar al backend (debería fallar).

## Mejoras futuras
- Añadir políticas que limiten el tráfico de salida.
- Utilizar etiquetas más complejas para seleccionar pods.
- Probar con diferentes CNIs.
