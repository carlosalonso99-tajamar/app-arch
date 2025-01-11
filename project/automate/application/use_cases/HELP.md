### Use Cases for Publish Content

#### Responsabilidad
Implementan la l�gica de negocio de alto nivel espec�fica de la publicaci�n de contenido. Los casos de uso son responsables de coordinar las interacciones entre los puertos de entrada (Driving Ports) y los puertos de salida (Driven Ports).

#### Relaci�n con otras capas
- **Implementan**: Los puertos de entrada (Driving Ports).
- **Usan**: Los puertos de salida (Driven Ports) para interactuar con recursos externos.

#### Ejemplo de Caso de Uso
```python
class PublishContentUseCase(PublishPort):
    def __init__(self, publish_service_port):
        self.publish_service_port = publish_service_port

    def execute(self, content_id, metadata):
        content = {"content_id": content_id, "metadata": metadata, "status": "publishing"}
        # Llama al puerto de salida para realizar la publicaci�n
        return self.publish_service_port.publish_content(content_id, metadata)
```