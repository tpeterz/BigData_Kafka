from flask import Flask, render_template, request
import threading
from consumer import received_messages, consume_messages

app = Flask(__name__)

@app.route('/')
def index():
    # Read filters from query params
    artist = request.args.get('artist', '').lower()
    genre = request.args.get('genre', '').lower()
    platform = request.args.get('platform', '').lower()
    country = request.args.get('country', '').lower()
    mood = request.args.get('mood', '').lower()
    rating = request.args.get('rating', '').strip()
    skipped = request.args.get('skipped', '').lower()

    filtered = []
    for msg in received_messages:
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
        if rating and str(msg.get('rating', '')) != rating:
            continue
        if skipped:
            is_skipped = msg.get('skipped', False)
            if skipped == "yes" and not is_skipped:
                continue
            if skipped == "no" and is_skipped:
                continue
        filtered.append(msg)

    return render_template('index.html', messages=filtered)

def start_consumer():
    print("Starting consumer thread from Flask app...")
    consume_messages()

consumer_thread = threading.Thread(target=start_consumer, daemon=True)
consumer_thread.start()

if __name__ == '__main__':
    app.run(debug=True)
