import streamlit as st
import pickle
import string
from pathlib import Path
from nltk.corpus import stopwords

# Load model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "emotion_model.pkl"
VECTORIZER_PATH = BASE_DIR / "tfidf_vectorizer.pkl"

if MODEL_PATH.exists() and VECTORIZER_PATH.exists():
    with MODEL_PATH.open("rb") as model_file:
        model = pickle.load(model_file)
    with VECTORIZER_PATH.open("rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
else:
    st.error("Model files were not found. Please make sure emotion_model.pkl and tfidf_vectorizer.pkl are in the same folder as this app.")
    model = None
    vectorizer = None

# Emotion Mapping
emotion_map = {
    0: "😢 Sadness",
    1: "😠 Anger",
    2: "❤️ Love",
    3: "😲 Surprise",
    4: "😨 Fear",
    5: "😊 Joy"
}

# -----------------------------
# Text Cleaning Functions
# -----------------------------

def remove_punc(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_numbers(text):
    return ''.join(i for i in text if not i.isdigit())

def remove_emojis(text):
    return ''.join(i for i in text if i.isascii())

try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    import nltk
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))


def remove_stopwords(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)


def preprocess(text):
    text = text.lower()
    text = remove_punc(text)
    text = remove_numbers(text)
    text = remove_emojis(text)
    text = remove_stopwords(text)
    return text

# -----------------------------
# UI
# -----------------------------

st.set_page_config(
    page_title="Emotion Detection",
    page_icon="😊"
)

st.title("😊 NLP Emotion Detection")

st.write("Enter any sentence below and the model will predict its emotion.")

user_input = st.text_area("Enter Text")

if st.button("Predict Emotion"):
    if model is None or vectorizer is None:
        st.error("The model could not be loaded. Please check the app directory.")
    else:
        cleaned = preprocess(user_input)
        print(cleaned)

        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)[0]

        st.success(f"Predicted Emotion: {emotion_map[prediction]}")