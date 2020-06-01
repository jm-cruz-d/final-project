# De Madrid al cielo

De Madrid al cielo es un proyecto que permite mediante el machine learning el reconocimiento de fachadas de los edificios más representativos de la ciudad de Madrid.

![Alt text](images/pres.jpg?raw=true "Title" | width=50%)

El primer paso fue la creación de la base de datos a partir de imagenes descargadas de google, así como la extracción de frames de videos realizados al edificio y de videos en time lapse. Una vez creada la base de datos se realiza un proceso de data cleaning.

Una vez se tiene la base de datos en condiciones optimas se entrena el modelo usando las librerias Keras y Tensorflow, mediante la plataforma de google colab. La red neuronal utilizada entrena con 5 capas, unas dimensiones de 32, 64 y 128 pixeles y un kernel de (3,3).

Con ello se obtuvo un porcentaje de acierto del 96% y para su aplicación se ha desarrollado una api donde puedes insertar la imagen que quieres comprobar.

![Alt text](images/api.jpg?raw=true "Title2" | width=50%)

Los siguientes pasos a desarrollar serían la ampliación de la base de datos incluyendo más edificios y otras ciudades, subirlo a heroku y desarrollar una aplicación para su uso en móviles, entre otros.
