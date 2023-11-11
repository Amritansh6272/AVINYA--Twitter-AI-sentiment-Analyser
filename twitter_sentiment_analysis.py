from textblob import TextBlob
import tweepy
import sys

api_key = "M2kzFnI6rZiRbjWgxyxeRpPje" 
api_key_secret = "6AvKwGFrtzMXMuIJ201yOLRdFwt8Bz9iTfwdhRgIrfrQKyrbaj"
access_token = "1722861998344671232-ocW72w5q5mKbnMhEjgeRqXz1ZbNHgW"
access_token_secret = "XpoJyqk369snrH1LfFCr2ob0Sa4WkhqG28JmlseSU0RoB"

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'stocks'
tweet_amount = 200

tweets = tweepy.cursor(api.search, q=search_term, lang='en').items(tweet_amount)

polarity = 0
positive = 0
negative = 0
neutral = 0

for tweet in tweets:
    print(tweet)
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith('@'):
        position = final_text.index(":")
        final_text = final_text[position+2:]

    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position+2:]
    analysis = TextBlob (final_text)
    tweet_polarity = analysis_polarity
    if tweet_polarity > 0.00:
        positive += 1
    elif tweet_polarity < 0.00:
        negative += 1
    elif tweet_polarity == 0.00:
        neutral += 1
    else :
        neutral += 1
    polarity += analysis.polarity

print (polarity)

