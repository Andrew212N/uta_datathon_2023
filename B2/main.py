import pandas as pd

print('Find Health Tweets containing a specific medical term.\nInitializing word bank and Tweet bank...')
words_dictionary = {}
with open('wordlist.txt', 'r') as file:
    for line in file:
        words_dictionary[line.strip()] = 1

xlsx = pd.read_excel("TwitterHealthData.xlsx", usecols=['tweet_text'])
dataset = list(xlsx.iloc[:,0])

search = input('Enter a search term: ')
print('Printing out all the tweets that contain the word: ' + search +  '\nPlease wait a few seconds...\n')
search = search.lower()

if search in words_dictionary:
    matches = [entry for entry in dataset if any(word.lower() in entry.lower() for word in words_dictionary) and search in entry.lower()]
    if matches:
        for entry in matches:
            print(entry + '\n')
        print(f'Found {len(matches)} tweets')
    else:
        print('No entries found')
else:
    print(f'{search} is not in the word bank\nTry using different capitalization or dashes where there should be.')
