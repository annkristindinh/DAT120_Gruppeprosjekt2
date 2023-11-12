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

import csv #importerer slik at programmet leser csv filen
from datetime import datetime #Importerer datetime for å kunne lese datoer
import matplotlib.pyplot as plt #for å lage diagrammer

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
    #den tar inn filnavn som parameter og returner en liste med tupler, som inneholder 
    # datoer og verdier for skydekke fra filen som ble lest av. 

filnavn_skydekke = "snoedybder_vaer_en_stasjon_dogn.csv" #filnavnet defineres 

skydekke_data = les_skydekke_data(filnavn_skydekke) #filen leses av

år_penvær = {} #oppretter en tok dictonary for å holde oversikt over antall penversdager


for dato, skydekke in skydekke_data:
    år = dato.year
    if år not in år_penvær:
        år_penvær[år] = []
    if skydekke <= 3:
        år_penvær[år].append(1)
    else:
        år_penvær[år].append(0)
#Her itererer koden gjennom værdataene. For hver dag blir året hentet fra datoen.
# Hvis året ikke allerede er i år_penvær-dictionaryen, legges det til en tom liste for 
#å holde oversikt over penværsdager. Deretter blir det bestemt om dagen har pent vær 
#(skydekke <= 3), og verdien 1 eller 0 blir lagt til i listen for det aktuelle året.

gyldige_år_penvær = [år for år, data in år_penvær.items() if len(data) >= 300]
#opprettes en liste for årene der det er minst 300 dager

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





































