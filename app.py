import os
import pickle
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, render_template, request
from dotenv import load_dotenv # <-- NEW: Import the library

# --- NEW: Load the .env file ---
# This line looks for a .env file and loads the variables from it.
load_dotenv()

# --- Initialize Flask App ---
app = Flask(__name__)

# --- Load Model Files ---
try:
    songs_df = pd.DataFrame(pickle.load(open('songs_dict.pkl', 'rb')))
    similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))
    popular_df = pickle.load(open('popular.pkl', 'rb'))
except FileNotFoundError:
    print("ERROR: Model files not found. Please ensure .pkl files are in the same directory.")
    exit()

# --- Spotify API Setup (Secure Method using .env) ---
# This code now reads the keys loaded from your .env file.
try:
    client_credentials_manager = SpotifyClientCredentials(
        client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
        client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET')
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    # This line confirms the connection was successful.
    sp.search(q='test', type='track', limit=1) 
    print("--- Successfully connected to Spotify API ---")
except Exception as e:
    sp = None
    print("\n" + "="*60)
    print("!!! WARNING: COULD NOT CONNECT TO SPOTIFY API !!!")
    print(f"The error was: {e}")
    print("\nThis means there is likely an issue with the keys in your .env file.")
    print("Please ensure the .env file is saved in the same folder as app.py and that the keys are correct.")
    print("="*60 + "\n")


# --- Helper Function to Get Track Details ---
def get_track_details(track_id):
    if not sp:
        return {"image_url": "https://placehold.co/600x400/ef4444/ffffff?text=API+Connection+Failed"}
    
    try:
        track = sp.track(track_id)
        image_url = track['album']['images'][0]['url'] if track['album']['images'] else "https://placehold.co/300x300/cccccc/ffffff?text=No+Image"
        return {"image_url": image_url, "id": track_id}
    except Exception:
        return {"image_url": "https://placehold.co/600x400/fbbf24/ffffff?text=Track+Info+Error", "id": track_id}

# --- Flask Routes ---

@app.route('/')
def index():
    top_50_with_images = []
    for _, row in popular_df.iterrows():
        details = get_track_details(row['id'])
        top_50_with_images.append({
            'name': row['name'],
            'artists': str(row['artists']).strip("[]'"),
            'id': row['id'],
            'image_url': details['image_url']
        })
    return render_template('index.html', songs=top_50_with_images)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    recommendations_with_images = []
    error_message = None
    user_song = None

    if request.method == 'POST':
        user_song = request.form.get('song_name')
        if user_song not in songs_df['name'].values:
            error_message = f"Sorry, '{user_song}' was not found in our dataset. Please check the spelling or try another song."
        else:
            song_index = songs_df[songs_df['name'] == user_song].index[0]
            similarity_scores = list(enumerate(similarity_matrix[song_index]))
            sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
            top_songs_indices = [i[0] for i in sorted_scores[1:11]]
            
            recommended_data = songs_df.iloc[top_songs_indices]

            for _, row in recommended_data.iterrows():
                details = get_track_details(row['id'])
                recommendations_with_images.append({
                    'name': row['name'],
                    'artists': str(row['artists']).strip("[]'"),
                    'id': row['id'],
                    'image_url': details['image_url']
                })

    return render_template('recommend.html', 
                           song_names=list(songs_df['name']), 
                           recommendations=recommendations_with_images,
                           error_message=error_message,
                           user_song=user_song)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

