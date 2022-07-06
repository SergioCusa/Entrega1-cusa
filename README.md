## Contenido
1. [Informacion general](#informacion-general)
2. [Instalacion](#instalacion)
3. [Uso](#uso)

### Informacion general
El poyecto cuenta con un entorno virtual "venv", una carpeta con los templates y
una app creada para vistas,urls,models y forms llamada "Blog"

### instalacion
Para un correcto funcionamiento del proyecto en el mismo se encuentra elarchivo
"requirements.txt". Este contiene las versiones actualizadas de los programas neceasarios
para correr el blog.

### Uso
En la parte superior de la pantalla de inicio se encuentran dos botones:  
Inicio: Vuelve a cargar la pantalla de inicio  
Instrumentos: Devuelve un listado de instrumetos cargados en la Bd, el mismo template    cuenta con un buscador y un boton para gargar instrumentos.      
Para buscar un elemento escriba la palabra clave y precione "Buscar", esto devolvera un   listado con las coincidencias encontradas, de no encontrar ninguna devolvera el mensaje "No se encontraron resultados", precione "Buscar"nuevamente para volver al listado.  
Para ingresar un elemento a la lista precione en "Cargar instrumento" y podra llenar 3   campos:  
-Nombre: ingrese nombre del instrumento  
-Tipo: ingrese el tipo de instrumento (viento,cuerda,percusion,etc)  
-Fecha: ingrese la fecha de creacion del elemento, de no ingresar un valor en este campo el mismo se completara automaticamente.

