### Adapters Layer for Enrich

#### Responsabilidad
Conecta la l�gica de negocio del enriquecimiento de contenido con el mundo exterior. Incluye:
- **Driving Adapters**: Traducen solicitudes externas y llaman a los puertos de entrada (Driving Ports).
- **Driven Adapters**: Implementan los puertos de salida (Driven Ports) y gestionan las interacciones con recursos externos.

#### Relaci�n con otras capas
- **Es llamado por**: Fuentes externas (para Driving Adapters) y casos de uso (para Driven Adapters).
- **Llama a**: Puertos de entrada (Driving Ports) y recursos externos.

#### Ejemplo de Flujo
- Un Driving Adapter traduce una solicitud externa y llama a un Driving Port para invocar un caso de uso.
- El caso de uso, a trav�s de un Driven Port, llama a un Driven Adapter que interact�a con recursos externos.
```