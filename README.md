# genero_genero
Análisis del uso de palabras en géneros literarios.

Primero se debe correr `initialize.sh`, que crea los directorios necesarios e instala los paquetes de ubuntu. En requirements.txt se encuentran los paquetes de python.

* `metadatos`. Genera un csv con metadatos de los libros de Gutenberg.
* `download_gutenberg`. Descarga los libros especificados de Proyect Gutenberg.
* `label_terms`. Etiqueta los términos especificados en `terms.txt` en todos los libros y los guarda en una carpeta aparte.
* `train_w2v`. Entrena un modelo Word2Vec a partir de los archivos.
