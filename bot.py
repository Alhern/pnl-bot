#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

lion = open("lion.txt", "r")
onizuka = open("onizuka.txt", "r")

lionLines = lion.readlines()
oniLines = onizuka.readlines()

allLines = [lionLines, oniLines]

print(random.choice(random.choice(allLines)))

lion.close()
onizuka.close()
