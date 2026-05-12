import json
import random

def lambda_handler(event, context):
    mensajes = ["Acceso validado", "Transaccion exitosa", "Sistema estable"]
    return {
        "statusCode": 200,
        "body": json.dumps({"resultado": random.choice(mensajes)})
    }
