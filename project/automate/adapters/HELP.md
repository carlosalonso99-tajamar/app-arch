### Adapters Layer for Automate

#### Responsabilidad
Conecta la l�gica de negocio de automatizaci�n con el mundo exterior. Incluye:
- **Driving Adapters**: Traducen solicitudes externas y llaman a los puertos de entrada (Driving Ports).
- **Driven Adapters**: Implementan los puertos de salida (Driven Ports) y gestionan las interacciones con recursos externos.

#### Relaci�n con otras capas
- **Es llamado por**: Fuentes externas (para Driving Adapters) y casos de uso (para Driven Adapters).
- **Llama a**: Puertos de entrada (Driving Ports) y recursos externos.