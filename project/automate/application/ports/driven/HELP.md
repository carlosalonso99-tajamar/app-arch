### Driven Ports for Publish Content

#### Responsabilidad
Definen las interfaces de salida utilizadas por los casos de uso para interactuar con recursos externos, como servicios de publicación de contenido en redes sociales, sitios web, o plataformas de terceros. Estas interfaces son implementadas por los adaptadores de salida (Driven Adapters), garantizando un desacoplamiento entre la lógica de negocio y la infraestructura.

#### Relación con otras capas
- **Es llamado por**: Casos de uso en la misma capa de aplicación para interactuar con recursos externos.
- **Es implementado por**: Adaptadores de salida (Driven Adapters) en la capa de infraestructura.

#### Ejemplo de Interfaz
```python
class PublishServicePort:
    def publish_content(self, content_id, metadata):
        pass
```