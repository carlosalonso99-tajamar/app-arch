### Domain Layer for Automate Content

#### Responsabilidad
Contiene la l�gica de negocio central y las reglas espec�ficas de la automatizaci�n de contenido. Es completamente independiente de cualquier detalle t�cnico o infraestructura.

#### Relaci�n con otras capas
- **Es utilizado por**: Casos de uso.
- **Utiliza**: Entidades, eventos y servicios del dominio.

#### Ejemplo
```python
class AutomateContentService:
    def process_content(self, content):
        content.status = "processed"
```