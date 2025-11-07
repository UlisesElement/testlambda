import os

def lambda_handler(event, context):
    file_path = os.path.join(os.path.dirname(__file__), '../archivo.txt')
    a = 1
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            contenido = f.read()
        return {
            'statusCode': 200,
            'body': contenido
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error al leer el archivo  : {str(e)}'
        }
