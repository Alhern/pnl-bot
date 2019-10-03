#! /usr/bin/env python
# -*- coding: utf-8 -*-


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


lion.close()
onizuka.close()
ninety1s.close()
deconnecte.close()
kutaubud.close()