from flask import Flask, render_template
import threading
import time

app = Flask(__name__)

# this guy STORES the Kafka messages
stored_data = []

@app.route("/")
def index():
    # last 20 shown for now
    return render_template("index.html", messages=stored_data[-20:])  

if __name__ == "__main__":
    app.run(debug=True)
