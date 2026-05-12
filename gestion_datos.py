import boto3
import uuid
from datetime import datetime
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
nombre_tabla = 'LogsAcceso'
tabla = dynamodb.Table(nombre_tabla)

def insertar_registro(descripcion):
    """Inserta un log de actividad en la tabla"""
    try:
        id_log = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        tabla.put_item(
            Item={
                'id': id_log,
                'evento': descripcion,
                'fecha': timestamp,
                'empresa': 'Soluciones Tecnologicas del Futuro'
            }
        )
        print(f" Registro insertado: {descripcion} (ID: {id_log})")
    except ClientError as e:
        print(f" Error al insertar: {e.response['Error']['Message']}")

def consultar_registros():
    """Lee todos los registros de la tabla"""
    print("\n--- Consultando Base de Datos ---")
    response = tabla.scan()
    items = response.get('Items', [])
    for item in items:
        print(f"Fecha: {item['fecha']} | Evento: {item['evento']}")

if __name__ == "__main__":
    insertar_registro("Inicio de sesion en el sistema financiero")
    insertar_registro("Despliegue de contenedor Docker exitoso")
    consultar_registros()