import pika

def send_message(queue_name, message):
    credentials = pika.PlainCredentials('juan', 'juan')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()
    
    channel.queue_declare(queue=queue_name)
    
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    print(f" [x] Sent {message}")
    
    connection.close()

if __name__ == "__main__":
    send_message('prueba1', 'Ejemplo de gestor de colas enviado por Gmail - Juan Araujo')
