### Enrich Module

#### Responsabilidad
Gestiona la lógica de enriquecimiento de contenido mediante una estructura organizada en capas:
- **Aplicación**: Coordina casos de uso y puertos.
- **Dominio**: Contiene la lógica de negocio central y entidades.
- **Adaptadores**: Manejan la interacción con el mundo exterior.

#### Relación con otras capas
- **Interactúa con**: La infraestructura para gestionar recursos compartidos como el DAM o tareas asíncronas.

#### Ejemplo
- Una solicitud externa es manejada por un Driving Adapter, que llama al caso de uso correspondiente a través de un Driving Port. El caso de uso utiliza un Driven Port para interactuar con recursos externos a través de un Driven Adapter.
```