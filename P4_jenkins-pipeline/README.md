# Pipeline Jenkins para una aplicación Node.js

Este proyecto contiene un Jenkinsfile que define un pipeline para construir, probar y desplegar una aplicación Node.js en un entorno Kubernetes.

## Características del pipeline
- **Checkout**: Obtiene el código desde un repositorio Git.
- **Build**: Construye la imagen Docker de la aplicación.
- **Test**: Ejecuta tests unitarios.
- **Security Scan**: Escanea la imagen Docker con Trivy.
- **Deploy**: Despliega la aplicación en Kubernetes (usando kubectl).
- **Rollback**: Opción para revertir el despliegue en caso de fallo.

## Requisitos
- Jenkins con plugins de Docker, Kubernetes y Pipeline.
- Un clúster de Kubernetes accesible desde Jenkins.
- Docker Registry (puede ser Docker Hub o un registro privado).

## Configuración en Jenkins
1. Crear un pipeline job y apuntar al repositorio que contiene este Jenkinsfile.
2. Configurar las credenciales en Jenkins para:
   - Docker Registry (usuario/contraseña)
   - Kubernetes (kubeconfig)
3. Ajustar las variables en el Jenkinsfile según tu entorno.

## Uso
El pipeline se ejecuta automáticamente al hacer push a la rama main, pero también puede lanzarse manualmente.

## Mejoras futuras
- Añadir etapa de pruebas de integración.
- Implementar canary deployments.
- Añadir notificaciones a Slack o email.
