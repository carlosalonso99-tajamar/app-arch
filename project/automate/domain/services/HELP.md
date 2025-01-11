### Domain Services for Automate Content

#### Responsabilidad
Encapsulan l�gica de negocio que no pertenece exclusivamente a una entidad, como validaciones complejas o reglas transversales relacionadas con la automatizaci�n de contenido.

#### Relaci�n con otras capas
- **Es llamado por**: Casos de uso.
- **Utiliza**: Entidades y eventos del dominio.

#### Ejemplo
```python
def validate_content(content):
    if not content.metadata:
        raise ValueError("Content must include metadata")
```