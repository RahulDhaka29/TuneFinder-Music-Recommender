# 🎵 TuneFinder - Music Recommendation System

**TuneFinder** is a content-based music recommendation system built with **Python, Flask, Scikit-learn**, and the **Spotify API**.  
Enter a song you like, and get recommendations for 5 other songs with similar audio features! 🎶

---

## ✨ Features

- 🎧 **Content-Based Recommendations:**  
  Recommends songs based on their intrinsic audio features (like danceability, energy, tempo, valence, etc.) using cosine similarity.

- 🖼️ **Spotify Integration:**  
  Fetches real-time album cover art and metadata using the Spotify Web API.

- 💻 **Interactive UI:**  
  A clean, modern, and responsive web interface built using **Flask** and **Tailwind CSS**.

- 🔗 **"Listen on Spotify" Links:**  
  Provides direct links to play the recommended tracks on the Spotify platform.

- 🏆 **Top 50 Popular Songs:**  
  The homepage showcases a curated list of the **50 most popular tracks** from the processed dataset.

---

## 📁 Project Structure

```
/tunefinder-music-recommender/
|-- app.py                          # Main Flask application logic
|-- songs_dict.pkl                  # Processed song data (DataFrame as dictionary)
|-- scaled_features.npy             # Scaled audio features (NumPy array) - Used for on-the-fly similarity
|-- popular.pkl                     # Top 50 popular songs data (DataFrame)
|-- music-recommendation-system.ipynb # Jupyter notebook for model building & EDA
|-- README.md                       # This file
|-- .env                            # File for storing API keys (IMPORTANT: Add to .gitignore)
|-- requirements.txt                # List of Python dependencies
|-- /templates/
|   |-- index.html                  # Homepage template (Top 50)
|   |-- recommend.html              # Recommendation page template
|   |-- about.html                  # About page template
|   |-- contact.html                # Contact page template

---
## Dataset 📊

This project uses the "120 years of Olympic history, athletes and results" dataset.

**Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)

**Required Files:** To run the analysis notebook (`olympics_analysis.ipynb`), you must first download the following files from the Kaggle link above and place them in the main project directory:
* `athlete_events.csv`
* `noc_regions.csv`

## ⚙️ Setup and Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/tunefinder-music-recommender.git
cd tunefinder-music-recommender
```

> Replace `your-username` with your actual GitHub username.

---

### 2️⃣ Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
```

#### On Windows:
```bash
.env\Scriptsctivate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Get Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in and **create a new application**.
3. Note down your **Client ID** and **Client Secret**.
4. In your app settings, add the following as a Redirect URI:
   ```
   http://127.0.0.1:5000/
   ```
   (or your local development URL)

---

### 5️⃣ Set Environment Variables

Create a file named `.env` in the project’s root directory (same level as `app.py`). Add your credentials:

```env
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
```

> ⚠️ **Important:** Add `.env` to your `.gitignore` file to prevent accidental commits of your API keys.

---

## 🚀 How to Run

1. Ensure model files `songs_dict.pkl`, `scaled_features.npy`, and `popular.pkl` are present in the root directory.  
   If not, run the **`music-recommendation-system.ipynb`** notebook to generate them.

2. Activate your virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and visit:  
   👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Model Building Process (Summary)

The **`music-recommendation-system.ipynb`** notebook details the model creation:

1. **Data Loading & Cleaning:**  
   Loaded Spotify track and artist data; handled missing song names.

2. **Feature Engineering:**  
   Merged datasets on artist ID, filtered songs (released ≥ 2000, popularity > 60), selected relevant audio features, and handled duplicate song names.

3. **Feature Scaling:**  
   Applied `MinMaxScaler` from Scikit-learn to normalize audio features between 0 and 1.

4. **Model Export:**  
   Saved final song data (`songs_dict.pkl`), scaled features array (`scaled_features.npy`), and popularity list (`popular.pkl`).  
   *(Similarity is now calculated on-the-fly in the app; `similarity.pkl` is deprecated.)*

---

## 💻 Technologies Used

| Technology | Purpose |
|-------------|----------|
| **Python** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations, saving scaled features |
| **Scikit-learn** | Feature scaling (`MinMaxScaler`), similarity calculation (`cosine_similarity`) |
| **Flask** | Backend web framework |
| **Spotipy** | Spotify API integration |
| **python-dotenv** | Secure management of API keys |
| **HTML** | Frontend structure |
| **Tailwind CSS** | Modern and responsive UI styling |
| **Jupyter Notebook** | Model development, EDA, and experimentation |
| **Git & GitHub** | Version control and hosting |

---

## 👨‍💻 Author

Project created by **[Rahul Dhaka]**  
[LinkedIn](https://www.linkedin.com/in/rahul-dhaka-56b975289/),  [GitHub](https://github.com/RahulDhaka29)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
