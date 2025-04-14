import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("FBKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
platforms_collection = db.collection("platforms")

platforms = ["Spotify", "Apple Music", "YouTube Music", "SoundCloud", "Amazon Music"]

for platform in platforms:
    try:
        doc_id = platform.replace(" ", "_")
        platforms_collection.document(doc_id).set({
            "name": platform
        })
        print(f"Uploaded: {platform}")
    except Exception as e:
        print(f"Error uploading {platform}: {e}")
