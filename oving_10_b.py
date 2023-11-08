#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 12:52:50 2023

@author: annkristin
"""

"""
b) 
Dere kan regne med at det er skiføre om snødybden på værstasjonen er 20 centimeter eller mer. 
Regn ut antall dager med skiføre for hver vintersesong i datasettet. 
En vintersesong  strekker seg fra oktober ett år til juni året etterpå. 
Bruk funksjonen fra del 1 oppgave d) til å  beregne antall dager med skiføre i hver skisesong. 
Dette vil kreve at dere lager egne lister for  hver skisesong som dere kan bruke som input til 
funksjonen fra del 1 oppgave d) 


Del 1, oppgave d)
def tell_storre_enn_verdi(liste, verdi):
    antall_storre_enn_verdi=0
    for element in liste:
        if element>=verdi:
            antall_storre_enn_verdi+=1
    return antall_storre_enn_verdi

min_liste= [1.5, 2.0, 3.7, 4.2, 5.1, 6.7, 10.9]
min_verdi=3.0

resultat= tell_storre_enn_verdi(min_liste,min_verdi)
print(f"Antall elementer større enn eller lik {min_verdi}: {resultat}")


"""
import csv
from datetime import datetime


def les_snoedybde_data(filnavn):
    snoedybde_data = []
    with open(filnavn, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Leser headeren
        for row in reader:
            dato_str = row[2]
            snodybde_str = row[3].replace(',', '.')  # Erstatte komma med punktum som desimaltall
            if dato_str and snodybde_str != '-':
                dato = datetime.strptime(dato_str, '%d.%m.%Y')
                snodybde = float(snodybde_str)
                snoedybde_data.append((dato, snodybde))
    return snoedybde_data


def finn_vintersesonger(data):
    vintersesonger = []
    sesong_start = None

    for dato, snodybde in data:
        if dato.month >= 10:
            if sesong_start is None:
                sesong_start = dato
        elif dato.month < 6:
            if sesong_start is not None:
                vintersesonger.append((sesong_start, dato))
                sesong_start = None

    return vintersesonger

def antall_dager_med_skiføre(data, verdi):
    antall_dager = 0
    for dato, snodybde in data:
        if snodybde >= verdi:
            antall_dager += 1
    return antall_dager

filnavn = "snoedybder_vaer_en_stasjon_dogn.csv"
snoedybde_data = les_snoedybde_data(filnavn)
vintersesonger = finn_vintersesonger(snoedybde_data)
skiføre_verdi = 20  # Skiføre definert som 20 centimeter eller mer

for i, (start, slutt) in enumerate(vintersesonger):
    sesong_data = [(dato, snodybde) for dato, snodybde in snoedybde_data if start <= dato <= slutt]
    antall_dager = antall_dager_med_skiføre(sesong_data, skiføre_verdi)
    print(f"Vintersesong {i + 1}: Antall dager med skiføre = {antall_dager}")


