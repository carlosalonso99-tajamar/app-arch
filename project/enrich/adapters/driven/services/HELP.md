### Driven Services for Enrich

#### Responsabilidad
Implementan las interfaces definidas en los puertos de salida (Driven Ports) para interactuar con servicios externos, como APIs de terceros o sistemas relacionados con el enriquecimiento de contenido. Proporcionan la conexi�n directa con estos servicios, encapsulando los detalles de implementaci�n.

#### Relaci�n con otras capas
- **Es llamado por**: Puertos de salida (Driven Ports) implementados por los casos de uso.
- **Llama a**: Recursos externos (servicios o APIs externas).

#### Ejemplo de Interacci�n
```python
from application.ports.driven.enrich_service_port import EnrichServicePort

class EnrichService(EnrichServicePort):
    def enrich_metadata(self, metadata):
        # L�gica para interactuar con un servicio externo de enriquecimiento
        enriched_metadata = {**metadata, "tags": ["enriched", "AI"]}
        return enriched_metadata
```