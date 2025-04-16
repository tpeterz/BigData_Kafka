import json
from kafka import KafkaConsumer
import time

# Create Kafka consumer
consumer = KafkaConsumer(
    'music-streams',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='music-group'
)

received_messages = []
from kafka import KafkaConsumer
import firebase_admin
from firebase_admin import credentials, firestore
import json

if not firebase_admin._apps:
    cred = credentials.Certificate("FBkey.json")  
    firebase_admin.initialize_app(cred)
db = firestore.client()

consumer = KafkaConsumer(
    'music-streams',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='music-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)


for message in consumer:
    data = message.value
    try:
        doc_id = f"{data['user_id']}_{data['track_id']}"
        db.collection("stream_events").document(doc_id).set(data)
        print(f"Stored in Firestore: {doc_id}")
    except Exception as e:
        print("Firestore error:", e)

    time.sleep(2)

def consume_messages():
    global received_messages
    for message in consumer:
        try:
            data = message.value

            print(f"Received: {data}")
            received_messages.append(data)

            if len(received_messages) > 50:
                received_messages.pop(0)
        except Exception as e:
            print("Error processing message:", e)
