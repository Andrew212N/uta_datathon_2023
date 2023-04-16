import pandas as pd
from textblob import TextBlob
import random

xlsx = pd.read_excel("TwitterHealthData.xlsx", dtype={'tweet_id':'int', 'tweet_text':'str'})

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

    xlsx['Sentiment'] = xlsx['Text'].apply(get_sentiment)

num_rows = len(xlsx)

for i in range(20):
    rand_num = random.randint(0, num_rows-1)
    print('Tweet ID: ' + str(xlsx['tweet_id'].iloc[rand_num]))
    print(xlsx['tweet_text'].iloc[rand_num] + '\n')
