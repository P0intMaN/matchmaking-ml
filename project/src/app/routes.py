from flask import render_template, request, jsonify
from app import flask_app
from sentence_transformers import SentenceTransformer
import numpy as np


def compute_similarity(string1, string2):

    # Define the pre-trained model
    model = SentenceTransformer('bert-base-nli-mean-tokens', cache_folder='cache_models/')

    # Get embeddings for the two strings
    embeddings = model.encode([string1, string2])

    # Calculate cosine similarity between the two embeddings
    similarity = np.dot(embeddings[0], embeddings[1]) / (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))

    if similarity < 0.5:
        return 0
    
    return 1


# Render the HTML form for input
@flask_app.route('/')
def home():
    return render_template('home.html', result= '')

# Receive the form data and run the matchmaking algorithm
@flask_app.route('/match', methods=['POST'])
def match():
    profile1 = request.form['profile1']
    profile2 = request.form['profile2']
    result = compute_similarity(profile1, profile2)
    print(result)
    return jsonify({
        'result' : result
    })

