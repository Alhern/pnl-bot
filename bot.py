#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

lion = open("lion.txt", "r")

lionLines = lion.readlines()

print(random.choice(lionLines))

lion.close()
