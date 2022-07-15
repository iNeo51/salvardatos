Test Tecnico
1.- Se resolveran dos ejecicios dentro de funciones get request, elaboradas en flask, las instrucciones vienen en cada metodo.
2.- Para este inciso se debera instalar Airflow y tambien MongoDB ó Posgres(se valorará más con Mongodb), tambien se podrá hacer usos de servicios de free tier, por ejemplo:  https://www.mongodb.com/cloud/atlas/register
Se creara un flujo que tome un archivo con cualquier tipo de informacion(txt,csv,json) y despues lo cargue en la base de datos de mongo/posgres; se entregarán el archivo .py y capturas de pantalla que se crean convenientes.
pasos:
    a) subir archivo a airflow (DAG).
    b) crear pipeline ó Dag.
    c) cargar datos en base de datos.
    d) leer datos de base de datos.

Algunos Recursos para consultar:
https://airflow.apache.org/
https://hackersandslackers.com/data-pipelines-apache-airflow/
https://airflow.apache.org/docs/apache-airflow-providers-mongo/stable/connections/mongo.html
https://pypi.org/project/apache-airflow-providers-mongo/
