import os
import json

def lambda_handler(event, context):
    greeting = os.environ.get('greeting', 'Hello, World!')
    
    print(f"Execution environment: {greeting}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': greeting,
            'environment': os.environ.get('environment', 'dev')
        })
    }