import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv(r"D:\protest_tweets.csv")


# Label the sentiment using TextBlob
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["sentiment"] = df["text"].apply(get_sentiment)

# Convert text to features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["sentiment"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classifier
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Try with new input
def analyze_sentiment(new_text):
    x_new = vectorizer.transform([new_text])
    return clf.predict(x_new)[0]

# Example test
print("New sentence sentiment:", analyze_sentiment("People were shouting and breaking things."))
