### Logger Infrastructure

Este m�dulo contiene la configuraci�n centralizada y l�gica para el manejo de logs en el proyecto. 

#### Responsabilidades
- Definir configuraciones est�ndar de logging (niveles, formatos, handlers, etc.).
- Proveer un logger reutilizable que pueda ser consumido por cualquier capa o m�dulo del proyecto.

#### Ejemplo de Uso
Los m�dulos o capas pueden importar el logger configurado de esta manera:
```python
from infrastructure.logger import get_logger
logger = get_logger(__name__)
logger.info('Esto es un mensaje de log.')
```

#### Notas
El logger debe estar dise�ado para ser flexible y soportar m�ltiples destinos de logs (archivo, consola, servicios externos como ELK o CloudWatch).