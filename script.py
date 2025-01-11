import os

# Estructura del proyecto con descripciones en HELP.md
PROJECT_STRUCTURE = {
    "project": {
        "enrich": {
            "application": {
                "ports": {
                    "driving": {
                        "__init__.py": None,
                        "HELP.md": "### Driving Ports for Enrich\n\n#### Responsabilidad\nDefinen las interfaces de entrada que son implementadas por los casos de uso en la capa de aplicación. Proporcionan un contrato claro para los adaptadores de entrada (Driving Adapters) para interactuar con la lógica de negocio.\n\n#### Relación con otras capas\n- **Es llamado por**: Adaptadores de entrada (Driving Adapters), como controladores REST, manejadores de eventos o cualquier otra fuente externa.\n- **Es implementado por**: Casos de uso en la misma capa de aplicación.\n\n#### Ejemplo de Interfaz\n```python\nclass EnrichPort:\n    def execute(self, content_id, metadata):\n        pass\n```"
                    },
                "driven": {
                    "__init__.py": None,
                    "HELP.md": "### Driven Ports for Enrich Content\n\n#### Responsabilidad\nDefinen las interfaces de salida utilizadas por los casos de uso para interactuar con servicios externos de enriquecimiento, como APIs de terceros para análisis de texto, etiquetado o generación de metadatos adicionales. Estas interfaces son implementadas por los adaptadores de salida (Driven Adapters), garantizando un desacoplamiento entre la lógica de negocio y la infraestructura.\n\n#### Relación con otras capas\n- **Es llamado por**: Casos de uso en la misma capa de aplicación para interactuar con recursos externos.\n- **Es implementado por**: Adaptadores de salida (Driven Adapters) en la capa de infraestructura.\n\n#### Ejemplo de Interfaz\n```python\nclass EnrichServicePort:\n    def enrich_metadata(self, metadata):\n        pass\n```"
                    }
                },
                "use_cases": {
                    "__init__.py": None,
                    "HELP.md": "### Use Cases for Enrich Content\n\n#### Responsabilidad\nImplementan la lógica de negocio de alto nivel específica del enriquecimiento de contenido. Los casos de uso son responsables de coordinar las interacciones entre los puertos de entrada (Driving Ports) y los puertos de salida (Driven Ports).\n\n#### Relación con otras capas\n- **Implementan**: Los puertos de entrada (Driving Ports).\n- **Usan**: Los puertos de salida (Driven Ports) para interactuar con recursos externos.\n\n#### Ejemplo de Caso de Uso\n```python\nclass EnrichContentUseCase(EnrichPort):\n    def __init__(self, enrich_service_port):\n        self.enrich_service_port = enrich_service_port\n\n    def execute(self, content_id, metadata):\n        # Enriquecimiento del contenido\n        enriched_metadata = self.enrich_service_port.enrich_metadata(metadata)\n        return {\"content_id\": content_id, \"metadata\": enriched_metadata, \"status\": \"enriched\"}\n```"
                },
            "__init__.py": None,
            "HELP.md": "### Application Layer for Enrich\n\n#### Responsabilidad\nCoordina la ejecución de los casos de uso relacionados con el enriquecimiento de contenido, actuando como intermediario entre los adaptadores y la lógica del dominio. Proporciona una estructura clara para la ejecución de la lógica de negocio a través de los puertos definidos.\n\n#### Relación con otras capas\n- **Es llamado por**: Adaptadores de entrada (Driving Adapters), que usan los puertos de entrada (Driving Ports).\n- **Llama a**: Casos de uso que implementan los puertos de entrada (Driving Ports). Los casos de uso, a su vez, llaman a los puertos de salida (Driven Ports) para interactuar con recursos externos.\n\n#### Ejemplo de Flujo\nUn Driving Adapter llama a un caso de uso a través de un Driving Port:\n```python\nDrivingPort > use case(DrivingPort) > DrivenPort\n```"
            },
            "domain": {
                "entities": {
                    "__init__.py": None,
                    "HELP.md": "### Entities for Enrich\n\n#### Responsabilidad\nRepresentan los objetos clave del dominio relacionados con el enriquecimiento de contenido. Contienen datos y comportamientos esenciales del negocio, independientes de cualquier implementación técnica.\n\n#### Relación con otras capas\n- **Es utilizado por**: Servicios del dominio y casos de uso."
                },
                "events": {
                    "__init__.py": None,
                    "HELP.md": "### Domain Events for Enrich\n\n#### Responsabilidad\nCapturan y representan cambios significativos en el estado del sistema relacionados con el enriquecimiento de contenido (ej. contenido transcrito o enriquecido).\n\n#### Relación con otras capas\n- **Es utilizado por**: Servicios del dominio, casos de uso y adaptadores."
                },
                "services": {
                    "__init__.py": None,
                    "HELP.md": "### Domain Services for Enrich\n\n#### Responsabilidad\nEncapsulan lógica de negocio que no pertenece exclusivamente a una entidad, como validaciones complejas o reglas transversales relacionadas con el enriquecimiento de contenido.\n\n#### Relación con otras capas\n- **Es llamado por**: Casos de uso.\n- **Utiliza**: Entidades y eventos del dominio."
                },
                "__init__.py": None,
                "HELP.md": "### Domain Layer for Enrich\n\n#### Responsabilidad\nContiene la lógica de negocio central y las reglas específicas del enriquecimiento de contenido. Es completamente independiente de cualquier detalle técnico o infraestructura.\n\n#### Relación con otras capas\n- **Es utilizado por**: Casos de uso.\n- **Utiliza**: Entidades, eventos y servicios del dominio."
            },
            "adapters": {
                "driving": {
                    "api": {
                        "__init__.py": None,
                        "HELP.md": "### Driving Adapters for Enrich\n\n#### Responsabilidad\nSon responsables de traducir las solicitudes externas (como usuarios o sistemas) y llamar a los puertos de entrada (Driving Ports) para ejecutar casos de uso relacionados con el enriquecimiento. Exponen los casos de uso al mundo exterior a través de interfaces como APIs REST, manejadores de eventos, entre otros.\n\n#### Relación con otras capas\n- **Es llamado por**: Fuentes externas (usuarios, sistemas).\n- **Llama a**: Puertos de entrada (Driving Ports) implementados por los casos de uso para invocar la lógica de negocio.\n\n#### Ejemplo de Interacción\n```python\n@app.route('/api/enrich/<int:content_id>', methods=['POST'])\ndef enrich_content(content_id):\n    metadata = request.json.get(\"metadata\", {})\n    # Llama al puerto de entrada inyectado como instancia\n    return enrich_port.execute(content_id, metadata)\n```\n\n#### Nota\nLa instancia del Driving Port (`enrich_port`) debe ser inyectada al controlador desde una fábrica o en el punto de configuración de la aplicación. Esto asegura un diseño limpio y desacoplado."
                    }
                },
                "driven": {
                    "repositories": {
                        "__init__.py": None,
                        "HELP.md": "### Driven Repositories for Enrich\n\n#### Responsabilidad\nImplementan las interfaces definidas en los puertos de salida (Driven Ports) para interactuar con sistemas de almacenamiento persistente, como bases de datos o el DAM. Garantizan el desacoplamiento entre la lógica de negocio y la infraestructura de almacenamiento.\n\n#### Relación con otras capas\n- **Es llamado por**: Puertos de salida (Driven Ports) implementados por los casos de uso.\n- **Llama a**: Recursos externos (bases de datos, DAM, etc.).\n\n#### Ejemplo de Interacción\n```python\nclass DAMRepository:\n    def save_metadata(self, content_id, metadata):\n        # Lógica para guardar metadatos en el DAM\n        pass\n```"
                    },
                    "services": {
                        "__init__.py": None,
                        "HELP.md": "### Driven Services for Enrich\n\n#### Responsabilidad\nImplementan las interfaces definidas en los puertos de salida (Driven Ports) para interactuar con servicios externos, como APIs de terceros o sistemas relacionados con el enriquecimiento de contenido. Proporcionan la conexión directa con estos servicios, encapsulando los detalles de implementación.\n\n#### Relación con otras capas\n- **Es llamado por**: Puertos de salida (Driven Ports) implementados por los casos de uso.\n- **Llama a**: Recursos externos (servicios o APIs externas).\n\n#### Ejemplo de Interacción\n```python\nfrom application.ports.driven.enrich_service_port import EnrichServicePort\n\nclass EnrichService(EnrichServicePort):\n    def enrich_metadata(self, metadata):\n        # Lógica para interactuar con un servicio externo de enriquecimiento\n        enriched_metadata = {**metadata, \"tags\": [\"enriched\", \"AI\"]}\n        return enriched_metadata\n```"
                    }
                },
                "__init__.py": None,
                "HELP.md": "### Adapters Layer for Enrich\n\n#### Responsabilidad\nConecta la lógica de negocio del enriquecimiento de contenido con el mundo exterior. Incluye:\n- **Driving Adapters**: Traducen solicitudes externas y llaman a los puertos de entrada (Driving Ports).\n- **Driven Adapters**: Implementan los puertos de salida (Driven Ports) y gestionan las interacciones con recursos externos.\n\n#### Relación con otras capas\n- **Es llamado por**: Fuentes externas (para Driving Adapters) y casos de uso (para Driven Adapters).\n- **Llama a**: Puertos de entrada (Driving Ports) y recursos externos.\n\n#### Ejemplo de Flujo\n- Un Driving Adapter traduce una solicitud externa y llama a un Driving Port para invocar un caso de uso.\n- El caso de uso, a través de un Driven Port, llama a un Driven Adapter que interactúa con recursos externos.\n```"
            },
            "__init__.py": None,
            "HELP.md": "### Enrich Module\n\n#### Responsabilidad\nGestiona la lógica de enriquecimiento de contenido mediante una estructura organizada en capas:\n- **Aplicación**: Coordina casos de uso y puertos.\n- **Dominio**: Contiene la lógica de negocio central y entidades.\n- **Adaptadores**: Manejan la interacción con el mundo exterior.\n\n#### Relación con otras capas\n- **Interactúa con**: La infraestructura para gestionar recursos compartidos como el DAM o tareas asíncronas.\n\n#### Ejemplo\n- Una solicitud externa es manejada por un Driving Adapter, que llama al caso de uso correspondiente a través de un Driving Port. El caso de uso utiliza un Driven Port para interactuar con recursos externos a través de un Driven Adapter.\n```"
        },
        "automate": {
            "application": {
                "ports": {
                    "driving": {
                        "__init__.py": None,
                        "HELP.md": "### Driving Ports for Automate\n\n#### Responsabilidad\nDefinen las interfaces de entrada que son implementadas por los casos de uso en la capa de aplicación. Proporcionan un contrato claro para los adaptadores de entrada (Driving Adapters) para interactuar con la lógica de negocio.\n\n#### Relación con otras capas\n- **Es llamado por**: Adaptadores de entrada (Driving Adapters), como controladores REST, manejadores de eventos o cualquier otra fuente externa.\n- **Es implementado por**: Casos de uso en la misma capa de aplicación.\n\n#### Ejemplo de Interfaz\n```python\nclass AutomatePort:\n    def execute(self, task_id):\n        pass\n ```"
                    },
                    "driven": {
                        "__init__.py": None,
                        "HELP.md": "### Driven Ports for Publish Content\n\n#### Responsabilidad\nDefinen las interfaces de salida utilizadas por los casos de uso para interactuar con recursos externos, como servicios de publicación de contenido en redes sociales, sitios web, o plataformas de terceros. Estas interfaces son implementadas por los adaptadores de salida (Driven Adapters), garantizando un desacoplamiento entre la lógica de negocio y la infraestructura.\n\n#### Relación con otras capas\n- **Es llamado por**: Casos de uso en la misma capa de aplicación para interactuar con recursos externos.\n- **Es implementado por**: Adaptadores de salida (Driven Adapters) en la capa de infraestructura.\n\n#### Ejemplo de Interfaz\n```python\nclass PublishServicePort:\n    def publish_content(self, content_id, metadata):\n        pass\n```"
                    }
                },
                "use_cases": {
                    "__init__.py": None,
                    "HELP.md": "### Use Cases for Publish Content\n\n#### Responsabilidad\nImplementan la lógica de negocio de alto nivel específica de la publicación de contenido. Los casos de uso son responsables de coordinar las interacciones entre los puertos de entrada (Driving Ports) y los puertos de salida (Driven Ports).\n\n#### Relación con otras capas\n- **Implementan**: Los puertos de entrada (Driving Ports).\n- **Usan**: Los puertos de salida (Driven Ports) para interactuar con recursos externos.\n\n#### Ejemplo de Caso de Uso\n```python\nclass PublishContentUseCase(PublishPort):\n    def __init__(self, publish_service_port):\n        self.publish_service_port = publish_service_port\n\n    def execute(self, content_id, metadata):\n        content = {\"content_id\": content_id, \"metadata\": metadata, \"status\": \"publishing\"}\n        # Llama al puerto de salida para realizar la publicación\n        return self.publish_service_port.publish_content(content_id, metadata)\n```"
                },
                "__init__.py": None,
                "HELP.md": "### Application Layer for Automate\n\n#### Responsabilidad\nCoordina la ejecución de los casos de uso relacionados con las tareas de automatización, actuando como intermediario entre los adaptadores y la lógica del dominio. Proporciona una estructura clara para la ejecución de la lógica de negocio a través de los puertos definidos.\n\n#### Relación con otras capas\n- **Es llamado por**: Adaptadores de entrada (Driving Adapters), que usan los puertos de entrada (Driving Ports).\n- **Llama a**: Casos de uso que implementan los puertos de entrada (Driving Ports). Los casos de uso, a su vez, llaman a los puertos de salida (Driven Ports) para interactuar con recursos externos.\n\n#### Ejemplo de Flujo\nUn Driving Adapter llama a un caso de uso a través de un Driving Port:\n```python\nDrivingPort > use case(DrivingPort) > DrivenPort\n```"
            },
                "domain": {
                    "entities": {
                        "__init__.py": None,
                        "HELP.md": "### Entities for Automate Content\n\n#### Responsabilidad\nRepresentan los objetos clave del dominio relacionados con la automatización de contenido. Contienen datos y comportamientos esenciales del negocio, independientes de cualquier implementación técnica.\n\n#### Relación con otras capas\n- **Es utilizado por**: Servicios del dominio y casos de uso.\n\n#### Ejemplo\n```python\nclass Content:\n    def __init__(self, content_id, metadata, status):\n        self.content_id = content_id\n        self.metadata = metadata\n        self.status = status\n```"
                    },
                    "events": {
                        "__init__.py": None,
                        "HELP.md": "### Domain Events for Automate Content\n\n#### Responsabilidad\nCapturan y representan cambios significativos en el estado del sistema relacionados con la automatización de contenido (ej. contenido procesado o actualizado).\n\n#### Relación con otras capas\n- **Es utilizado por**: Servicios del dominio, casos de uso y adaptadores.\n\n#### Ejemplo\n```python\nclass ContentUpdated:\n    def __init__(self, content_id, status):\n        self.content_id = content_id\n        self.status = status\n```"
                    },
                    "services": {
                        "__init__.py": None,
                        "HELP.md": "### Domain Services for Automate Content\n\n#### Responsabilidad\nEncapsulan lógica de negocio que no pertenece exclusivamente a una entidad, como validaciones complejas o reglas transversales relacionadas con la automatización de contenido.\n\n#### Relación con otras capas\n- **Es llamado por**: Casos de uso.\n- **Utiliza**: Entidades y eventos del dominio.\n\n#### Ejemplo\n```python\ndef validate_content(content):\n    if not content.metadata:\n        raise ValueError(\"Content must include metadata\")\n```"
                    },
                    "__init__.py": None,
                    "HELP.md": "### Domain Layer for Automate Content\n\n#### Responsabilidad\nContiene la lógica de negocio central y las reglas específicas de la automatización de contenido. Es completamente independiente de cualquier detalle técnico o infraestructura.\n\n#### Relación con otras capas\n- **Es utilizado por**: Casos de uso.\n- **Utiliza**: Entidades, eventos y servicios del dominio.\n\n#### Ejemplo\n```python\nclass AutomateContentService:\n    def process_content(self, content):\n        content.status = \"processed\"\n```"
                    },
            "adapters": {
                "driving": {
                    "api": {
                        "__init__.py": None,
                        "HELP.md": "### Driving Adapters for Automate\n\n#### Responsabilidad\nSon responsables de traducir las solicitudes externas (como usuarios o sistemas) y llamar a los puertos de entrada (Driving Ports) para ejecutar casos de uso relacionados con las tareas de automatización. Exponen los casos de uso al mundo exterior a través de interfaces como APIs REST, manejadores de eventos, entre otros.\n\n#### Relación con otras capas\n- **Es llamado por**: Fuentes externas (usuarios, sistemas).\n- **Llama a**: Puertos de entrada (Driving Ports) implementados por los casos de uso para invocar la lógica de negocio.\n\n#### Ejemplo de Interacción\n```python\n@app.route('/api/automate/<int:task_id>', methods=['POST'])\ndef automate_task(task_id):\n    task_data = request.json\n    return automate_port.execute(task_id)\n```\n\n#### Nota\nLa instancia del Driving Port (`automate_port`) debe ser inyectada al controlador desde una fábrica o en el punto de configuración de la aplicación. Esto asegura un diseño limpio y desacoplado."
                    }
                },
                "driven": {
                    "repositories": {
                        "__init__.py": None,
                        "HELP.md": "### Driven Repositories for Automate\n\n#### Responsabilidad\nImplementan las interfaces definidas en los puertos de salida (Driven Ports) para interactuar con sistemas de almacenamiento persistente, como bases de datos.\n\n#### Relación con otras capas\n- **Es llamado por**: Puertos de salida (Driven Ports).\n- **Llama a**: Recursos externos (bases de datos, etc.).\n\n#### Ejemplo\n```python\nclass TaskRepository:\n    def save_task(self, task):\n        pass\n```"
                    },
                    "services": {
                        "__init__.py": None,
                        "HELP.md": "### Driven Services for Publish Content\n\n#### Responsabilidad\nImplementan las interfaces definidas en los puertos de salida (Driven Ports) para interactuar con servicios externos relacionados con la publicación de contenido, como APIs de redes sociales, CMS, o servicios de distribución de contenido.\n\n#### Relación con otras capas\n- **Es llamado por**: Puertos de salida (Driven Ports) implementados por los casos de uso.\n- **Llama a**: Recursos externos (servicios o APIs externas).\n\n#### Ejemplo\n```python\nfrom application.ports.driven.publish_service_port import PublishServicePort\n\nclass PublishService(PublishServicePort):\n    def publish_content(self, content_id, metadata):\n        # Lógica para interactuar con un servicio externo de publicación\n        print(f\"Publicando contenido {content_id} con metadatos: {metadata}\")\n        return {\"content_id\": content_id, \"status\": \"published\"}\n```"
                    }
                },
                "__init__.py": None,
                "HELP.md": "### Adapters Layer for Automate\n\n#### Responsabilidad\nConecta la lógica de negocio de automatización con el mundo exterior. Incluye:\n- **Driving Adapters**: Traducen solicitudes externas y llaman a los puertos de entrada (Driving Ports).\n- **Driven Adapters**: Implementan los puertos de salida (Driven Ports) y gestionan las interacciones con recursos externos.\n\n#### Relación con otras capas\n- **Es llamado por**: Fuentes externas (para Driving Adapters) y casos de uso (para Driven Adapters).\n- **Llama a**: Puertos de entrada (Driving Ports) y recursos externos."
            },
            "__init__.py": None,
            "HELP.md": "### Automate Module\n\n#### Responsabilidad\nGestiona la lógica de automatización mediante una estructura organizada en capas:\n- **Aplicación**: Coordina casos de uso y puertos.\n- **Dominio**: Contiene la lógica de negocio central y entidades.\n- **Adaptadores**: Manejan la interacción con el mundo exterior.\n\n#### Relación con otras capas\n- **Interactúa con**: Infraestructura para manejar recursos compartidos, como sistemas de colas o bases de datos."
        },
        "infrastructure": {
            "dam": {
                "__init__.py": None,
                "HELP.md": "### DAM Infrastructure\n\nContiene la lógica para interactuar con el DAM (ResourceSpace), accesible por los adaptadores y casos de uso."
            },
            "celery": {
                "__init__.py": None,
                "HELP.md": "### Celery Infrastructure\n\nIncluye configuración y tareas compartidas para enriquecimiento y automatización."
            },
            "dependencies": {
                "__init__.py": None,
                "HELP.md": "### Dependencies Infrastructure\n\nEste módulo contiene la configuración y definición de dependencias compartidas del proyecto. Es accesible por todas las capas y módulos para centralizar la lógica de inicialización de dependencias comunes, como contenedores de inyección de dependencias, configuraciones globales y otros recursos compartidos."
            },
            "logger": {
                "__init__.py": None,
                "HELP.md": "### Logger Infrastructure\n\nEste módulo contiene la configuración centralizada y lógica para el manejo de logs en el proyecto. \n\n#### Responsabilidades\n- Definir configuraciones estándar de logging (niveles, formatos, handlers, etc.).\n- Proveer un logger reutilizable que pueda ser consumido por cualquier capa o módulo del proyecto.\n\n#### Ejemplo de Uso\nLos módulos o capas pueden importar el logger configurado de esta manera:\n```python\nfrom infrastructure.logger import get_logger\nlogger = get_logger(__name__)\nlogger.info('Esto es un mensaje de log.')\n```\n\n#### Notas\nEl logger debe estar diseñado para ser flexible y soportar múltiples destinos de logs (archivo, consola, servicios externos como ELK o CloudWatch)."
            },
            "__init__.py": None,
            "HELP.md": "### Infrastructure Layer\n\nProporciona herramientas y servicios compartidos como DAM, Celery y logging, accesibles por todos los módulos."
        },
        "tests": {
            "unit": {
                "__init__.py": None,
                "HELP.md": "### Unit Tests\n\nPruebas unitarias para validar componentes individuales de manera aislada."
            },
            "__init__.py": None,
            "HELP.md": "### Tests\n\nIncluye pruebas unitarias y de integración para garantizar la calidad del sistema."
        },
        "__init__.py": None,
        "HELP.md": "### Project Root\n\nCoordinación de los módulos 'enrich' y 'automate', además de infraestructura y pruebas."
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as file:
                if content:
                    file.write(content)

if __name__ == "__main__":
    base_dir = os.path.join(os.getcwd())
    create_structure(base_dir, PROJECT_STRUCTURE)
    print(f"Estructura del proyecto creada en: {base_dir}")

#TODO: Revisar HELP.md de cada archivo y directorio
#TODO: Modificar los ejemplos de driven port  adapter de enrich para que sean de un servicio de transcribir por ejemplo y no de update content