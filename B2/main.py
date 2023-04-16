import pandas as pd
from textblob import TextBlob

words_dictionary = {}
with open('wordlist.txt', 'r') as file:
    for line in file:
        words_dictionary[line.strip()] = 1

xlsx = pd.read_excel("TwitterHealthData.xlsx", dtype={'tweet_id':'int', 'tweet_text':'str'})

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

    xlsx['Sentiment'] = xlsx['Text'].apply(get_sentiment)

search = input('Enter a search term: ')

if search in words_dictionary:
        matches = []
