import pika
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    ##En esta parte se deben de ingresar las credenciales para que pueda funcionar correctamente
    from_email = "**@gmail.com"
    from_password = "***"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    send_email("New Message", body.decode(), "destinatario@example.com")

def start_consuming(queue_name):
    credentials = pika.PlainCredentials('juan', 'juan') 
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()
    
    channel.queue_declare(queue=queue_name)
    
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    start_consuming('prueba1')
