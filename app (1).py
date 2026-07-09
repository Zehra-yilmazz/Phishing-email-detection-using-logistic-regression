import re

import joblib
import nltk
import streamlit as st
from textblob import Word

# ---------------------------------------------------------------------------
# 0) ONE-TIME NLTK DATA DOWNLOAD (needed for lemmatization, same as the notebook)
# ---------------------------------------------------------------------------
@st.cache_resource
def ensure_nltk_data():
    nltk.download("wordnet", quiet=True)
    nltk.download("omw-1.4", quiet=True)


ensure_nltk_data()


# ---------------------------------------------------------------------------
# 1) LOAD THE SAVED MODEL + VECTORIZER
#    (these two files must sit in the same folder as app.py)
# ---------------------------------------------------------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return model, vectorizer


model, vectorizer = load_artifacts()


# ---------------------------------------------------------------------------
# 2) TEXT CLEANING
#    This mirrors EXACTLY the preprocessing used in the notebook's final
#    (cleaned-text) model, cell by cell:
#      - lowercase
#      - remove punctuation (regex: [^\w\s])
#      - remove digits (regex: \d)
#      - lemmatize each word with TextBlob's Word().lemmatize()
#    (TfidfVectorizer itself still handles lowercasing + English stopword
#    removal at the vectorize step, same as in the notebook.)
# ---------------------------------------------------------------------------
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d", "", text)
    text = " ".join(Word(w).lemmatize() for w in text.split())
    return text


# ---------------------------------------------------------------------------
# 3) STREAMLIT UI
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Phishing Email Detector", page_icon="🔒")

st.title("🔒 Phishing Email Detector")
st.write(
    "Paste the text of an email below. The model (Logistic Regression, "
    "trained on the [Phishing Emails Kaggle dataset]"
    "(https://www.kaggle.com/datasets/subhajournal/phishingemails)) "
    "will predict whether it's **safe** or **phishing**."
)

email_text = st.text_area(
    "Email content",
    height=250,
    placeholder="Paste the email text here...",
)

if st.button("Analyze", type="primary"):
    if not email_text.strip():
        st.warning("Please paste some email text first.")
    else:
        cleaned = clean_text(email_text)
        vectorized = vectorizer.transform([cleaned])

        prediction = model.predict(vectorized)[0]
        proba = model.predict_proba(vectorized)[0]
        confidence = max(proba) * 100

        # Label encoding confirmed from the notebook: 0 = Safe Email, 1 = Phishing Email
        if prediction == 1:
            st.error(f"⚠️ This looks like a **PHISHING** email ({confidence:.1f}% confidence)")
        else:
            st.success(f"✅ This looks like a **SAFE** email ({confidence:.1f}% confidence)")

        with st.expander("See the cleaned text sent to the model"):
            st.write(cleaned)

st.markdown("---")
st.caption("Logistic Regression model · Built by Zehra Yılmaz")
