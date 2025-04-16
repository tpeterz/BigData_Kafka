import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("FBKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

genres_collection = db.collection("genres")
songs_collection = db.collection("songs")

predefined_genres = [
    "Classic Rock", "Alt R&B", "Dream Pop", "Alt Pop", "EDM", "Electronica",
    "Psych Rock", "Nu Disco", "Lo-fi Pop", "Chillwave", "Synthpop", "Folktronica",
    "Experimental", "City Pop", "K-pop", "Hip Hop", "J-Pop", "TV Soundtrack",
    "Lo-fi", "Indie Pop", "Indie Rock", "Jazz Fusion", "Pop", "New Age", "Jazz",
    "Latin Pop", "Funk Rock", "Pop Rock", "Funk", "Soft Rock", "Dance Pop",
    "Grunge", "Britpop", "Rock & Roll"
]

def upload_genre(genre_name):
    doc_id = genre_name.replace(" ", "_").replace("/", "-")
    try:
        genres_collection.document(doc_id).set({"name": genre_name})
        print(f"Uploaded genre: {genre_name}")
    except Exception as e:
        print(f"Failed to upload genre '{genre_name}': {e}")

for genre in predefined_genres:
    upload_genre(genre)

song_docs = songs_collection.stream()

existing_genre_ids = set(doc.id for doc in genres_collection.stream())

for doc in song_docs:
    song = doc.to_dict()
    genre = song.get("genre")

    if genre:
        doc_id = genre.replace(" ", "_").replace("/", "-")
        if doc_id not in existing_genre_ids:
            upload_genre(genre)
            existing_genre_ids.add(doc_id)
