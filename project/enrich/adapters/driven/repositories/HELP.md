### Driven Repositories for Enrich

#### Responsabilidad
Implementan las interfaces definidas en los puertos de salida (Driven Ports) para interactuar con sistemas de almacenamiento persistente, como bases de datos o el DAM. Garantizan el desacoplamiento entre la l�gica de negocio y la infraestructura de almacenamiento.

#### Relaci�n con otras capas
- **Es llamado por**: Puertos de salida (Driven Ports) implementados por los casos de uso.
- **Llama a**: Recursos externos (bases de datos, DAM, etc.).

#### Ejemplo de Interacci�n
```python
class DAMRepository:
    def save_metadata(self, content_id, metadata):
        # L�gica para guardar metadatos en el DAM
        pass
```