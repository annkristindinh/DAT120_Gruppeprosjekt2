#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:20:18 2023

@author: annkristin
"""

"""
f)
Bruk funksjonen fra del 1 oppgave f) til å finne den lengste perioden med tørke (ingen  nedbør) 
for hvert år i datasettet. Plott resultatet. Inkluder bare år hvor det er nedbørsdata
for mesteparten av året, det må være data for minst 300 dager for at et år skal være gyldig. 


Del 1, oppg.f)


def lengste_nullsekvens(liste):
    maks_lengde=0  #starter fra 0
    gjeldende_lengde=0   #hvor mange 0er det faktisk er
    
    for nummer in liste:
        if nummer==0:
            gjeldende_lengde+=1
            
            if gjeldende_lengde>maks_lengde:
                maks_lengde=gjeldende_lengde
        else:
           gjeldende_lengde=0
        
    return maks_lengde

min_liste=[0,2,0,0,2,0,0,0,0,0,2]
resultat=lengste_nullsekvens(min_liste)
print("Lengden på den lengste sammenhengende sekvensen av nuller er:", resultat)

"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

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
    maks_lengde = 0  # Starter fra 0
    gjeldende_lengde = 0  # Hvor mange 0er det faktisk er
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

filnavn = "snoedybder_vaer_en_stasjon_dogn.csv"
nedbørsdata = les_nedbørsdata(filnavn)

år_tørke = {}  # Lagre resultatet for hvert år

for dato, nedbør in nedbørsdata:
    år = dato.year
    if år not in år_tørke:
        år_tørke[år] = []
    år_tørke[år].append(nedbør)

gyldige_år = [år for år, data in år_tørke.items() if len(data) >= 300]

# Begrenser til de første tre gyldige årene
gyldige_år = gyldige_år[:3]

for år in gyldige_år:
    tørke_perioder = år_tørke[år]
    lengste_tørke = lengste_nullsekvens(tørke_perioder)
    print(f"År {år}: Lengste tørkeperiode = {len(lengste_tørke)} dager")

    # Plot resultatet
    plt.figure(figsize=(10, 4))
    plt.plot(list(år_tørke[år]))
    plt.title(f"Tørkeperioder i {år}")
    plt.grid(True)
    plt.xlabel("Dager")
    plt.ylabel("Nedbør (mm) 0 = tørke") 
    plt.show()

