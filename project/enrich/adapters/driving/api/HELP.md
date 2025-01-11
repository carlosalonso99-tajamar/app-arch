### Driving Adapters for Enrich

#### Responsabilidad
Son responsables de traducir las solicitudes externas (como usuarios o sistemas) y llamar a los puertos de entrada (Driving Ports) para ejecutar casos de uso relacionados con el enriquecimiento. Exponen los casos de uso al mundo exterior a trav�s de interfaces como APIs REST, manejadores de eventos, entre otros.

#### Relaci�n con otras capas
- **Es llamado por**: Fuentes externas (usuarios, sistemas).
- **Llama a**: Puertos de entrada (Driving Ports) implementados por los casos de uso para invocar la l�gica de negocio.

#### Ejemplo de Interacci�n
```python
@app.route('/api/enrich/<int:content_id>', methods=['POST'])
def enrich_content(content_id):
    metadata = request.json.get("metadata", {})
    # Llama al puerto de entrada inyectado como instancia
    return enrich_port.execute(content_id, metadata)
```

#### Nota
La instancia del Driving Port (`enrich_port`) debe ser inyectada al controlador desde una f�brica o en el punto de configuraci�n de la aplicaci�n. Esto asegura un dise�o limpio y desacoplado.