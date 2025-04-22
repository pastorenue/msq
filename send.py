#!/usr/bin/env python3

import pika
import json

parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',
    credentials=pika.PlainCredentials('guest', 'guest'),    
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')

msg = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

channel.basic_publish(exchange='',
                    routing_key='hello',
                    body=json.dumps(msg))

print(f" [x] Sent {json.dumps(msg)}")

connection.close()