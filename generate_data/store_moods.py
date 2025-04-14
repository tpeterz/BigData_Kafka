import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("FBKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
moods_collection = db.collection("moods")

moods = [
    "Happy", "Sad", "Energetic", "Calm", "Romantic", "Moody",
    "Chill", "Melancholic", "Hype", "Dreamy", "Dark", "Uplifting",
    "Groovy", "Hopeful", "Lo-fi"
]

for mood in moods:
    try:
        doc_id = mood.replace(" ", "_").replace("/", "-")
        moods_collection.document(doc_id).set({
            "name": mood
        })
        print(f"Uploaded: {mood}")
    except Exception as e:
        print(f"Error uploading {mood}: {e}")
