#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import tweepy
from creds import *

# The songs' files that will be used:
lion = open("lion.txt", "r")
onizuka = open("onizuka.txt", "r")


# Catching all the lines for each song:
lionLines = lion.readlines()
oniLines = onizuka.readlines()


# Regrouping all the lines in one list:
allLines = [lionLines, oniLines]


# Authenticating
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Time to tweet:
def tweet():
    api.update_status(random.choice(random.choice(allLines)))


tweet()

lion.close()
onizuka.close()
