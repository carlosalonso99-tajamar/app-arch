### Domain Events for Automate Content

#### Responsabilidad
Capturan y representan cambios significativos en el estado del sistema relacionados con la automatización de contenido (ej. contenido procesado o actualizado).

#### Relación con otras capas
- **Es utilizado por**: Servicios del dominio, casos de uso y adaptadores.

#### Ejemplo
```python
class ContentUpdated:
    def __init__(self, content_id, status):
        self.content_id = content_id
        self.status = status
```