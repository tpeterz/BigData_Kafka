from flask import Flask, redirect, render_template, request, url_for
import firebase_admin
from firebase_admin import credentials, firestore
from uuid import uuid4
import time

app = Flask(__name__)

if not firebase_admin._apps:
    cred = credentials.Certificate("FBKey.json")  
    firebase_admin.initialize_app(cred)

db = firestore.client()

def fetch_stream_events(limit=500):
    try:
        docs = db.collection("stream_events") \
                 .order_by("timestamp", direction=firestore.Query.DESCENDING) \
                 .limit(limit) \
                 .stream()
        return [doc.to_dict() for doc in docs]
    except Exception as e:
        print(f"Error fetching stream_events: {e}")
        return []

@app.route('/')
def index():
    artist = request.args.get('artist', '').lower()
    genre = request.args.get('genre', '').lower()
    platform = request.args.get('platform', '').lower()
    country = request.args.get('country', '').lower()
    mood = request.args.get('mood', '').lower()
    rating = request.args.get('rating', '').strip()
    skipped = request.args.get('skipped', '').lower()
    completed = request.args.get('completed', '').lower()

    sort_by = request.args.get('sort_by', 'timestamp')
    sort_order = request.args.get('sort_order', 'desc')

    messages = fetch_stream_events()
    filtered = []

    genres = sorted([doc.to_dict()['name'] for doc in db.collection("genres").stream()])
    platforms = sorted([doc.to_dict()['name'] for doc in db.collection("platforms").stream()])
    moods = sorted([doc.to_dict()['name'] for doc in db.collection("moods").stream()])

    for msg in messages:
        if artist and artist not in msg['artist'].lower():
            continue
        if genre and genre not in msg['genre'].lower():
            continue
        if platform and platform not in msg['platform'].lower():
            continue
        if country and country not in msg['location']['country'].lower():
            continue
        if mood and mood not in msg.get('mood', '').lower():
            continue
        if rating:
            try:
                if int(msg.get('rating', 0)) < int(rating):
                    continue
            except ValueError:
                continue
        if skipped == 'yes' and not msg.get('is_skipped', False):
            continue
        if skipped == 'no' and msg.get('is_skipped', False):
            continue
        if completed == 'yes' and not msg.get('completed', False):
            continue
        if completed == 'no' and msg.get('completed', False):
            continue

        filtered.append(msg)

    reverse = (sort_order == 'desc')

    def sort_key(msg):
        if sort_by == 'name':
            return msg.get('name', '').lower()
        elif sort_by == 'title':
            return msg.get('title', '').lower()
        elif sort_by == 'artist':
            return msg.get('artist', '').lower()
        elif sort_by == 'genre':
            return msg.get('genre', '').lower()
        elif sort_by == 'platform':
            return msg.get('platform', '').lower()
        elif sort_by == 'city':
            return msg.get('location', {}).get('city', '').lower()
        elif sort_by == 'country':
            return msg.get('location', {}).get('country', '').lower()
        elif sort_by == 'duration_seconds':
            return int(msg.get('duration_seconds', 0))
        elif sort_by == 'listen_position':
            return int(msg.get('listen_position', 0))
        elif sort_by == '%_listened':
            duration = msg.get('duration_seconds', 1)
            return (msg.get('listen_position', 0) / duration) if duration > 0 else 0
        elif sort_by == 'rating':
            return float(msg.get('rating', 0))
        else:
            return msg.get('timestamp', 0)

    filtered = sorted(filtered, key=sort_key, reverse=reverse)

    return render_template('index.html',
                           messages=filtered,
                           genres=genres,
                           platforms=platforms,
                           moods=moods,
                           sort_by=sort_by,
                           sort_order=sort_order)

@app.route('/add', methods=['POST'])
def add_stream_event():
    form = request.form

    event = {
        "user_id": str(uuid4()),
        "name": form['name'],
        "email": form['email'],
        "track_id": str(uuid4()),
        "title": form['title'],
        "artist": form['artist'],
        "genre": form['genre'],
        "timestamp": int(time.time()),
        "platform": form['platform'],
        "location": {
            "city": form['city'],
            "country": form['country']
        },
        "mood": form['mood'],
        "duration_seconds": int(form['duration_seconds']),
        "listen_position": int(form['listen_position']),
        "completed": float(form['listen_position']) / float(form['duration_seconds']) >= .8,
        "rating": int(form['rating']),
        "is_skipped": float(form['listen_position']) / float(form['duration_seconds']) < .8
    }

    event_id = f"{event['user_id']}_{event['track_id']}"
    try:
        db.collection("stream_events").document(event_id).set(event)
        print(f"Stream event stored: {event_id}")
    except Exception as e:
        print(f"Failed to store stream event: {e}")

    song_title = form['title']
    songs_ref = db.collection("songs")
    existing = songs_ref.where("title", "==", song_title).limit(1).stream()
    song_exists = any(existing)

    if not song_exists:
        try:
            new_song_doc = {
                "title": song_title,
                "artist": form['artist'],
                "genre": form['genre']
            }
            doc_id = song_title.replace(" ", "_").replace("/", "-")
            songs_ref.document(doc_id).set(new_song_doc)
            print(f"🎵 Added new song to database: {song_title}")
        except Exception as e:
            print(f"Failed to add song to songs collection: {e}")

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
