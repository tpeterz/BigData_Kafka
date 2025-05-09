import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("FBkey.json") 
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()
songs_collection = db.collection("songs")

# Songs list (directly included here)
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
    {"title": "More Than Just a Dream", "artist": "Fitz and The Tantrums", "genre": "Indie Pop"},
    {"title": "Waiting For Love", "artist": "Avicii", "genre": "EDM"},
    {"title": "Happy Together", "artist": "The Turtles", "genre": "Pop Rock"},
    {"title": "Kokomo", "artist": "The Beach Boys", "genre": "Surf Rock"},
    {"title": "Uptown Girl", "artist": "Billy Joel", "genre": "Pop"},
    {"title": "Daylight", "artist": "Matt and Kim", "genre": "Indie Pop"},
    {"title": "Beyond the Sea", "artist": "Bobby Darin", "genre": "Jazz"},
    {"title": "Why Can't We Be Friends", "artist": "War", "genre": "Funk"},
    {"title": "Animal", "artist": "Neon Trees", "genre": "Alt Rock"},
    {"title": "Let Her Dance", "artist": "The Bobby Fuller Four", "genre": "Rock & Roll"},
    {"title": "Sunshine, Lollipops And Rainbows", "artist": "Lesley Gore", "genre": "Pop"},
    {"title": "Rasputin", "artist": "Boney M.", "genre": "Disco"},
    {"title": "We Found Love", "artist": "Rihanna, Calvin Harris", "genre": "Pop"},
    {"title": "Thinkin Bout You", "artist": "Frank Ocean", "genre": "Alt R&B"},
    {"title": "Yesterday - Remastered 2009", "artist": "The Beatles", "genre": "Classic Rock"},
    {"title": "Talk Too Much", "artist": "COIN", "genre": "Indie Pop"},
    {"title": "Everybody Wants To Rule The World", "artist": "Tears For Fears", "genre": "New Wave"},
    {"title": "I Ran (So Far Away)", "artist": "A Flock Of Seagulls", "genre": "Synthpop"},
    {"title": "Talking In Your Sleep", "artist": "The Romantics", "genre": "Rock"},
    {"title": "(I Just) Died In Your Arms", "artist": "Cutting Crew", "genre": "Pop Rock"},
    {"title": "Waiting for a Girl Like You", "artist": "Foreigner", "genre": "Soft Rock"},
    {"title": "Come As You Are", "artist": "Nirvana", "genre": "Grunge"},
    {"title": "Don't Speak", "artist": "No Doubt", "genre": "Alt Rock"},
    {"title": "Believe", "artist": "Cher", "genre": "Dance Pop"},
    {"title": "I Want It That Way", "artist": "Backstreet Boys", "genre": "Pop"},
    {"title": "Californication", "artist": "Red Hot Chili Peppers", "genre": "Alt Rock"},
    {"title": "Iris", "artist": "The Goo Goo Dolls", "genre": "Alt Rock"},
    {"title": "There She Goes", "artist": "The La's", "genre": "Britpop"},
    {"title": "Under the Bridge", "artist": "Red Hot Chili Peppers", "genre": "Alt Rock"},
    {"title": "Holding Out for a Hero", "artist": "Bonnie Tyler", "genre": "Rock"},
    {"title": "Don't Stop Me Now", "artist": "Queen", "genre": "Classic Rock"}
]

# Upload to Firestore
for song in songs:
    try:
        doc_id = song["title"].replace(" ", "_").replace("/", "-")
        songs_collection.document(doc_id).set({
            "title": song["title"],
            "artist": song["artist"],
            "genre": song["genre"]
        })
        print(f"Uploaded: {song['title']}")
    except Exception as e:
        print(f"Error uploading {song['title']}: {e}")
