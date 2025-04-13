from kafka import KafkaProducer
from faker import Faker
import json, random, time

# Initialize faker & Kafka producer
fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Song list
songs = [
    {"title": "Baba O'Riley", "artist": "The Who", "genre": "Classic Rock"},
    {"title": "Limbo", "artist": "Keshi", "genre": "Alt R&B"},
    {"title": "From the Subway Train", "artist": "Vansire", "genre": "Dream Pop"},
    {"title": "Glimpse of Us", "artist": "Joji", "genre": "Alt Pop"},
    {"title": "Levels", "artist": "Avicii", "genre": "EDM"},
    {"title": "Alice", "artist": "Pogo", "genre": "Electronica"},
    {"title": "The Less I Know The Better", "artist": "Tame Impala", "genre": "Psych Rock"},
    {"title": "Lightenup", "artist": "Parcels", "genre": "Nu Disco"},
    {"title": "Without You", "artist": "Avicii", "genre": "EDM"},
    {"title": "Afterthought", "artist": "Joji", "genre": "Lo-fi Pop"},
    {"title": "A Moment Apart", "artist": "ODESZA", "genre": "Chillwave"},
    {"title": "Midnight City", "artist": "M83", "genre": "Synthpop"},
    {"title": "Lovers’ Carvings", "artist": "Bibio", "genre": "Folktronica"},
    {"title": "Tokyo", "artist": "Brockhampton", "genre": "Experimental"},
    {"title": "Angel Baby", "artist": "Troye Sivan", "genre": "Alt Pop"}
]

platforms = ["Spotify", "Apple Music", "YouTube Music", "SoundCloud", "Amazon Music"]

# Send fake data every [2] seconds
while True:
    track = random.choice(songs)
    
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
        }
    }

    print("Sending:", data)
    producer.send("music-streams", data)
    time.sleep(2)
