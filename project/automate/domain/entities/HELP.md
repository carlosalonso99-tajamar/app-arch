### Entities for Automate Content

#### Responsabilidad
Representan los objetos clave del dominio relacionados con la automatizaci�n de contenido. Contienen datos y comportamientos esenciales del negocio, independientes de cualquier implementaci�n t�cnica.

#### Relaci�n con otras capas
- **Es utilizado por**: Servicios del dominio y casos de uso.

#### Ejemplo
```python
class Content:
    def __init__(self, content_id, metadata, status):
        self.content_id = content_id
        self.metadata = metadata
        self.status = status
```