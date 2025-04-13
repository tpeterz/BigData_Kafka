from kafka import KafkaConsumer
import json
from app import stored_data 

consumer = KafkaConsumer(
    'music-streams',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='music-group'
)

print("Listening for messages on 'music-streams'...\n")
for message in consumer:
    data = message.value
    stored_data.append(data)
    print(f"Received: {data}")
