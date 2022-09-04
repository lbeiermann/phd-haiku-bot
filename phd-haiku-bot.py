import tweepy
consumer_key = 'your key here' 
consumer_secret = 'your secret here' 
access_token = 'your access token here' 
access_token_secret = 'your access token secret here' 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

part1 = ["today in the lab /", "the cat is my friend /", "a blank page staring /", "cannot stop reading /", "cannot stop thinking /", "i've found the right page /", "i've made a new friend /", "i'm glued to my chair /", "my fingers typing /", "i have the best job /"]
part2 = ["take a break when you read this /", "crumpled paper in the bin /", "so highly motivated /", "just write when the baby writes /", "moving out and never in /", "i'm writing to apply for /", "a whole book for a footnote /", "but do they pay you for that /", "pasta with cheese pasta with /", "the birds outside my window /", "i dream of philosophers /", "i sleep on a stack of books /", "where has everyone gone /", "who wrote it first thought it first /"]
part3 = ["the sound of the rain //", "running on coffee //", "eat write eat write sleep //", "la dolce vita //", "the things i could do //", "rising with the sun //", "let's go for coffee //", "the places i'll go //", "the fridge is empty //", "the sun sets early //", "publish and perish //", "thinking of the sea //"]

best_words = [part1, part2, part3]

import random

sentence = []

for i in best_words:
    r = random.randint(0, len(i) - 1)
    sentence.append(i[r])

print(" ".join(sentence) + " #PhDLife")
api.update_status(" ".join(sentence) + " #PhDLife")
