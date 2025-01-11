### Driven Ports for Enrich Content

#### Responsabilidad
Definen las interfaces de salida utilizadas por los casos de uso para interactuar con servicios externos de enriquecimiento, como APIs de terceros para an�lisis de texto, etiquetado o generaci�n de metadatos adicionales. Estas interfaces son implementadas por los adaptadores de salida (Driven Adapters), garantizando un desacoplamiento entre la l�gica de negocio y la infraestructura.

#### Relaci�n con otras capas
- **Es llamado por**: Casos de uso en la misma capa de aplicaci�n para interactuar con recursos externos.
- **Es implementado por**: Adaptadores de salida (Driven Adapters) en la capa de infraestructura.

#### Ejemplo de Interfaz
```python
class EnrichServicePort:
    def enrich_metadata(self, metadata):
        pass
```