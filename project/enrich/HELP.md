### Enrich Module

#### Responsabilidad
Gestiona la l�gica de enriquecimiento de contenido mediante una estructura organizada en capas:
- **Aplicaci�n**: Coordina casos de uso y puertos.
- **Dominio**: Contiene la l�gica de negocio central y entidades.
- **Adaptadores**: Manejan la interacci�n con el mundo exterior.

#### Relaci�n con otras capas
- **Interact�a con**: La infraestructura para gestionar recursos compartidos como el DAM o tareas as�ncronas.

#### Ejemplo
- Una solicitud externa es manejada por un Driving Adapter, que llama al caso de uso correspondiente a trav�s de un Driving Port. El caso de uso utiliza un Driven Port para interactuar con recursos externos a trav�s de un Driven Adapter.
```