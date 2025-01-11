### Logger Infrastructure

Este módulo contiene la configuración centralizada y lógica para el manejo de logs en el proyecto. 

#### Responsabilidades
- Definir configuraciones estándar de logging (niveles, formatos, handlers, etc.).
- Proveer un logger reutilizable que pueda ser consumido por cualquier capa o módulo del proyecto.

#### Ejemplo de Uso
Los módulos o capas pueden importar el logger configurado de esta manera:
```python
from infrastructure.logger import get_logger
logger = get_logger(__name__)
logger.info('Esto es un mensaje de log.')
```

#### Notas
El logger debe estar diseñado para ser flexible y soportar múltiples destinos de logs (archivo, consola, servicios externos como ELK o CloudWatch).