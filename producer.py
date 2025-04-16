from kafka import KafkaProducer
from faker import Faker
import json, random, time

import firebase_admin
from firebase_admin import credentials, firestore


if not firebase_admin._apps:
    cred = credentials.Certificate("FBkey.json")  
    firebase_admin.initialize_app(cred)

db = firestore.client()

def fetch_firestore_data():
    songs_ref = db.collection("songs").stream()
    platforms_ref = db.collection("platforms").stream()
    moods_ref = db.collection("moods").stream()

    songs = [doc.to_dict() for doc in songs_ref]
    platforms = [doc.to_dict()["name"] for doc in platforms_ref]
    moods = [doc.to_dict()["name"] for doc in moods_ref]

    return songs, platforms, moods

songs, platforms, moods = fetch_firestore_data()

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    track = random.choice(songs)
    duration = random.randint(90, 300)
    listen_position = random.randint(0, duration)
    completed = listen_position / duration >= .8
    rating = random.randint(0, 5)
    is_skipped = not completed

    data = {
        "user_id": fake.uuid4(),
        "name": fake.user_name(),
        "email": fake.email(),
        "track_id": fake.uuid4(),
        "title": track["title"],
        "artist": track["artist"],
        "genre": track["genre"],
        "timestamp": int(time.time()),
        "platform": random.choice(platforms),
        "location": {
            "city": fake.city(),
            "country": fake.country()
        },
        "mood": random.choice(moods),
        "duration_seconds": duration,
        "listen_position": listen_position,
        "completed": completed,
        "rating": rating,
        "is_skipped": is_skipped
    }

    print("Sending to Kafka:", data)
    producer.send("music-streams", data)
    time.sleep(2)
