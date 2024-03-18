import boto3

def send_email(sender_email, recipient_email, subject, body):
    # Substitua 'SEU_ACCESS_KEY' e 'SEU_SECRET_KEY' pelas suas credenciais da AWS
    session = boto3.Session(
        aws_access_key_id= 'XXXXXXXXXXXXXXX',      
        aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        region_name='us-east-1'  # Substitua a região pela desejada
    )

    # Crie um cliente SES a partir da sessão
    ses_client = session.client('ses')

    # Tente enviar o e-mail
    try:
        response = ses_client.send_email(
            Source=sender_email,
            Destination={
                'ToAddresses': [recipient_email]
            },
            Message={
                'Subject': {
                    'Data': subject
                },
                'Body': {
                    'Text': {
                        'Data': body
                    }
                }
            }
        )
        print("E-mail enviado! ID da mensagem:", response['MessageId'])
    except Exception as e:
        print("Ocorreu um erro ao enviar o e-mail:", e)

# Insira suas informações aqui
sender_email = 'xyz@zyx.com'
recipient_email = 'abc@zyx.com'
subject = 'Teste de e-mail via SES da AWS python'
body = 'Este é um teste de envio de e-mail via SES da AWS usando Python.'


send_email(sender_email, recipient_email, subject, body)
