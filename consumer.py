from kafka import KafkaConsumer
import json

# Create Kafka consumer
consumer = KafkaConsumer(
    'music-streams',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='music-group'
)

# Shared list to store messages
received_messages = []

def consume_messages():
    global received_messages  # <- ensures shared access
    for message in consumer:
        data = message.value
        print(f"Received: {data}")
        received_messages.append(data)
        if len(received_messages) > 50:
            received_messages.pop(0)
