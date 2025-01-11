### Driving Adapters for Automate

#### Responsabilidad
Son responsables de traducir las solicitudes externas (como usuarios o sistemas) y llamar a los puertos de entrada (Driving Ports) para ejecutar casos de uso relacionados con las tareas de automatización. Exponen los casos de uso al mundo exterior a través de interfaces como APIs REST, manejadores de eventos, entre otros.

#### Relación con otras capas
- **Es llamado por**: Fuentes externas (usuarios, sistemas).
- **Llama a**: Puertos de entrada (Driving Ports) implementados por los casos de uso para invocar la lógica de negocio.

#### Ejemplo de Interacción
```python
@app.route('/api/automate/<int:task_id>', methods=['POST'])
def automate_task(task_id):
    task_data = request.json
    return automate_port.execute(task_id)
```

#### Nota
La instancia del Driving Port (`automate_port`) debe ser inyectada al controlador desde una fábrica o en el punto de configuración de la aplicación. Esto asegura un diseño limpio y desacoplado.