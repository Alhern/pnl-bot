#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random, tweepy
from creds import *

lion = open("lion.txt", "r")
onizuka = open("onizuka.txt", "r")

lionLines = lion.readlines()
oniLines = onizuka.readlines()

allLines = [lionLines, oniLines]

print(random.choice(random.choice(allLines)))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

user = api.me()
print(user.name)

lion.close()
onizuka.close()
