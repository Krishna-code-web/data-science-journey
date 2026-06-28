import streamlit as st
import pickle
import string

# Load model
model = pickle.load(open("emotion_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

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

def preprocess(text):
    text = text.lower()
    text = remove_punc(text)
    text = remove_numbers(text)
    text = remove_emojis(text)
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

    cleaned = preprocess(user_input)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    st.success(f"Predicted Emotion: {emotion_map[prediction]}")