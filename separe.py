import EDA
import get_Data
import set_api_values
import pandas as pd
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# # Ensure NLTK data is downloaded
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')



def sentimentsByPhases(data):
    # Assuming 'data' is your DataFrame
    # data = EDA.analysisEdaAPi()
    if data is None or data.empty:
        print("Warning: The input data is None. Exiting the function.")
        return None

    if 'sentiment' in data.columns:
        return data
    else:
        # Check if necessary NLTK resources are already downloaded, if not, download them
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')

        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')

        try:
            nltk.data.find('tokenizers/punkt_tab')
        except LookupError:
            nltk.download('punkt_tab')

        # Apply the function to the 'description' column and create a new column with the tokenized results
        data['tokenized_description'] = data['description'].apply(tokenize_description)
        print("data['tokenized_description']", data['tokenized_description'])

        # Print the first few rows to check the results
        # print(data[['description', 'tokenized_description']].head())

        # Apply the sentiment analysis function to the 'tokenized_description' column
        data['sentiment'] = data['tokenized_description'].apply(get_sentiment)

        # data = data.drop(columns=['tokenized_description'])

        # Print the first few rows to check the results
        # print(data[['description', 'tokenized_description', 'sentiment']].head())

        # Print the first few rows to check the results
        # print(data.head())

        # print(data.columns)

    return data

# Define a function to tokenize the descriptions
def tokenize_description(description):
    language = set_api_values.returnLongLanguage()
    if isinstance(description, str):
        tokens = nltk.word_tokenize(description)
        tokens = [word for word in tokens if word.isalnum()]  # Remove punctuation
        tokens = [word for word in tokens if word.lower() not in stopwords.words(f'{language}')]  # Remove stopwords
        # print('tokens', tokens)
        # return tokens
        return ' '.join(tokens)  # Join tokens back to a single string
    else:
        return []

# Define a function to perform sentiment analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'
