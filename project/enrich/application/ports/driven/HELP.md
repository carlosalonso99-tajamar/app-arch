### Driven Ports for Enrich Content

#### Responsabilidad
Definen las interfaces de salida utilizadas por los casos de uso para interactuar con servicios externos de enriquecimiento, como APIs de terceros para análisis de texto, etiquetado o generación de metadatos adicionales. Estas interfaces son implementadas por los adaptadores de salida (Driven Adapters), garantizando un desacoplamiento entre la lógica de negocio y la infraestructura.

#### Relación con otras capas
- **Es llamado por**: Casos de uso en la misma capa de aplicación para interactuar con recursos externos.
- **Es implementado por**: Adaptadores de salida (Driven Adapters) en la capa de infraestructura.

#### Ejemplo de Interfaz
```python
class EnrichServicePort:
    def enrich_metadata(self, metadata):
        pass
```