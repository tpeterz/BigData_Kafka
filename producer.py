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
    {"title": "Angel Baby", "artist": "Troye Sivan", "genre": "Alt Pop"},
    {"title": "Friday Chinatown", "artist": "FRIDAY CHINATOWN", "genre": "City Pop"},
    {"title": "YESTERDAY", "artist": "BLOCK B", "genre": "K-pop"},
    {"title": "CHEER UP", "artist": "TWICE", "genre": "K-pop"},
    {"title": "Bulletproof", "artist": "Laure, GASPER, DAIGON", "genre": "Hip Hop"},
    {"title": "Pop Food", "artist": "Jack Stauber", "genre": "Alt Pop"},
    {"title": "Jump", "artist": "Van Halen", "genre": "Classic Rock"},
    {"title": "Count What You Have Now", "artist": "Vontmer", "genre": "J-Pop"},
    {"title": "Gravity Falls", "artist": "Brad Breeck", "genre": "TV Soundtrack"},
    {"title": "bee.", "artist": "groove.dominic0254", "genre": "Lo-fi"},
    {"title": "Pumped Up Kicks", "artist": "Foster the People", "genre": "Indie Pop"},
    {"title": "Gilbert Grapes (feat. Neal Crea)", "artist": "Cricketbow & The Dead Coast", "genre": "Indie Rock"},
    {"title": "Handshakes & Solution", "artist": "Cricketbow & The Dead Coast", "genre": "Indie Rock"},
    {"title": "on my puter", "artist": "Cowboy", "genre": "Experimental"},
    {"title": "Circle Jazz", "artist": "Maat", "genre": "Jazz Fusion"},
    {"title": "Money, Money, Money", "artist": "ABBA", "genre": "Pop"},
    {"title": "Orinoco Flow", "artist": "Enya", "genre": "New Age"},
    {"title": "Susto Two-to-Fit - Cover", "artist": "Beats & Pieces", "genre": "Jazz"},
    {"title": "MASCARA", "artist": "RANIA", "genre": "K-pop"},
    {"title": "Lay All Your Love on Me", "artist": "ABBA", "genre": "Pop"},
    {"title": "Hero", "artist": "Enrique Iglesias", "genre": "Latin Pop"},
    {"title": "Come and Get Your Love", "artist": "Redbone", "genre": "Funk Rock"},
    {"title": "The Girl I Want Most", "artist": "Kishi Bashi", "genre": "Indie Pop"},
    {"title": "Alive", "artist": "Empire of the Sun", "genre": "Synthpop"},
    {"title": "Girls Just Want to Have Fun", "artist": "Cyndi Lauper", "genre": "Pop Rock"},
    {"title": "Tokyo (Vocal)", "artist": "Yasuha", "genre": "City Pop"},
    {"title": "Shining on E Wis", "artist": "Fujii Kaze", "genre": "J-Pop"},
    {"title": "GOING CRAZY", "artist": "TREASURE", "genre": "K-pop"},
    {"title": "Demons - 2008 Remaster", "artist": "The Fatback Band", "genre": "Funk"},
    {"title": "More Than Just a Dream", "artist": "Fitz and The Tantrums", "genre": "Indie Pop"}
]

platforms = ["Spotify", "Apple Music", "YouTube Music", "SoundCloud", "Amazon Music"]

# NEW adding moods for filtering (going to be randomly assignned by faker)
moods = [
    "Happy", "Sad", "Energetic", "Calm", "Romantic", "Moody",
    "Chill", "Melancholic", "Hype", "Dreamy", "Dark", "Uplifting",
    "Groovy", "Hopeful", "Lo-fi"
]
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
        },
        "mood": random.choice(moods)
    }

    print("Sending:", data)
    producer.send("music-streams", data)
    time.sleep(2)
