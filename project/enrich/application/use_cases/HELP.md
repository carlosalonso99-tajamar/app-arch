### Use Cases for Enrich Content

#### Responsabilidad
Implementan la lógica de negocio de alto nivel específica del enriquecimiento de contenido. Los casos de uso son responsables de coordinar las interacciones entre los puertos de entrada (Driving Ports) y los puertos de salida (Driven Ports).

#### Relación con otras capas
- **Implementan**: Los puertos de entrada (Driving Ports).
- **Usan**: Los puertos de salida (Driven Ports) para interactuar con recursos externos.

#### Ejemplo de Caso de Uso
```python
class EnrichContentUseCase(EnrichPort):
    def __init__(self, enrich_service_port):
        self.enrich_service_port = enrich_service_port

    def execute(self, content_id, metadata):
        # Enriquecimiento del contenido
        enriched_metadata = self.enrich_service_port.enrich_metadata(metadata)
        return {"content_id": content_id, "metadata": enriched_metadata, "status": "enriched"}
```