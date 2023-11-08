#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:21:18 2023

@author: annkristin
"""

"""
g) 
Finn antall penværsdager for hvert år og plott dette. Man kan finne antall penværsdager ved 
å sjekke gjennomsnittlig skydekke. Hver dag med verdi 3 eller lavere er en penværsdag. 
Inkluder bare år hvor det er data om skydekke for mesteparten av året, det må være data for 
minst 300 dager for at et år skal være gyldig. 

"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

def les_skydekke_data(filnavn):
    skydekke_data = []
    with open(filnavn, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Leser headeren
        for row in reader:
            dato_str = row[2]
            if dato_str:
                dato = datetime.strptime(dato_str, '%d.%m.%Y')
                skydekke_str = row[6].replace(',', '.')  # Erstatte komma med punktum som desimaltall
                if skydekke_str != '-' and skydekke_str != '':
                    skydekke = float(skydekke_str)
                    skydekke_data.append((dato, skydekke))
    return skydekke_data

def les_nedbørsdata(filnavn):
    nedbørsdata = []
    with open(filnavn, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Leser headeren
        for row in reader:
            dato_str = row[2]
            if dato_str:
                dato = datetime.strptime(dato_str, '%d.%m.%Y')
                nedbør_str = row[4].replace(',', '.')  # Erstatte komma med punktum som desimaltall
                if nedbør_str != '-':
                    nedbør = float(nedbør_str)
                    nedbørsdata.append((dato, nedbør))
    return nedbørsdata

def lengste_nullsekvens(liste):
    maks_lengde = 0
    gjeldende_lengde = 0
    lengste_tørke = []

    for nummer in liste:
        if nummer == 0:
            gjeldende_lengde += 1
            if gjeldende_lengde > maks_lengde:
                maks_lengde = gjeldende_lengde
                lengste_tørke = [0] * maks_lengde
        else:
            gjeldende_lengde = 0

    return lengste_tørke

filnavn_skydekke = "snoedybder_vaer_en_stasjon_dogn.csv"
filnavn_nedbør = "snoedybder_vaer_en_stasjon_dogn.csv"

skydekke_data = les_skydekke_data(filnavn_skydekke)
nedbørsdata = les_nedbørsdata(filnavn_nedbør)

år_penvær = {}
år_tørke = {}

maks_år = 3  # Begrenser til de tre første årene

for dato, skydekke in skydekke_data:
    år = dato.year
    if år not in år_penvær:
        år_penvær[år] = []
    if skydekke <= 3:
        år_penvær[år].append(1)
    else:
        år_penvær[år].append(0)

for dato, nedbør in nedbørsdata:
    år = dato.year
    if år not in år_tørke:
        år_tørke[år] = []
    if nedbør == 0:
        år_tørke[år].append(0)
    else:
        år_tørke[år].append(1)

gyldige_år_penvær = [år for år, data in år_penvær.items() if len(data) >= 300]
gyldige_år_tørke = [år for år, data in år_tørke.items() if len(data) >= 300]

# Begrenser til de tre første gyldige årene
gyldige_år_penvær = gyldige_år_penvær[:maks_år]
gyldige_år_tørke = gyldige_år_tørke[:maks_år]

for år in gyldige_år_penvær:
    penvær_dager = sum(år_penvær[år])
    print(f"År {år}: Antall penværsdager = {penvær_dager}")

    # Plot penværsdager
    plt.figure(figsize=(10, 4))
    plt.plot(list(år_penvær[år]))
    plt.title(f"Penværsdager i {år}")
    plt.xlabel("Dager")
    plt.ylabel("Penvær (1 = penværsdag)")
    plt.show()

for år in gyldige_år_tørke:
    tørke_perioder = år_tørke[år]
    lengste_tørke = lengste_nullsekvens(tørke_perioder)
    print(f"År {år}: Lengste tørkeperiode = {len(lengste_tørke)} dager")

    # Plot tørkeperioder
    plt.figure(figsize=(10, 4))
    plt.plot(list(år_tørke[år]))
    plt.title(f"Tørkeperioder i {år}")
    plt.xlabel("Dager")
    plt.ylabel("Nedbør (0 = tørke)")
    plt.show()

































