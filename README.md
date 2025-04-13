from pathlib import Path

readme_content = """
# Real-Time Kafka Music Streaming Analysis

This project demonstrates a simplified real-time data pipeline using **Apache Kafka**, **Flask**, and **Docker** to simulate music streaming events — who’s listening, what they’re listening to, and where they are.

---

## What This Project Does

We created a real-time streaming web app that mimics a music analytics dashboard. Every few seconds, it sends out new “fake” music stream events like:
- A user in **Japan** streamed “Glimpse of Us” on **Spotify**
- Someone in **Colombia** listened to “Tokyo” on **YouTube Music** feeling **Melancholy**

These events are:
- Sent by a Kafka **producer**
- Received by a Kafka **consumer**
- Displayed on a **Flask web interface**
- Filterable by artist, platform, genre, mood, or country

This mimics what real streaming platforms like Spotify might analyze — just simplified and randomized for learning purposes.

---

## What We Used

| Layer        | Tool/Tech          | Purpose |
|--------------|--------------------|---------|
| Data Stream  | Apache Kafka       | Message broker for real-time data |
| Backend      | Python + Flask     | Web server and message filtering |
| Frontend     | HTML + Bootstrap   | Live dashboard interface |
| Container    | Docker + Compose   | Simplified multi-service setup |
| Faker        | Python Faker lib   | Randomly generates realistic data |

---

## How It Works

### 1. Producer (`producer.py`)
- Uses `Faker` to generate **users**, **songs**, **locations**, and **moods**
- Randomly emits music stream events into a Kafka **topic** called `music-streams`

### 2. Consumer (`consumer.py`)
- Subscribes to the `music-streams` topic
- Collects messages as they arrive and stores them in memory
- Feeds them to the Flask frontend in real time

### 3. Flask App (`app.py`)
- Hosts a dashboard on `localhost:5000`
- Displays messages in a table that updates live
- Lets you **filter** by artist, genre, mood, platform, or country

---

## How This Connects to Big Data Class

### Kafka = Big Data Streaming
- Like Cassandra, Kafka uses **partitioning** for distributing data.
- Each message goes to a **partition** based on a hash of the key (`user_id`).
- Kafka is **append-only** and handles real-time ingest like logs or song plays.

### Cassandra-Like Data Modeling

If we were storing the data long-term, it might look like this:

```sql
CREATE TABLE music_streams_by_user (
    user_id UUID,
    timestamp BIGINT,
    title TEXT,
    artist TEXT,
    genre TEXT,
    mood TEXT,
    platform TEXT,
    city TEXT,
    country TEXT,
    PRIMARY KEY (user_id, timestamp)
);
