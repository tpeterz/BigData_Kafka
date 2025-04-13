# Real-Time Kafka Music Streaming Analysis

This project demonstrates a simplified real-time data pipeline using **Apache Kafka**, **Flask**, and **Docker** to simulate music streaming events. We look at who’s listening, what they’re listening to, and where they are.

---

## What This Project Does

<<<<<<< HEAD
We created a real-time streaming web app that mimics a music analytics dashboard. Every few seconds, it sends out new simulated music stream events like:

- A user in **Japan** streamed “Glimpse of Us” on **Spotify** feeling **Melancholy**
- Someone in **Colombia** listened to “Tokyo” on **YouTube Music**, skipped it, and rated it **4**
=======
We created a real-time streaming web app that mimics a music analytics dashboard. Every few seconds, it sends out new “fake” music stream events like (for example):
- A user in **Japan** streamed “Glimpse of Us” on **Spotify**
- Someone in **Colombia** listened to “Tokyo” on **YouTube Music** feeling **Melancholy**
>>>>>>> 23807dd411451490c8006ee304212d599bbca6a7

These events are:
- Sent by a Kafka **producer**
- Received by a Kafka **consumer**
- Displayed on a **Flask web interface**
- Filterable by artist, genre, platform, country, mood, rating, or whether the song was skipped

<<<<<<< HEAD
This mimics how real platforms like Spotify or Apple Music analyze listener behavior, using randomized data for educational purposes.
=======
This mimics what real streaming platforms like Spotify might analyze that are simplified and randomized for learning purposes.
>>>>>>> 23807dd411451490c8006ee304212d599bbca6a7

---

## What We Used

| Layer        | Tool/Tech          | Purpose |
|--------------|--------------------|---------|
| Data Stream  | Apache Kafka       | Message broker for real-time event streaming |
| Backend      | Python + Flask     | Web server, consumer integration, filtering |
| Frontend     | HTML + Bootstrap   | Dashboard UI, filtering forms |
| Container    | Docker + Compose   | Orchestration of Kafka services |
| Faker        | Python Faker lib   | Generates realistic but fake user data |

---

## How It Works

### 1. Producer (`producer.py`)
- Uses `Faker` to simulate:
  - `user_id`, `username`, and `email`
  - Song `title`, `artist`, and `genre`
  - Platform like Spotify, YouTube Music, or Apple Music
  - Mood tag (e.g. Chill, Energetic, Sad)
  - `duration` (randomized seconds)
  - `rating` (0 to 5)
  - `skipped` (boolean, yes or no)
- Sends a new message every 2 seconds into the Kafka topic `music-streams`

### 2. Consumer (`consumer.py`)
- Subscribes to `music-streams`
- Consumes data in real time and stores the latest 50 messages in memory
- Outputs each received message to the terminal for inspection

### 3. Flask App (`app.py`)
- Launches a live dashboard on `http://localhost:5000`
- Displays all consumer messages as rows in a Bootstrap-styled table
- Allows filtering by:
  - Artist
  - Genre
  - Platform
  - Country
  - Mood
  - Rating
  - Skipped (yes/no)

The form preserves your selections and automatically refreshes every 5 seconds.

---

## How This Connects to Big Data Class

### Kafka and Big Data Concepts

- Kafka supports **real-time streaming** which is fundamental to Big Data pipelines
- Uses **partitioning** to distribute workload across nodes or brokers
- Messages are **append-only**, ideal for logs, streams, and events
- Enables **loose coupling** between producers and consumers

In our case, music streaming events are fire-and-forget. Producers do not need to know who consumes the data, and consumers can independently scale or process messages however they need to.

#### Kafka Terminology (Simplified)

- **Topic**: A category to which records are sent (like `music-streams`)
- **Partition**: A segment of a topic that allows Kafka to scale horizontally
- **Broker**: A Kafka server that stores messages and serves client requests
- **Producer**: The component that sends messages to a Kafka topic
- **Consumer**: The component that reads from the topic in real time

### Docker and Architecture

Docker Compose runs both Kafka and Zookeeper so you can:
- Set up the broker system locally
- Simulate a multi-component distributed pipeline
- Avoid installing Kafka globally on your machine

This makes the project easy to run, consistent for any user, and close to how microservice-based systems run in industry.

---

## How It Relates to Cassandra and Data Modeling

While our messages are not persisted long-term in a database, if we were using Cassandra or designing a real schema, a good data model might look like:

```sql
CREATE TABLE music_streams_by_user (
    user_id UUID,
    timestamp BIGINT,
    title TEXT,
    artist TEXT,
    genre TEXT,
    mood TEXT,
    platform TEXT,
    duration INT,
    rating INT,
    skipped BOOLEAN,
    city TEXT,
    country TEXT,
    PRIMARY KEY (user_id, timestamp)
);
```

This schema supports:

- High-speed inserts  
- Time-ordered user data  
- Fast access to the most recent activity  
- Grouping data by user or by time range

---

## How to Run the Project

### 1. Start Kafka and Zookeeper with Docker

From the project root:

```bash
docker compose up -d
```

This will run Kafka and Zookeeper in the background.

### 2. Run the Kafka Producer

In a second terminal:

```bash
python producer.py
```

### 3. Run the Flask Web App

In a third terminal:

```bash
python app.py
```

### 4. View the Dashboard

Go to [http://localhost:5000](http://localhost:5000) in your browser. You should see real-time data begin to populate the table. Use the form at the top to filter by any field.

---

## Future Considerations

To push this project further:

- Add persistent storage using Cassandra or PostgreSQL  
- Create graphs or visual analytics (e.g., genre distribution)  
- Use Kafka Connect or Spark Streaming for processing  
- Simulate spikes in traffic or multi-user concurrency  
- Store data in HDFS or S3 for batch analysis  

---

## Team Members

- Hayoung Jung 
- Anjana Madhaven 
- Taylor Peterson 

---

## Summary

This project simulates a simplified Big Data pipeline using Kafka and Flask. It incorporates essential concepts like producers, consumers, brokers, message topics, filtering, and partitioning. Using Docker and Faker makes the system reproducible and easily extensible. The architecture and schema design parallel what you might see in real platforms using Cassandra or distributed systems to analyze user behavior.
