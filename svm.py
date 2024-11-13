import spacy
import nltk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from nltk.stem import WordNetLemmatizer
import subprocess

import get_and_set_env
import separe
import EDA
import os
import json
import csv_to_sql

language = get_and_set_env.returnLanguageKey()
# nlp = spacy.load("en_core_web_sm")

# Define a mapping of languages to their respective Spacy models
LANGUAGE_MODELS = {
    'en': 'en_core_web_sm',
    'es': 'es_core_news_sm',
    'de': 'de_core_news_sm',
    'fr': 'fr_core_news_sm',
    'it': 'it_core_news_sm',
    'nl': 'nl_core_news_sm',
    'zh': 'zh_core_web_sm',
    'pt': 'pt_core_news_sm',
}

# Function to download the Spacy model if not already installed
def download_model(model_name):
    try:
        spacy.load(model_name)
    except OSError:
        print(f"Downloading model {model_name}...")
        subprocess.run(['python', '-m', 'spacy', 'download', model_name], check=True)
        print(f"Model {model_name} downloaded successfully.")

# Function to load the Spacy model based on the selected language
def load_model(language):
    model_name = LANGUAGE_MODELS.get(language)
    if model_name:
        download_model(model_name)
        return spacy.load(model_name)
    else:
        raise ValueError(f"Unsupported language: {language}")

# nlp = spacy.load("en_core_web_sm")
nlp = load_model(language)

# nltk.download('punk')
# nltk.download('wordnet')
def import_punkt_stopwords():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

def get_data():
    APi_data_without_sentiments = EDA.analysisEdaAPi()
    print()
    print('APi_data_without_sentiments', APi_data_without_sentiments)
    print()
    # print('APi_data_without_sentiments', APi_data_without_sentiments)
    CSV_df_without_sentiments = EDA.analysisEdaCSV()
    # print('CSV_df_without_sentiments ', CSV_df_without_sentiments)
    return APi_data_without_sentiments, CSV_df_without_sentiments
    # return CSV_df_without_sentiments

# if df is None or df.empty:
#     return None

import_punkt_stopwords()
APi_data_without_sentiments, CSV_df_without_sentiments = get_data()
# print('APi_data_without_sentiments', APi_data_without_sentiments)
# CSV_df_without_sentiments = get_data()

# Assuming 'data' is your DataFrame
# if APi_data_without_sentiments is not None and not APi_data_without_sentiments.empty:

df = separe.sentimentsByPhases(APi_data_without_sentiments)
print('size=' , df.groupby('sentiment').size())
# Save the resulting DataFrame to a CSV file
df.to_csv(f'./result_data/APiData.csv', index=False)

data = separe.sentimentsByPhases(CSV_df_without_sentiments)
print('size=' ,data.groupby('sentiment').size())
data.to_csv(f'./result_data/KaggleData.csv', index=False)

# Concatenate the DataFrames along the rows
merged_df = pd.concat([data, df], axis=0)
# merged_df = data
test = merged_df.groupby('sentiment').size()
test2 = test.min()
# print('test', test)
# print('test2', test2)
# Create a dictionary to hold DataFrames for each sentiment
sentiment_dfs = pd.concat([merged_df[merged_df['sentiment'] == sentiment].head(test2) for sentiment in ['positive', 'negative', 'neutral']], ignore_index=True)

# Save the resulting DataFrame to a CSV file
sentiment_dfs.to_csv(f'./result_data/dataTraining.csv', index=False)

# Probar las cantidad de valores en excel
# =COUNTIFS(G:G, "positive")
# =COUNTIFS(G:G, "negative")
# =COUNTIFS(G:G, "neutral")

def preprocess_text(text):
    # Remove numbers and special characters
    text = ''.join(char for char in text if char.isalnum() or char.isspace())

    doc = nlp(text)
    # Tokenización: Filtramos los tokens que no son stopwords ni puntuación
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    # print(tokens)

    # Reconocimiento de entidades nombradas (NER): Extraer entidades si es necesario
    entities = [ent.text for ent in doc.ents]

    return " ".join(tokens)

# Aplicar preprocesamiento a las frases
sentiment_dfs['clean_text'] = sentiment_dfs['description'].apply(preprocess_text)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sentiment_dfs['clean_text'])
y = sentiment_dfs['sentiment'].map({'positive': 1, 'negative': -1, 'neutral': 0})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, labels=[-1, 0, 1], target_names=['negative', 'neutral', 'positive']))


def sentiment_model():
    vectorizer = TfidfVectorizer()
    # X = vectorizer.fit_transform(sentiment_dfs['description'])
    X = vectorizer.fit_transform(sentiment_dfs['clean_text'])
    # print(X)

def predict_sentiment(text):
    # Preprocesar el texto
    clean_text = preprocess_text(text)

    # Vectorizar el texto
    text_vector = vectorizer.transform([clean_text])

    # Hacer la predicción
    sentiment = model.predict(text_vector)[0]

    # Traducir la predicción de vuelta a sentimiento
    sentiment_map = {1: 'positive', -1: 'negative', 0: 'neutral'}

    return sentiment_map[sentiment]

# Probar el modelo con frases de ejemplo
import call_json
test_phrases = call_json.calljson()

# Predict sentiment for each test phrase
for phrase in test_phrases:
    sentiment = predict_sentiment(phrase)
    print(f"Phrase: '{phrase}' -> Sentiment: {sentiment}")

sentiment_dfs.to_csv(f'./result_data/sentiment_dfs.csv', index=False)
csv_to_sql.csv_to_sql(f'./result_data/sentiment_dfs.csv', 'sentiment_dfs', 'sentiments')

def probe_model():
    while True:
        user_input = input("Enter a phrase to analyze sentiment (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        sentiment = predict_sentiment(user_input)
        print(f"Sentiment: {sentiment}")

# # Call the function to start probing the model with user input
probe_model()
