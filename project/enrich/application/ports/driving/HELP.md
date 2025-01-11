### Driving Ports for Enrich

#### Responsabilidad
Definen las interfaces de entrada que son implementadas por los casos de uso en la capa de aplicación. Proporcionan un contrato claro para los adaptadores de entrada (Driving Adapters) para interactuar con la lógica de negocio.

#### Relación con otras capas
- **Es llamado por**: Adaptadores de entrada (Driving Adapters), como controladores REST, manejadores de eventos o cualquier otra fuente externa.
- **Es implementado por**: Casos de uso en la misma capa de aplicación.

#### Ejemplo de Interfaz
```python
class EnrichPort:
    def execute(self, content_id, metadata):
        pass
```