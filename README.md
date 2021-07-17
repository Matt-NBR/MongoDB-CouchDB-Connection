## Tarea MongoDB-CouchDB

### Mateo Borja, Karen Hurtado, Stiven López

A continuación se muestran los pasos que permitieron ejecutar el script dado:

#### MongoDB

1.Se creo un cluster y se dió acceso a todos los miembros del grupo como se vió en clase

![image](https://user-images.githubusercontent.com/66144847/126025082-73b8354f-b46c-4eeb-bb7c-282aff2bed76.png)

2.Se conectó al cluster desde MongoDB Compass y se creó una base de datos

![image](https://user-images.githubusercontent.com/66144847/126025109-81d0e3dc-2c99-4eca-9eae-ff20e306f340.png)

3.Cada miembro importó en una colección un data set de Kaggle 

![image](https://user-images.githubusercontent.com/66144847/126025127-6c1dffd6-9c7e-403c-8010-f908779225a6.png)

#### Script

A continuación se describe como se modificó el script para permitir la conexión con la base de datos remota, referirse a los comentarios en el script para ver su funcionamiento

1.La linea que se modificó se muestra a continuación, se trata de la cadena de conexión

![image](https://user-images.githubusercontent.com/66144847/126025218-6eebcd57-a750-4445-be19-6f53202f880e.png)

2.Para obtener esta cadena, se debe ir al cluster creado y seleccionar connect en la base de datos

![image](https://user-images.githubusercontent.com/66144847/126025239-1bfa871c-d843-4409-95c5-32ee14a58e7e.png)

3.Seleccionar conectar con aplicación

![image](https://user-images.githubusercontent.com/66144847/126025250-7a36fc21-028a-4800-8459-073c4682c676.png)

4.Seleccionar el lenguaje y la version

![image](https://user-images.githubusercontent.com/66144847/126025262-b24c81c9-b39f-4ae7-a64c-ac99d1ba8a34.png)

5.Se obtendrá la cadena en la cual solo habrá que reemplazar las credenciales, no es necesario reemplazar la base de prueba a usarse

![image](https://user-images.githubusercontent.com/66144847/126025282-aa6261a0-a35f-490d-85f4-ecf19f3af132.png)

6.Verificar que la base de datos que se va a leer sea la creada en compass (en este caso Tarea1), de lo contrario el script no funcionará
7.Verificar que se haya instalado pymongo, esta es la principal librería que permite extraer los datos. Tambien se deben instalar las dependencias como se indica en la documentación de MongoDB

![image](https://user-images.githubusercontent.com/66144847/126025330-f9a7fc10-f3a5-4870-a703-5ec03d99b2e4.png)

8.Si el script se ejecutó correctamente se mostrarán mensajes de éxito y de los documentos que se vayan extrayendo

![image](https://user-images.githubusercontent.com/66144847/126025356-af640432-68e7-4fec-84f5-585736feca04.png)

Nota: Por motivos de simplicidad y ahorro de tiempo, se detuvo el script ya que extraer 17000 documentos hubiera tardado demasiado

#### CouchDB

Si se ingresa a couchDB se podrá observar la base de datos destino creada

![image](https://user-images.githubusercontent.com/66144847/126025409-5c08f7c2-bf3b-4e9b-9551-5b44cf15dd1c.png)

Y en ella, los datos extraidos de MongoDB

![image](https://user-images.githubusercontent.com/66144847/126025429-27da4865-cbeb-4e3f-adb9-8c2ca0bdcc25.png)

![image](https://user-images.githubusercontent.com/66144847/126025434-40f4f959-5d10-4888-824e-75f037adc965.png)


