from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://rickandmortyapi.com/api/character/"

# Function to fetch characters based on criteria
def fetch_characters(criteria=None):
    filtered_characters = []
    page = 1

    while True:
        response = requests.get(f"{BASE_URL}?page={page}")
        if response.status_code != 200:
            return {"error": "Unable to fetch data from API"}, 500

        data = response.json()

        for character in data['results']:
            if criteria == "human":
                if character['species'] == "Human":
                    filtered_characters.append({
                        "Name": character['name'],
                        "Location": character['location']['name'],
                        "Image": character['image']
                    })
            elif criteria == "alive":
                if character['status'] == "Alive":
                    filtered_characters.append({
                        "Name": character['name'],
                        "Location": character['location']['name'],
                        "Image": character['image']
                    })
            elif criteria == "earth":
                # Check if 'origin' or 'location' contains the word 'Earth'
                if ('Earth' in character.get('origin', {}).get('name', '') or 
                    'Earth' in character['location']['name']):
                    filtered_characters.append({
                        "Name": character['name'],
                        "Location": character['location']['name'],
                        "Image": character['image']
                    })

        if not data['info']['next']:
            break

        page += 1
    
    return filtered_characters

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "ok"}), 200

@app.route('/characters/human', methods=['GET'])
def get_human_characters():
    characters = fetch_characters(criteria="human")
    return jsonify(characters), 200

@app.route('/characters/alive', methods=['GET'])
def get_alive_characters():
    characters = fetch_characters(criteria="alive")
    return jsonify(characters), 200

@app.route('/characters/earth', methods=['GET'])
def get_earth_characters():
    characters = fetch_characters(criteria="earth")
    return jsonify(characters), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

