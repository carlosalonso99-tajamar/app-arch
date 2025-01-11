### Driving Adapters for Enrich

#### Responsabilidad
Son responsables de traducir las solicitudes externas (como usuarios o sistemas) y llamar a los puertos de entrada (Driving Ports) para ejecutar casos de uso relacionados con el enriquecimiento. Exponen los casos de uso al mundo exterior a través de interfaces como APIs REST, manejadores de eventos, entre otros.

#### Relación con otras capas
- **Es llamado por**: Fuentes externas (usuarios, sistemas).
- **Llama a**: Puertos de entrada (Driving Ports) implementados por los casos de uso para invocar la lógica de negocio.

#### Ejemplo de Interacción
```python
@app.route('/api/enrich/<int:content_id>', methods=['POST'])
def enrich_content(content_id):
    metadata = request.json.get("metadata", {})
    # Llama al puerto de entrada inyectado como instancia
    return enrich_port.execute(content_id, metadata)
```

#### Nota
La instancia del Driving Port (`enrich_port`) debe ser inyectada al controlador desde una fábrica o en el punto de configuración de la aplicación. Esto asegura un diseño limpio y desacoplado.