#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import tweepy
from time import sleep
from creds import *

# The songs' files that will be used:
lion = open("lion.txt", "r")
onizuka = open("onizuka.txt", "r")
ninety1s = open("91s.txt", "r")
deconnecte = open("deconnecte.txt", "r")
kutaubud = open("kutaubud.txt", "r")


# Catching all the lines for each song:
lionLines = lion.readlines()
oniLines = onizuka.readlines()
ninety1sLines = ninety1s.readlines()
deconnecteLines = deconnecte.readlines()
kutaubudLines = kutaubud.readlines()


# Regrouping all the lines in one list:
allLines = [lionLines, oniLines, ninety1sLines, deconnecteLines, kutaubudLines]


# Authenticating
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Time to tweet:
def main():
    while True:
        try:
            randomLine = random.choice(random.choice(allLines))
            api.update_status(randomLine)
            print("Successfully tweeted: ", randomLine)
            sleep(1800)
        except tweepy.TweepError as e:
            print(e.api_code, e.reason)
            continue


if __name__ == "__main__":
    main()


lion.close()
onizuka.close()
ninety1s.close()
deconnecte.close()
kutaubud.close()