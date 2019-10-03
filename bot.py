#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import tweepy
from time import sleep
from creds import *
from data import *


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
