
## Importar librerias necesarias
import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb

## Conectarse al servidor de CouchDB, reemplazar con credenciales propias
URL = 'http://mateo:couchdb@localhost:5984'
print(URL)

try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

## La cadena de conexion se usa para conectarse a la base de datos remota y sera dada por el servidor
## Mas detalles en Read.me....
CLIENT = MongoClient('mongodb+srv://user1:user1@admin.xjcpf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

## Conectarse a MongoDB
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

## Especificar la base de la que se extraeran los datos
DBS=['Tarea1']

## Crear base de destino en couchDB
try:
    dbc=server.create('mongo_destino2')
except:
    dbc=server['mongo_destino2']

## Iterar sobre todos los documentos de la base, obtenerlos y guardarlos en couchDB    
for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = CLIENT[db].list_collection_names()  
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    
                    documents=json.loads(json_util.dumps(x))

                    documents["_id"]=str(documents["_id"]["$oid"])


                    print(documents)
                    doc=dbc.save(documents)

                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  # creating list of skipped documents for later analysis
                    continue    # continue to next document
                except Exception as e:
                    raise e  
