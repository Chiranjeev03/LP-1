import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')
# Load Amazon reviews data from a CSV file (change the file path accordingly)
amazon_reviews = pd.read_csv('amazon_reviews.csv')

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Create lists to store sentiment results
positive_sentiments = []
negative_sentiments = []
neutral_sentiments = []

# Analyze each review and store the results
for review_text in amazon_reviews['review_text']:
    sentiment_scores = analyzer.polarity_scores(review_text)
    if sentiment_scores['compound'] >= 0.05:
        positive_sentiments.append(review_text)
    elif sentiment_scores['compound'] <= -0.05:
        negative_sentiments.append(review_text)
    else:
        neutral_sentiments.append(review_text)


# Display the results
print(f'Positive Sentiments ({len(positive_sentiments)} {'review' if len(positive_sentiments) == 1 else 'reviews'}):\n')
for review in positive_sentiments:
    print(review)
print("\n")
print(f'Negative Sentiments ({len(negative_sentiments)} reviews):\n')
for review in negative_sentiments:
    print(review)
print("\n")
print(f'Neutral Sentiments ({len(neutral_sentiments)} {'review' if len(neutral_sentiments) == 1 else 'reviews'}):\n')
for review in neutral_sentiments:
    print(review)
