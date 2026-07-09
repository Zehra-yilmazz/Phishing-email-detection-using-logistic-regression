Phishing Email Detection using Logistic Regression

A binary classification model that automatically detects phishing emails based on email text. The goal is to build a system that can distinguish "safe" emails from "phishing" emails in order to protect users from potential fraud/security risks.

📊 Dataset


Source: Phishing Emails Dataset – Kaggle
Content: Email text and label (Safe Email / Phishing Email)



🧠 Methodology


Preprocessing: [FILL IN: the cleaning steps you applied — e.g. lowercasing, HTML/punctuation removal, stopword removal]
Feature Extraction: [FILL IN: did you use TF-IDF, CountVectorizer, or another method?]
Modeling: Binary classification with Logistic Regression (scikit-learn)
Evaluation: Performance metrics computed on the held-out test set


✅ Results

MetricValue
Accuracy: 0.975973487986744
              precision    recall  f1-score   support

           0       0.97      0.99      0.98      2220
           1       0.98      0.96      0.97      1401







🛠️ Tech Stack

Python · Pandas · NumPy · Scikit-learn · Matplotlib/Seaborn

▶️ How to Run

bashgit clone https://github.com/Zehra-yilmazz/Phishing-email-detection-using-logistic-regression.git
cd Phishing-email-detection-using-logistic-regression
pip install -r requirements.txt   # if missing: pip install pandas numpy scikit-learn matplotlib seaborn
jupyter notebook phishing-email-detection-using-logistic-regression.ipynb


My LinkedIn:www.linkedin.com/in/zehra-yılmaz-b24793303
