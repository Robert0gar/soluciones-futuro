import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2', region_name='us-east-1')
s3 = boto3.client('s3')
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

def generar_reporte():
    print(f"=== REPORTE DE RECURSOS - {datetime.now()} ===")
    
    print("\n[Instancias EC2]")
    instancias = ec2.describe_instances()
    for reserva in instancias['Reservations']:
        for i in reserva['Instances']:
            print(f"ID: {i['InstanceId']} | Estado: {i['State']['Name']} | Tipo: {i['InstanceType']}")

    print("\n[Buckets S3]")
    buckets = s3.list_buckets()
    for b in buckets['Buckets']:
        print(f"Nombre: {b['Name']}")


    print("\n[Monitoreo CloudWatch]")
    print("Obteniendo métricas de los últimos 30 minutos...")

if __name__ == "__main__":
    generar_reporte()