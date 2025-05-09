from flask import Flask, render_template, request, jsonify
import spacy
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Initialize NLP Model
nlp = spacy.load('en_core_web_sm')

# Geolocation Setup
geolocator = Nominatim(user_agent="community_discovery_bot")

# Sample Data
user_profile = {
    "past_interactions": ["music", "concerts", "art exhibitions"],
    "explicit_preferences": ["fitness", "workshops"],
    "feedback": {"music": 5, "art exhibitions": 3}  # Ratings out of 5
}

all_events = [
    {"title": "Rock Concert", "category": "music", "location": "New York", "date": "this weekend"},
    {"title": "Art Expo", "category": "art", "location": "Los Angeles", "date": "next week"},
    {"title": "Yoga Workshop", "category": "fitness", "location": "San Francisco", "date": "this weekend"},
    {"title": "Food Festival", "category": "food", "location": "Austin", "date": "next weekend"},
    {"title": "Tech Conference", "category": "technology", "location": "Boston", "date": "next month"},
    {"title": "Book Reading", "category": "literature", "location": "Seattle", "date": "this weekend"},
    {"title": "Marathon", "category": "sports", "location": "Chicago", "date": "next month"},
    {"title": "Photography Workshop", "category": "art", "location": "San Diego", "date": "next weekend"},
    {"title": "Classical Music Concert", "category": "music", "location": "Philadelphia", "date": "this weekend"},
    {"title": "Startup Pitch Night", "category": "business", "location": "New York", "date": "next week"}
]

# Extract Entities
def extract_entities(query):
    doc = nlp(query)
    entities = {
        "location": None,
        "time_frame": None,
        "interests": []
    }
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]:
            entities["location"] = ent.text
        elif ent.label_ == "DATE":
            entities["time_frame"] = ent.text
        elif ent.label_ == "NOUN":
            entities["interests"].append(ent.text.lower())
    return entities

# Recommend Events
def recommend_events(entities):
    interest_weights = {interest: user_profile['feedback'].get(interest, 0) for interest in user_profile['past_interactions']}
    filtered_events = [
        event for event in all_events
        if (not entities['location'] or entities['location'].lower() in event['location'].lower()) and
           (not entities['time_frame'] or entities['time_frame'].lower() in event['date'].lower())
    ]
    def score_event(event):
        category = event['category']
        return interest_weights.get(category, 0)
    ranked_events = sorted(filtered_events, key=score_event, reverse=True)
    return ranked_events

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get('query', '')
    entities = extract_entities(user_query)
    recommendations = recommend_events(entities)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
