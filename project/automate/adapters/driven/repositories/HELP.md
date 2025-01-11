### Driven Repositories for Automate

#### Responsabilidad
Implementan las interfaces definidas en los puertos de salida (Driven Ports) para interactuar con sistemas de almacenamiento persistente, como bases de datos.

#### Relación con otras capas
- **Es llamado por**: Puertos de salida (Driven Ports).
- **Llama a**: Recursos externos (bases de datos, etc.).

#### Ejemplo
```python
class TaskRepository:
    def save_task(self, task):
        pass
```