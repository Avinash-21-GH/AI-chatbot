from flask import Flask, request, jsonify, render_template
import sqlite3
import re

app = Flask(__name__)
app.secret_key = "hitam_secret"

verified_emails = set()

def get_info(topic):
    conn = sqlite3.connect('database/chatbot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM info WHERE topic = ?", (topic,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else "Sorry, I couldn't find that info."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get("message", "").lower()
    email = data.get("email", "")

    # Validate Gmail format and verify the email
    if email:
        if re.match(r"[^@]+@gmail\.com$", email):
            # Add the email to the verified set if not already present
            verified_emails.add(email)
        else:
            return jsonify({"response": "Please enter a valid Gmail to continue chatting."})

    # Ensure the email is verified before allowing further conversation
    if not email or email not in verified_emails:
        return jsonify({"response": "Please enter a valid Gmail to continue chatting."})

    # Handling greetings
    greetings = ["hi", "hello", "hey", "good morning", "good evening", "greetings"]
    if any(greet in user_msg for greet in greetings):
        return jsonify({"response": "Hello! How can I help you with HITAM College information today?"})

    # Mapping user messages to topics in the database
    keywords = {
        "location": "location",
        "faculty": "faculty",
        "department": "departments",
        "fee": "fees",
        "lab": "labs",
        "sports": "sports",
        "hygiene": "hygiene",
        "block": "blocks",
        "transport": "transport",
        "placement": "placements",
        "education": "education",
        "hostel": "hostel",
        "canteen": "canteen",
        "library": "library",
        "events": "events",
        "timings": "timings"
    }

    # Check for keyword and return corresponding info
    for key, topic in keywords.items():
        if key in user_msg:
            return jsonify({"response": get_info(topic)})

    return jsonify({"response": "Sorry, I didn't understand. Try asking about faculty, fees, placements, or other topics."})

if __name__ == '__main__':
    app.run(debug=True)
