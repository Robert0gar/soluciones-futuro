import boto3
from datetime import datetime

ec2 = boto3.client('ec2', region_name='us-east-1')
s3 = boto3.client('s3')
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
asg = boto3.client('autoscaling', region_name='us-east-1')
iam = boto3.client('iam')

def generar_reporte():
    print(f"=== REPORTE DE INFRAESTRUCTURA Y GESTION - {datetime.now()} ===")
    
    print("\n[Instancias EC2]")
    instancias = ec2.describe_instances()
    for reserva in instancias['Reservations']:
        for i in reserva['Instances']:
            print(f"ID: {i['InstanceId']} | Estado: {i['State']['Name']} | Tipo: {i['InstanceType']}")

    print("\n[Buckets S3]")
    buckets = s3.list_buckets()
    for b in buckets['Buckets']:
        print(f"Nombre: {b['Name']}")

    print("\n[Gestion de Auto Scaling Groups]")
    grupos = asg.describe_auto_scaling_groups()
    if not grupos['AutoScalingGroups']:
        print("No se detectaron grupos de Auto Scaling activos.")
    else:
        for g in grupos['AutoScalingGroups']:
            print(f"Grupo: {g['AutoScalingGroupName']} | Capacidad Deseada: {g['DesiredCapacity']}")

    print("\n[Auditoria de Usuarios y Seguridad]")
    usuarios = iam.list_users()
    for u in usuarios['Users']:
        print(f"Usuario: {u['UserName']} | Ultimo Acceso: {u.get('PasswordLastUsed', 'N/A')}")

    print("\n[Estado de CloudWatch]")
    alarmas = cloudwatch.describe_alarms()
    for a in alarmas['MetricAlarms']:
        print(f"Alarma: {a['AlarmName']} | Estado: {a['StateValue']}")

if __name__ == "__main__":
    generar_reporte()