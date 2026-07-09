# 🔒 Phishing Email Detection using Logistic Regression

A binary classification model that automatically detects phishing emails based on email text. The goal is to build a system that can distinguish "safe" emails from "phishing" emails in order to protect users from fraud/security risks — and to ship it as something people can actually try, not just a notebook.

## 🚀 Live Demo

**Try it here → https://phishing-email-detection-using-logistic-regression-8zr2v4rnn4t.streamlit.app/**

Paste any email text (yours or a made-up example) and get an instant Safe / Phishing prediction with a confidence score.

## 📊 Dataset

- Source: [Phishing Emails Dataset – Kaggle](https://www.kaggle.com/datasets/subhajournal/phishingemails)
- Content: raw email text + label (`Safe Email` / `Phishing Email`)
- Size: 18,650 emails (18,634 after removing 16 rows with missing text) — split 80/20 into train/test

## 🧠 Methodology

1. **Label Encoding:** `Safe Email → 0`, `Phishing Email → 1`
2. **Feature Extraction:** `TfidfVectorizer(min_df=1, stop_words="english", lowercase=True)` — converts each email into a weighted word-frequency vector
3. **Modeling:** Logistic Regression (scikit-learn) trained on the TF-IDF features
4. **Evaluation:** Accuracy, precision/recall/F1, and a confusion matrix on the held-out 20% test set
5. **Experiment — does text cleaning help?** A second version of the pipeline lowercases, strips punctuation/digits, and lemmatizes (TextBlob) the text before vectorizing, to test whether heavier cleaning improves results (see "What We Learned" below)
6. **Deployment:** the trained model + vectorizer are saved with `joblib` and served through a Streamlit web app for live predictions

## ✅ Results

The deployed model is the cleaned + lemmatized version, matching the headline number below:

| Metric | Safe (0) | Phishing (1) | Overall |
|---|---|---|---|
| Precision | 0.97 | 0.98 | — |
| Recall | 0.99 | 0.96 | — |
| F1-Score | 0.98 | 0.97 | — |
| **Accuracy** | | | **97.6%** |

Confusion matrix (rows = actual, columns = predicted):

| | Predicted Safe | Predicted Phishing |
|---|---|---|
| **Actual Safe** | 2193 | 27 |
| **Actual Phishing** | 60 | 1341 |

## 🎓 What We Learned

**Cleaning text doesn't automatically make a model better.** We compared the raw-text pipeline against the cleaned + lemmatized one:

| Version | Accuracy | Phishing Recall |
|---|---|---|
| Raw text (no cleaning) | **98.3%** | 97% |
| Cleaned + lemmatized | 97.6% | 96% |

The raw-text model actually performed slightly better. Our read on why: `TfidfVectorizer` already lowercases and strips English stopwords on its own, so the extra cleaning mostly removed information (punctuation patterns, digit sequences, capitalization) that turned out to carry real signal for spotting phishing emails, without adding enough noise reduction to make up for it. Lesson: always benchmark preprocessing changes against a baseline instead of assuming "more cleaning = better."

**Recall matters more than accuracy for a security use case.** Looking at the confusion matrix, the model's most expensive mistake is a false negative — a phishing email predicted as "safe" (60 cases). In a real inbox-protection product we'd tune the decision threshold or use `class_weight` to push recall on the phishing class even higher, accepting a few more false alarms in exchange for catching more real threats.

**Training a model and shipping it are two different skills.** Getting from a notebook with 98% accuracy to a working public demo surfaced its own set of problems — keeping the app's text-cleaning function in exact sync with the notebook's, matching `requirements.txt` to what the app actually imports, and (very literally) making sure filenames don't have stray characters in them. None of that shows up in a confusion matrix, but it's most of what makes a model usable by someone other than its author.

## 🛠️ Tech Stack

Python · Pandas · NumPy · Scikit-learn · TextBlob/NLTK (lemmatization) · Matplotlib/Seaborn · Streamlit (deployment) · joblib (model persistence)

## 📁 Project Structure

```
├── phishing-email-detection-using-logistic-regression.ipynb   # training, evaluation, experiments
├── app.py                                                      # Streamlit app for live predictions
├── requirements.txt                                            # dependencies for the app
├── model.pkl                                                   # trained Logistic Regression model
└── vectorizer.pkl                                              # fitted TF-IDF vectorizer
```

## ▶️ How to Run Locally

**Explore the analysis:**
```bash
git clone https://github.com/Zehra-yilmazz/Phishing-email-detection-using-logistic-regression.git
cd Phishing-email-detection-using-logistic-regression
jupyter notebook phishing-email-detection-using-logistic-regression.ipynb
```

**Run the app:**
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🔭 Next Steps

- Tune the classification threshold / `class_weight` to reduce false negatives on the phishing class
- Compare TF-IDF against word embeddings or DistilBERT
- Add a "why was this flagged" explanation (e.g. top contributing words) to the app output

---
*This project was developed by [Zehra Yılmaz](https://www.linkedin.com/in/zehra-yılmaz-b24793303).*
