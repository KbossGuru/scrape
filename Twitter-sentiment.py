from transformers import AutoTokenizer, AutoModelForSequenceClassification

from scipy.special import softmax

tweet = "@MehranShakarami today's cold @  home https://mehranshakarami.com"

#preprocess tweet

tweet_word = []

for word in tweet.split(' '):
    if word.startswith('@') and len(word) > 1:
        word = '@user'
    elif word.startswith('http'):
        word = "http"
    tweet_word.append(word)

tweet_proc = " ".join(tweet_word)   

# loadd model and tokenizer

roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)

tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negtative', 'Neutral', 'Positive']

#sentiment analysis

encoded_tweet = tokenizer(tweet_proc, return_tensors = 'pt')

print(encoded_tweet)