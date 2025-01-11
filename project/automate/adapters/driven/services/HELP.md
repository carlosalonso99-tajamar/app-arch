### Driven Services for Publish Content

#### Responsabilidad
Implementan las interfaces definidas en los puertos de salida (Driven Ports) para interactuar con servicios externos relacionados con la publicación de contenido, como APIs de redes sociales, CMS, o servicios de distribución de contenido.

#### Relación con otras capas
- **Es llamado por**: Puertos de salida (Driven Ports) implementados por los casos de uso.
- **Llama a**: Recursos externos (servicios o APIs externas).

#### Ejemplo
```python
from application.ports.driven.publish_service_port import PublishServicePort

class PublishService(PublishServicePort):
    def publish_content(self, content_id, metadata):
        # Lógica para interactuar con un servicio externo de publicación
        print(f"Publicando contenido {content_id} con metadatos: {metadata}")
        return {"content_id": content_id, "status": "published"}
```