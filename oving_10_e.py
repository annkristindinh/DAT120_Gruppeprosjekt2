#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:18:08 2023

@author: annkristin
"""

import csv
import matplotlib.pyplot as plt


def beregn_plantevekst(temp_liste):
    total_vekst = 0
    for temperatur in temp_liste:
        if temperatur == '-':
            continue  # Hopp over rader med manglende temperaturdata
        temperatur = float(temperatur.replace(',', '.'))  # Konverter temperatur til flyttall
        vekst = max(temperatur - 5, 0)  # Vekst er 0 hvis temperaturen er mindre enn 5 °C
        total_vekst += vekst
    return total_vekst

temperaturdata = {} # Initialiser variabler for å lagre temperaturdata
gyldige_aar_data = [] # Initialiser variabler for å lagre temperaturdata

# Les CSV-filen og analyser dataene
with open("snoedybder_vaer_en_stasjon_dogn.csv", mode="r", encoding="UTF-8") as fil:
    leser = csv.reader(fil, delimiter=';')
    next(leser)  # Hopp over overskriftsraden

    for kolonne in leser:
        aar = kolonne[2].split('.')[-1]
        temperatur = kolonne[5]  # Temperaturdata som streng

        if aar not in temperaturdata:
            temperaturdata[aar] = []

        temperaturdata[aar].append(temperatur)

for aar, temp_liste in temperaturdata.items(): # Filtrer og beregn plantevekst for gyldige år
    if len(temp_liste) >= 300:
        vekst = beregn_plantevekst(temp_liste)
        gyldige_aar_data.append((int(aar), vekst))


gyldige_aar_data.sort(key=lambda x: x[0]) # Sorter dataene for gyldige år etter år
aar, vekster = zip(*gyldige_aar_data) # Hent ut år og vekst for plotting

plt.plot(aar, vekster) # Plott planteveksten gjennom årene
plt.grid(True)
plt.xlabel('År')
plt.ylabel('Plantevekst')
plt.title('Plantevekst gjennom årene')
plt.show()






